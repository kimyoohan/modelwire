# Baseline Regeneration - 2026-07-07

Regenerated `ops/logic-baseline.json` from the current clean `py scripts\logic_check.py --today 2026-07-07 --write-baseline` run.

## Summary

- Old UNSUPPORTED count: 191
- New UNSUPPORTED count: 184
- Delta: -7
- Total accepted warning findings in regenerated baseline: 271

## Counts by class

| Class | Count |
| --- | ---: |
| AMBIGUOUS | 69 |
| RULE-4 | 15 |
| RULE-5 | 3 |
| UNSUPPORTED | 184 |

## Breakdown by field/class

| Field | Class | Count |
| --- | --- | ---: |
| context_window_tokens | AMBIGUOUS | 40 |
| max_output_tokens | AMBIGUOUS | 29 |
| modalities | UNSUPPORTED | 68 |
| pricing.cached_input_per_mtok | RULE-4 | 4 |
| pricing.input_per_mtok | RULE-4 | 5 |
| pricing.output_per_mtok | RULE-4 | 6 |
| status | RULE-5 | 3 |
| status | UNSUPPORTED | 116 |

## Remaining findings classification

| Entry | Field | Class | Classification | Detail |
| --- | --- | --- | --- | --- |
| alibaba/qwen3-max | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256K can mean decimal 256000 or binary 262144 tokens |
| alibaba/qwen3-max-2026-01-23 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256K can mean decimal 256000 or binary 262144 tokens |
| alibaba/qwen3.6-flash | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| alibaba/qwen3.6-flash-2026-04-16 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| alibaba/qwen3.6-max-preview | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256K can mean decimal 256000 or binary 262144 tokens |
| alibaba/qwen3.6-plus | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| alibaba/qwen3.6-plus-2026-04-02 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| alibaba/qwen3.7-plus | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| alibaba/qwen3.7-plus-2026-05-26 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| amazon/amazon.nova-lite-v1:0 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 300000 only matches ambiguous quote unit(s): 300k can mean decimal 300000 or binary 307200 tokens; 300k can mean decimal 300000 or binary 307200 tokens |
| amazon/amazon.nova-lite-v1:0 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 10000 only matches ambiguous quote unit(s): 10K can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens |
| amazon/amazon.nova-micro-v1:0 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens |
| amazon/amazon.nova-micro-v1:0 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 10000 only matches ambiguous quote unit(s): 10K can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens |
| amazon/amazon.nova-premier-v1:0 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| amazon/amazon.nova-premier-v1:0 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 10000 only matches ambiguous quote unit(s): 10K can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens |
| amazon/amazon.nova-pro-v1:0 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 300000 only matches ambiguous quote unit(s): 300k can mean decimal 300000 or binary 307200 tokens; 300k can mean decimal 300000 or binary 307200 tokens |
| amazon/amazon.nova-pro-v1:0 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 10000 only matches ambiguous quote unit(s): 10K can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens; 10k can mean decimal 10000 or binary 10240 tokens |
| amazon/anthropic.claude-3-5-sonnet-20241022-v2:0 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 200000 only matches ambiguous quote unit(s): 200K can mean decimal 200000 or binary 204800 tokens |
| anthropic/claude-fable-5 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| anthropic/claude-fable-5 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens |
| anthropic/claude-haiku-4-5-20251001 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 200000 only matches ambiguous quote unit(s): 200k can mean decimal 200000 or binary 204800 tokens |
| anthropic/claude-haiku-4-5-20251001 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| anthropic/claude-opus-4-6 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens |
| anthropic/claude-opus-4-7 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens |
| anthropic/claude-opus-4-8 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| anthropic/claude-opus-4-8 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens |
| anthropic/claude-sonnet-5 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| anthropic/claude-sonnet-5 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens |
| cohere/c4ai-aya-expanse-32b | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens |
| cohere/c4ai-aya-expanse-32b | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens; 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens; 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command-a-03-2025 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256k can mean decimal 256000 or binary 262144 tokens; 256k can mean decimal 256000 or binary 262144 tokens |
| cohere/command-a-03-2025 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 8000 only matches ambiguous quote unit(s): 8k can mean decimal 8000 or binary 8192 tokens; 8K can mean decimal 8000 or binary 8192 tokens; 8k can mean decimal 8000 or binary 8192 tokens |
| cohere/command-a-plus-05-2026 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens; 128K can mean decimal 128000 or binary 131072 tokens |
| cohere/command-a-plus-05-2026 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 64000 only matches ambiguous quote unit(s): 64k can mean decimal 64000 or binary 65536 tokens |
| cohere/command-a-reasoning-08-2025 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256k can mean decimal 256000 or binary 262144 tokens; 256k can mean decimal 256000 or binary 262144 tokens |
| cohere/command-a-reasoning-08-2025 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 32000 only matches ambiguous quote unit(s): 32k can mean decimal 32000 or binary 32768 tokens |
| cohere/command-a-translate-08-2025 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 8000 only matches ambiguous quote unit(s): 8k can mean decimal 8000 or binary 8192 tokens; 8K can mean decimal 8000 or binary 8192 tokens; 8k can mean decimal 8000 or binary 8192 tokens |
| cohere/command-a-translate-08-2025 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 8000 only matches ambiguous quote unit(s): 8k can mean decimal 8000 or binary 8192 tokens; 8K can mean decimal 8000 or binary 8192 tokens; 8k can mean decimal 8000 or binary 8192 tokens |
| cohere/command-a-vision-07-2025 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens; 128K can mean decimal 128000 or binary 131072 tokens |
| cohere/command-a-vision-07-2025 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 8000 only matches ambiguous quote unit(s): 8k can mean decimal 8000 or binary 8192 tokens; 8K can mean decimal 8000 or binary 8192 tokens; 8k can mean decimal 8000 or binary 8192 tokens |
| cohere/command-light | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens; 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command-light | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens; 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command-r-03-2024 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens |
| cohere/command-r-03-2024 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command-r-08-2024 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens; 128k can mean decimal 128000 or binary 131072 tokens; 128K can mean decimal 128000 or binary 131072 tokens |
| cohere/command-r-08-2024 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens; 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command-r-plus-04-2024 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens |
| cohere/command-r-plus-04-2024 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/command-r-plus-08-2024 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128k can mean decimal 128000 or binary 131072 tokens |
| cohere/command-r-plus-08-2024 | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 4000 only matches ambiguous quote unit(s): 4k can mean decimal 4000 or binary 4096 tokens |
| cohere/tiny-aya-global | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 8000 only matches ambiguous quote unit(s): 8k can mean decimal 8000 or binary 8192 tokens; 8k can mean decimal 8000 or binary 8192 tokens |
| cohere/tiny-aya-global | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 8000 only matches ambiguous quote unit(s): 8k can mean decimal 8000 or binary 8192 tokens; 8k can mean decimal 8000 or binary 8192 tokens |
| deepseek/deepseek-v4-flash | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| deepseek/deepseek-v4-flash | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 384000 only matches ambiguous quote unit(s): 384K can mean decimal 384000 or binary 393216 tokens |
| deepseek/deepseek-v4-pro | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| deepseek/deepseek-v4-pro | max_output_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 384000 only matches ambiguous quote unit(s): 384K can mean decimal 384000 or binary 393216 tokens |
| moonshot/kimi-k2.5 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256k can mean decimal 256000 or binary 262144 tokens |
| moonshot/kimi-k2.6 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256k can mean decimal 256000 or binary 262144 tokens |
| moonshot/kimi-k2.7-code | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256k can mean decimal 256000 or binary 262144 tokens |
| perplexity/sonar-pro | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 200000 only matches ambiguous quote unit(s): 200K can mean decimal 200000 or binary 204800 tokens |
| perplexity/sonar-reasoning-pro | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 128000 only matches ambiguous quote unit(s): 128K can mean decimal 128000 or binary 131072 tokens |
| together/Qwen/Qwen2.5-7B-Instruct-Turbo | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 32768 only matches ambiguous quote unit(s): 32K can mean decimal 32000 or binary 32768 tokens |
| xai/grok-4.20-0309-non-reasoning | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| xai/grok-4.20-0309-reasoning | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| xai/grok-4.20-multi-agent-0309 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| xai/grok-4.3 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 1000000 only matches ambiguous quote unit(s): 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens; 1M can mean decimal 1000000 or binary 1048576 tokens |
| xai/grok-build-0.1 | context_window_tokens | AMBIGUOUS | Still-unhandled parser case: shorthand numeric unit is ambiguous without a decimal/binary convention. | stored value 256000 only matches ambiguous quote unit(s): 256k can mean decimal 256000 or binary 262144 tokens |
| alibaba/qwen3.7-max <> together/qwen3.7-max | pricing.input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 2.5 vs 1.25 |
| alibaba/qwen3.7-max <> together/qwen3.7-max | pricing.output_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 7.5 vs 3.75 |
| fireworks/glm-5.1-fast <> together/glm-5.1 | pricing.cached_input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 0.52 vs 0.26 |
| fireworks/glm-5.1-fast <> together/glm-5.1 | pricing.input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 2.8 vs 1.4 |
| fireworks/glm-5.1-fast <> together/glm-5.1 | pricing.output_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 8.8 vs 4.4 |
| fireworks/glm-5.1-fast <> zhipu/glm-5.1 | pricing.cached_input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 0.52 vs 0.26 |
| fireworks/glm-5.1-fast <> zhipu/glm-5.1 | pricing.input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 2.8 vs 1.4 |
| fireworks/glm-5.1-fast <> zhipu/glm-5.1 | pricing.output_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 8.8 vs 4.4 |
| fireworks/kimi-k2.6-fast <> moonshot/kimi-k2.6 | pricing.output_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 8.0 vs 4.0 |
| fireworks/kimi-k2.7-code-fast <> moonshot/kimi-k2.7-code | pricing.cached_input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 0.38 vs 0.19 |
| fireworks/kimi-k2.7-code-fast <> moonshot/kimi-k2.7-code | pricing.input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 1.9 vs 0.95 |
| fireworks/kimi-k2.7-code-fast <> moonshot/kimi-k2.7-code | pricing.output_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 8.0 vs 4.0 |
| fireworks/kimi-k2.7-code-fast <> together/kimi-k2.7-code | pricing.cached_input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 0.38 vs 0.19 |
| fireworks/kimi-k2.7-code-fast <> together/kimi-k2.7-code | pricing.input_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 1.9 vs 0.95 |
| fireworks/kimi-k2.7-code-fast <> together/kimi-k2.7-code | pricing.output_per_mtok | RULE-4 | Real review gap: invariant warning remains; this is not a quote-parser miss. | same canonical model prices are exact 2x/10x ratio: 8.0 vs 4.0 |
| minimax/minimax-m2.7 | status | RULE-5 | Real review gap: invariant warning remains; this is not a quote-parser miss. | active status but source 0 contains inactive language: Legacy |
| minimax/minimax-m3 | status | RULE-5 | Real review gap: invariant warning remains; this is not a quote-parser miss. | active status but source 0 contains inactive language: Legacy |
| perplexity/sonar-reasoning-pro | status | RULE-5 | Real review gap: invariant warning remains; this is not a quote-parser miss. | active status but source 1 contains inactive language: deprecated |
| alibaba/qwen3-max | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3-max | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3-max-2026-01-23 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3-max-2026-01-23 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.6-flash | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.6-flash-2026-04-16 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.6-max-preview | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3.6-plus | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.6-plus-2026-04-02 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.7-max | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3.7-max | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.7-max-2026-05-17 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3.7-max-2026-05-17 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.7-max-2026-05-20 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3.7-max-2026-05-20 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.7-max-preview | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| alibaba/qwen3.7-plus | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| alibaba/qwen3.7-plus-2026-05-26 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| amazon/amazon.nova-lite-v1:0 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| amazon/amazon.nova-micro-v1:0 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| amazon/amazon.nova-premier-v1:0 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| amazon/amazon.nova-pro-v1:0 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| amazon/anthropic.claude-3-5-sonnet-20241022-v2:0 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| amazon/anthropic.claude-3-5-sonnet-20241022-v2:0 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| anthropic/claude-fable-5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| anthropic/claude-haiku-4-5-20251001 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| anthropic/claude-opus-4-6 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| anthropic/claude-opus-4-7 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| anthropic/claude-opus-4-8 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| anthropic/claude-sonnet-5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| cohere/command | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| cohere/command-a-plus-05-2026 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| cohere/command-a-vision-07-2025 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| cohere/command-light | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| cohere/command-r-03-2024 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| cohere/command-r-plus-04-2024 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| cohere/command-r7b-12-2024 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| deepseek/deepseek-v4-flash | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| deepseek/deepseek-v4-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/deepseek-v4-flash | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/deepseek-v4-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/glm-5.1 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/glm-5.1-fast | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/glm-5.2 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/glm-5.2-fast | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/kimi-k2.6 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/kimi-k2.6-fast | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/kimi-k2.7-code | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/kimi-k2.7-code-fast | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/llama-v3p3-70b-instruct | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/minimax-m2.7 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/minimax-m3 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/openai-gpt-oss-120b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/openai-gpt-oss-20b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/qwen-3.7-plus | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| fireworks/qwen2p5-vl-32b-instruct | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| fireworks/qwen2p5-vl-32b-instruct | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| google/gemini-2.5-flash | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| google/gemini-2.5-flash-lite | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| google/gemini-2.5-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| google/gemini-3.1-flash-lite | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| google/gemini-3.1-pro-preview | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['audio', 'image', 'text', 'video'] and output=['text'] |
| groq/llama-3.1-8b-instant | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| groq/llama-3.1-8b-instant | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| groq/llama-3.3-70b-versatile | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| groq/llama-3.3-70b-versatile | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| groq/openai/gpt-oss-120b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| groq/openai/gpt-oss-120b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| groq/openai/gpt-oss-20b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| groq/openai/gpt-oss-20b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| minimax/minimax-m2 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| minimax/minimax-m2 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| minimax/minimax-m2.1 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| minimax/minimax-m2.1 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status deprecated |
| minimax/minimax-m2.5 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| minimax/minimax-m2.7 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| minimax/minimax-m2.7 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| minimax/minimax-m3 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| minimax/minimax-m3 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/codestral-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/devstral-medium-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/devstral-small-latest | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| mistral/devstral-small-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/magistral-medium-latest | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| mistral/magistral-medium-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/mistral-large-latest | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| mistral/mistral-large-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/mistral-medium-latest | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| mistral/mistral-medium-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| mistral/mistral-small-latest | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['image', 'text'] and output=['text'] |
| mistral/mistral-small-latest | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| moonshot/kimi-k2.5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| moonshot/kimi-k2.6 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| moonshot/kimi-k2.7-code | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| openai/gpt-5.4 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| openai/gpt-5.5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| openai/gpt-5.5-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| perplexity/perplexity/sonar | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| perplexity/perplexity/sonar | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| perplexity/sonar-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| perplexity/sonar-reasoning-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/Qwen/Qwen2.5-7B-Instruct-Turbo | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/cogito-v2.1-671b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/cogito-v2.1-671b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/deepseek-v4-pro | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/deepseek-v4-pro | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/gemma-3n-e4b-instruct | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/gemma-3n-e4b-instruct | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/gemma-4-31b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/gemma-4-31b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/gemma-4-31b-it-pearl | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/gemma-4-31b-it-pearl | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/glm-5.1 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/glm-5.1 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/glm-5.2 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/glm-5.2 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/gpt-oss-120b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/gpt-oss-120b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/gpt-oss-20b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/gpt-oss-20b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/kimi-k2.6 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/kimi-k2.6 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/kimi-k2.7-code | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/kimi-k2.7-code | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/lfm2-24b-a2b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/lfm2-24b-a2b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/llama-3.3-70b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/llama-3.3-70b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/minimax-m2.5 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/minimax-m2.5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/minimax-m2.7 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/minimax-m2.7 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/minimax-m3 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/minimax-m3 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/nvidia-nemotron-3-ultra | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/nvidia-nemotron-3-ultra | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/qwen3-235b-a22b-fp8-throughput | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/qwen3-235b-a22b-fp8-throughput | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/qwen3.5-397b-a17b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/qwen3.5-397b-a17b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/qwen3.5-9b | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/qwen3.5-9b | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/qwen3.6-plus | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/qwen3.6-plus | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/qwen3.7-max | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/qwen3.7-max | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/qwen3.7-plus | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/qwen3.7-plus | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| together/rnj-1-instruct | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| together/rnj-1-instruct | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| xai/grok-4.20-0309-non-reasoning | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| xai/grok-4.20-0309-non-reasoning | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| xai/grok-4.20-0309-reasoning | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| xai/grok-4.20-0309-reasoning | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| xai/grok-4.20-multi-agent-0309 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| xai/grok-4.20-multi-agent-0309 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| xai/grok-4.3 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| xai/grok-4.3 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| xai/grok-build-0.1 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| xai/grok-build-0.1 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4-32b-0414-128k | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4-32b-0414-128k | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.5 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.5-air | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.5-air | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.5-airx | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.5-airx | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.5-x | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.5-x | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.6 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.6 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.7 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.7 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-4.7-flashx | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-4.7-flashx | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-5 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-5 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-5-turbo | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-5-turbo | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-5.1 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-5.1 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
| zhipu/glm-5.2 | modalities | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails input=['text'] and output=['text'] |
| zhipu/glm-5.2 | status | UNSUPPORTED | Real evidence gap: the stored quote does not explicitly entail this field/value. | no stored quote entails status ga |
