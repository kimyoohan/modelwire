#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.audit_external import (
    classify,
    compare_litellm,
    compare_modelsdev,
    litellm_value,
)


def fact():
    return {
        "provider": "acme",
        "model_id": "model-a",
        "pricing": {
            "input_per_mtok": 1.0,
            "output_per_mtok": 2.0,
            "cached_input_per_mtok": 0.1,
        },
        "context_window_tokens": 1000,
        "max_output_tokens": 100,
    }


class AuditExternalTests(unittest.TestCase):
    def test_litellm_prices_are_converted_from_per_token_to_per_mtok(self):
        record = {
            "input_cost_per_token": 0.000001,
            "output_cost_per_token": 0.000002,
            "cache_read_input_token_cost": 0.0000001,
        }

        self.assertEqual(litellm_value(record, "pricing.input_per_mtok"), 1.0)
        self.assertEqual(litellm_value(record, "pricing.output_per_mtok"), 2.0)
        self.assertAlmostEqual(litellm_value(record, "pricing.cached_input_per_mtok"), 0.1)

    def test_tolerance_logic_for_prices_and_token_limits(self):
        self.assertEqual(classify(100.0, 100.4, "pricing.input_per_mtok"), "match")
        self.assertEqual(classify(100.0, 100.6, "pricing.input_per_mtok"), "mismatch")
        self.assertEqual(classify(1000, 1000, "context_window_tokens"), "match")
        self.assertEqual(classify(1000, 1001, "context_window_tokens"), "mismatch")

    def test_alias_resolution_uses_mapped_litellm_key(self):
        rows = compare_litellm(
            fact(),
            {"litellm": ["external/model-a"]},
            {
                "external/model-a": {
                    "input_cost_per_token": 0.000001,
                    "output_cost_per_token": 0.000002,
                    "cache_read_input_token_cost": 0.0000001,
                    "max_input_tokens": 1000,
                    "max_output_tokens": 100,
                }
            },
        )

        self.assertEqual({row["status"] for row in rows}, {"match"})
        self.assertEqual({row["alias"] for row in rows}, {"external/model-a"})

    def test_not_present_we_lack_and_they_lack_are_classified(self):
        self.assertEqual(compare_litellm(fact(), {"litellm": []}, [])[0]["status"], "not_present")

        ours_missing = fact()
        ours_missing["pricing"]["cached_input_per_mtok"] = None
        rows = compare_modelsdev(
            ours_missing,
            {"modelsdev": [{"provider": "acme", "model": "model-a"}]},
            {
                "acme": {
                    "models": {
                        "model-a": {
                            "cost": {"input": 1.0, "output": 2.0, "cache_read": 0.1},
                            "limit": {"context": 1000, "output": 100},
                        }
                    }
                }
            },
        )
        self.assertEqual(next(row for row in rows if row["field"] == "pricing.cached_input_per_mtok")["status"], "we_lack")

        theirs_missing = fact()
        rows = compare_modelsdev(
            theirs_missing,
            {"modelsdev": [{"provider": "acme", "model": "model-a"}]},
            {
                "acme": {
                    "models": {
                        "model-a": {
                            "cost": {"input": 1.0, "output": 2.0},
                            "limit": {"context": 1000, "output": 100},
                        }
                    }
                }
            },
        )
        self.assertEqual(next(row for row in rows if row["field"] == "pricing.cached_input_per_mtok")["status"], "they_lack")


if __name__ == "__main__":
    unittest.main()
