#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACCESSED_AT = "2026-07-04T05:55:32Z"
VERIFIED_AT = ACCESSED_AT

OPENAI_PRICING = "https://developers.openai.com/api/docs/pricing"
OPENAI_COMPARE = "https://developers.openai.com/api/docs/models/compare"
ANTHROPIC_PRICING = "https://platform.claude.com/docs/en/about-claude/pricing"
ANTHROPIC_MODELS = "https://platform.claude.com/docs/en/about-claude/models/overview"
ANTHROPIC_IDS = "https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions"
GEMINI_PRICING = "https://ai.google.dev/gemini-api/docs/pricing"
MISTRAL_PRICING = "https://mistral.ai/pricing/api/"
XAI_PRICING = "https://docs.x.ai/developers/pricing"
XAI_MODELS = "https://docs.x.ai/developers/models"
DEEPSEEK_PRICING = "https://api-docs.deepseek.com/quick_start/pricing"
DEEPSEEK_MODELS = "https://api-docs.deepseek.com/api/list-models"
COHERE_PRICING = "https://cohere.com/pricing"
COHERE_MODELS = "https://docs.cohere.com/docs/models"


def src(url, fields, quote):
    return {
        "url": url,
        "accessed_at": ACCESSED_AT,
        "fields": fields,
        "quote": quote,
    }


def entry(
    provider,
    model_id,
    display_name,
    status,
    pricing,
    modalities,
    sources,
    context=None,
    max_output=None,
    cutoff=None,
    notes=None,
):
    return {
        "provider": provider,
        "model_id": model_id,
        "display_name": display_name,
        "status": status,
        "release_date": None,
        "deprecation_date": None,
        "retirement_date": None,
        "pricing": {
            "input_per_mtok": pricing.get("input"),
            "output_per_mtok": pricing.get("output"),
            "cached_input_per_mtok": pricing.get("cached"),
            "batch_discount_pct": pricing.get("batch_discount_pct"),
        },
        "context_window_tokens": context,
        "max_output_tokens": max_output,
        "modalities": modalities,
        "knowledge_cutoff": cutoff,
        "sources": sources,
        "verified_at": VERIFIED_AT,
        "notes": notes,
    }


def pricing_fields(cached=True):
    fields = ["pricing.input_per_mtok", "pricing.output_per_mtok"]
    if cached:
        fields.append("pricing.cached_input_per_mtok")
    return fields


facts = []

# OpenAI: use standard short-context pricing where long-context tiers also exist.
openai_models = [
    ("gpt-5.5", "GPT-5.5", 5.00, 30.00, 0.50, 1050000, 128000, "Dec 01, 2025",
     "gpt-5.5$5.00$0.50$30.00$10.00$1.00$45.00",
     "GPT-5.5 ... Input $5.00 Cached Input $0.50 Output $30.00 Context Window 1,050,000 Max Output Tokens 128,000 Knowledge Cutoff Dec 01, 2025"),
    ("gpt-5.5-pro", "GPT-5.5 Pro", 30.00, 180.00, None, 1050000, 128000, "Dec 01, 2025",
     "gpt-5.5-pro$30.00-$180.00$60.00-$270.00",
     "GPT-5.5 Pro ... Input $30.00 Cached Input - Output $180.00 Context Window 1,050,000 Max Output Tokens 128,000 Knowledge Cutoff Dec 01, 2025"),
    ("gpt-5.4", "GPT-5.4", 2.50, 15.00, 0.25, 1050000, 128000, "Aug 31, 2025",
     "gpt-5.4$2.50$0.25$15.00$5.00$0.50$22.50",
     "GPT-5.4 ... Input $2.50 Cached Input $0.25 Output $15.00 Context Window 1,050,000 Max Output Tokens 128,000 Knowledge Cutoff Aug 31, 2025"),
]
for model_id, name, inp, out, cached, context, max_out, cutoff, price_quote, compare_quote in openai_models:
    fields = pricing_fields(cached is not None)
    facts.append(entry(
        "openai",
        model_id,
        name,
        "ga",
        {"input": inp, "output": out, "cached": cached},
        {"input": ["text", "image"], "output": ["text"]},
        [
            src(OPENAI_PRICING, fields, price_quote),
            src(OPENAI_COMPARE, ["context_window_tokens", "max_output_tokens", "knowledge_cutoff", "modalities"], compare_quote + " Supported Features Streaming Function calling Structured outputs Image input"),
        ],
        context,
        max_out,
        cutoff,
        "OpenAI pricing records the standard short-context tier; long-context pricing, where present, is noted in the cited quote.",
    ))

# Anthropic.
anthropic_price_quote = "Claude Fable 5$10 / MTok$12.50 / MTok$20 / MTok$1 / MTok$50 / MTok Claude Opus 4.8$5 / MTok$6.25 / MTok$10 / MTok$0.50 / MTok$25 / MTok Claude Opus 4.7$5 / MTok$6.25 / MTok$10 / MTok$0.50 / MTok$25 / MTok Claude Opus 4.6$5 / MTok$6.25 / MTok$10 / MTok$0.50 / MTok$25 / MTok Claude Sonnet 5 through August 31, 2026 $2 / MTok$2.50 / MTok$4 / MTok$0.20 / MTok$10 / MTok Claude Haiku 4.5$1 / MTok$1.25 / MTok$2 / MTok$0.10 / MTok$5 / MTok"
anthropic_modal_quote = "All current Claude models support text and image input, text output, multilingual capabilities, and vision."
anthropic_specs_quote = "Claude API ID claude-fable-5 claude-opus-4-8 claude-sonnet-5 claude-haiku-4-5-20251001 ... Context window 1M tokens 1M tokens 1M tokens 200k tokens Max output 128k tokens 128k tokens 128k tokens 64k tokens Reliable knowledge cutoff Jan 2026 Jan 2026 Jan 2026 Feb 2025"
anthropic_id_quote = "For example: `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-opus-4-6`, `claude-opus-4-7`, and `claude-opus-4-8`"
anthropic_long_quote = "Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, and Sonnet 4.6 include the full 1M token context window at standard pricing."
anthropic_entries = [
    ("claude-fable-5", "Claude Fable 5", 10, 50, 1, 1000000, 128000, "Jan 2026", "ga"),
    ("claude-opus-4-8", "Claude Opus 4.8", 5, 25, 0.50, 1000000, 128000, "Jan 2026", "ga"),
    ("claude-opus-4-7", "Claude Opus 4.7", 5, 25, 0.50, 1000000, None, None, "ga"),
    ("claude-opus-4-6", "Claude Opus 4.6", 5, 25, 0.50, 1000000, None, None, "ga"),
    ("claude-sonnet-5", "Claude Sonnet 5", 2, 10, 0.20, 1000000, 128000, "Jan 2026", "ga"),
    ("claude-haiku-4-5-20251001", "Claude Haiku 4.5", 1, 5, 0.10, 200000, 64000, "Feb 2025", "ga"),
]
for model_id, name, inp, out, cached, context, max_out, cutoff, status in anthropic_entries:
    sources = [
        src(ANTHROPIC_PRICING, pricing_fields(True), anthropic_price_quote),
        src(ANTHROPIC_MODELS, ["modalities"], anthropic_modal_quote),
    ]
    if model_id in {"claude-fable-5", "claude-opus-4-8", "claude-sonnet-5", "claude-haiku-4-5-20251001"}:
        fields = ["model_id", "context_window_tokens"]
        if max_out is not None:
            fields.append("max_output_tokens")
        if cutoff is not None:
            fields.append("knowledge_cutoff")
        sources.append(src(ANTHROPIC_MODELS, fields, anthropic_specs_quote))
    else:
        sources.append(src(ANTHROPIC_IDS, ["model_id"], anthropic_id_quote))
        sources.append(src(ANTHROPIC_PRICING, ["context_window_tokens"], anthropic_long_quote))
    facts.append(entry(
        "anthropic",
        model_id,
        name,
        status,
        {"input": inp, "output": out, "cached": cached},
        {"input": ["text", "image"], "output": ["text"]},
        sources,
        context,
        max_out,
        cutoff,
    ))

# Google Gemini API.
google_entries = [
    ("gemini-3.1-flash-lite", "Gemini 3.1 Flash-Lite", "ga", 0.25, 1.50, 0.025, {"input": ["text", "image", "video"], "output": ["text"]}, "Gemini 3.1 Flash-Lite `gemini-3.1-flash-lite` ... Input price Free of charge $0.25 (text / image / video) $0.50 (audio) Output price (including thinking tokens) Free of charge $1.50 Context caching price Not available $0.025 (text / image / video)"),
    ("gemini-3.1-pro-preview", "Gemini 3.1 Pro Preview", "preview", 2.00, 12.00, 0.20, {"input": ["text", "image", "video", "audio"], "output": ["text"]}, "Gemini 3.1 Pro Preview `gemini-3.1-pro-preview` ... Input price Not available $2.00, prompts <= 200k tokens $4.00, prompts > 200k tokens Output price (including thinking tokens) Not available $12.00, prompts <= 200k tokens $18.00, prompts > 200k Context caching price Not available $0.20, prompts <= 200k tokens"),
    ("gemini-3.1-flash-live-preview", "Gemini 3.1 Flash Live Preview", "preview", 0.75, 4.50, None, {"input": ["text"], "output": ["text"]}, "Gemini 3.1 Flash Live Preview `gemini-3.1-flash-live-preview` ... Input price Free of charge $0.75 (text) $3.00 or $0.005/min (audio) $1.00 or $0.002/min (image/video) Output price (including thinking tokens) Free of charge $4.50 (text) $12.00 or $0.018/min (audio)"),
    ("gemini-3-flash-preview", "Gemini 3 Flash Preview", "preview", 0.50, 3.00, 0.05, {"input": ["text", "image", "video"], "output": ["text"]}, "Gemini 3 Flash Preview `gemini-3-flash-preview` ... Input price Free of charge $0.50 (text / image / video) $1.00 (audio) Output price (including thinking tokens) Free of charge $3.00 Context caching price Free of charge $0.05 (text / image / video)"),
    ("gemini-2.5-pro", "Gemini 2.5 Pro", "ga", 1.25, 10.00, 0.125, {"input": ["text"], "output": ["text"]}, "Gemini 2.5 Pro `gemini-2.5-pro` ... Input price Free of charge $1.25, prompts <= 200k tokens $2.50, prompts > 200k tokens Output price (including thinking tokens) Free of charge $10.00, prompts <= 200k tokens $15.00, prompts > 200k Context caching price Not available $0.125, prompts <= 200k tokens"),
    ("gemini-2.5-flash", "Gemini 2.5 Flash", "ga", 0.30, 2.50, 0.03, {"input": ["text", "image", "video"], "output": ["text"]}, "Gemini 2.5 Flash `gemini-2.5-flash` Our first hybrid reasoning model which supports a 1M token context window ... Input price Free of charge $0.30 (text / image / video) $1.00 (audio) Output price (including thinking tokens) Free of charge $2.50 Context caching price Not available $0.03 (text / image / video)"),
    ("gemini-2.5-flash-lite", "Gemini 2.5 Flash-Lite", "ga", 0.10, 0.40, 0.01, {"input": ["text", "image", "video"], "output": ["text"]}, "Gemini 2.5 Flash-Lite `gemini-2.5-flash-lite` ... Input price (text, image, video) Free of charge $0.10 (text / image / video) $0.30 (audio) Output price (including thinking tokens) Free of charge $0.40 Context caching price Not available $0.01 (text / image / video)"),
    ("gemini-2.5-flash-lite-preview-09-2025", "Gemini 2.5 Flash-Lite Preview", "preview", 0.10, 0.40, 0.01, {"input": ["text", "image", "video"], "output": ["text"]}, "Gemini 2.5 Flash-Lite Preview `gemini-2.5-flash-lite-preview-09-2025` ... Input price (text, image, video) Free of charge $0.10 (text / image / video) $0.30 (audio) Output price (including thinking tokens) Free of charge $0.40 Context caching price Not available $0.01 (text / image / video)"),
    ("gemini-2.5-flash-native-audio-preview-12-2025", "Gemini 2.5 Flash Native Audio", "preview", 0.50, 2.00, None, {"input": ["text", "audio", "video"], "output": ["text", "audio"]}, "Gemini 2.5 Flash Native Audio (Live API) `gemini-2.5-flash-native-audio-preview-12-2025` ... Input price Free of charge $0.50 (text) $3.00 (audio / video) Output price (including thinking tokens) Free of charge $2.00 (text) $12.00 (audio)"),
    ("gemini-2.5-flash-preview-tts", "Gemini 2.5 Flash Preview TTS", "preview", 0.50, 10.00, None, {"input": ["text"], "output": ["audio"]}, "Gemini 2.5 Flash Preview TTS `gemini-2.5-flash-preview-tts` ... Input price Free of charge $0.50 (text) Output price Free of charge $10.00 (audio)"),
]
for model_id, name, status, inp, out, cached, modalities, quote in google_entries:
    context = 1000000 if model_id == "gemini-2.5-flash" else None
    fields = pricing_fields(cached is not None) + ["modalities"]
    if context is not None:
        fields.append("context_window_tokens")
    facts.append(entry(
        "google",
        model_id,
        name,
        status,
        {"input": inp, "output": out, "cached": cached},
        modalities,
        [src(GEMINI_PRICING, fields, quote)],
        context=context,
        notes="Gemini pricing may vary by modality and prompt length; this entry records the cited standard text or text/image/video tier.",
    ))

# Mistral.
mistral_entries = [
    ("mistral-medium-latest", "Mistral Medium 3.5", 1.5, 7.5, {"input": ["text", "image"], "output": ["text"]}, "Mistral Medium 3.5 ... Text-to-text Reasoning Coding Agentic Multimodal Input (/M tokens) $1.5 Output (/M tokens) $7.5 mistral-medium-latest"),
    ("mistral-small-latest", "Mistral Small 4", 0.15, 0.6, {"input": ["text", "image"], "output": ["text"]}, "Mistral Small 4 ... Text-to-text Agentic Multimodal Lightweight Input (/M tokens) $0.15 Output (/M tokens) $0.6 mistral-small-latest"),
    ("mistral-large-latest", "Mistral Large 3", 0.5, 1.5, {"input": ["text", "image"], "output": ["text"]}, "Mistral Large 3 ... Text-to-text Multimodal Input (/M tokens) $0.5 Output (/M tokens) $1.5 mistral-large-latest"),
    ("voxtral-small-latest", "Voxtral Small", 0.1, 0.4, {"input": ["text", "audio"], "output": ["text"]}, "Voxtral Small ... Audio Input (per min / per M tok) $0.004 Text Input (per min / per M tok) $0.1 Output (/M tokens) $0.4 Available on `/v1/chat/completions` voxtral-small-latest"),
    ("devstral-medium-latest", "Devstral 2", 0.4, 2.0, {"input": ["text"], "output": ["text"]}, "Devstral 2 ... Coding Agentic Text-to-text Input (/M tokens) $0.4 Output (/M tokens) $2 devstral-medium-latest"),
    ("devstral-small-latest", "Devstral Small 2", 0.1, 0.3, {"input": ["text", "image"], "output": ["text"]}, "Devstral Small 2 ... Coding Agentic Text-to-text Lightweight Multimodal Input (/M tokens) $0.1 Output (/M tokens) $0.3 devstral-small-latest"),
    ("codestral-latest", "Codestral", 0.3, 0.9, {"input": ["text"], "output": ["text"]}, "Codestral ... Coding Text-to-text Input (/M tokens) $0.3 Output (/M tokens) $0.9 codestral-latest"),
    ("magistral-medium-latest", "Magistral Medium", 2.0, 5.0, {"input": ["text", "image"], "output": ["text"]}, "Magistral Medium ... Text-to-text Reasoning Multimodal Input (/M tokens) $2 Output (/M tokens) $5 magistral-medium-latest"),
]
for model_id, name, inp, out, modalities, quote in mistral_entries:
    facts.append(entry(
        "mistral",
        model_id,
        name,
        "ga",
        {"input": inp, "output": out},
        modalities,
        [src(MISTRAL_PRICING, pricing_fields(False) + ["modalities"], quote)],
    ))

# xAI.
xai_price_quote = "Chat API Prices per 1M tokens Model Context Input Cached input Output grok-build-0.1 256k $1.00 $0.20 $2.00 grok-4.3 1M $1.25 $0.20 $2.50 grok-4.20-multi-agent-0309 1M $1.25 $0.20 $2.50 grok-4.20-0309-reasoning 1M $1.25 $0.20 $2.50 grok-4.20-0309-non-reasoning 1M $1.25 $0.20 $2.50"
xai_model_quote = "We have dedicated models and APIs for audio, image, and video capabilities. For everything else, use Grok 4.3."
xai_entries = [
    ("grok-build-0.1", "Grok Build 0.1", 1.00, 2.00, 0.20, 256000),
    ("grok-4.3", "Grok 4.3", 1.25, 2.50, 0.20, 1000000),
    ("grok-4.20-multi-agent-0309", "Grok 4.20 Multi-Agent 0309", 1.25, 2.50, 0.20, 1000000),
    ("grok-4.20-0309-reasoning", "Grok 4.20 0309 Reasoning", 1.25, 2.50, 0.20, 1000000),
    ("grok-4.20-0309-non-reasoning", "Grok 4.20 0309 Non-Reasoning", 1.25, 2.50, 0.20, 1000000),
]
for model_id, name, inp, out, cached, context in xai_entries:
    facts.append(entry(
        "xai",
        model_id,
        name,
        "ga",
        {"input": inp, "output": out, "cached": cached},
        {"input": ["text"], "output": ["text"]},
        [
            src(XAI_PRICING, pricing_fields(True) + ["context_window_tokens"], xai_price_quote),
            src(XAI_MODELS, ["modalities"], xai_model_quote),
        ],
        context=context,
    ))

# DeepSeek.
deepseek_entries = [
    ("deepseek-v4-flash", "DeepSeek V4 Flash", 0.14, 0.28, 0.0028),
    ("deepseek-v4-pro", "DeepSeek V4 Pro", 0.435, 0.87, 0.003625),
]
for model_id, name, inp, out, cached in deepseek_entries:
    facts.append(entry(
        "deepseek",
        model_id,
        name,
        "ga",
        {"input": inp, "output": out, "cached": cached},
        {"input": ["text"], "output": ["text"]},
        [
            src(DEEPSEEK_PRICING, pricing_fields(True) + ["context_window_tokens", "max_output_tokens", "modalities"], "MODEL deepseek-v4-flash(1)deepseek-v4-pro ... CONTEXT LENGTH 1M MAX OUTPUT MAXIMUM: 384K ... 1M INPUT TOKENS (CACHE HIT)$0.0028$0.003625 1M INPUT TOKENS (CACHE MISS)$0.14$0.435 1M OUTPUT TOKENS$0.28$0.87"),
            src(DEEPSEEK_MODELS, ["model_id"], '"id": "deepseek-v4-flash" ... "id": "deepseek-v4-pro"'),
        ],
        context=1000000,
        max_output=384000,
    ))

# Cohere.
cohere_entries = [
    ("command-r-plus-08-2024", "Command R+ 08-2024", "ga", 2.50, 10.00, 128000, 4000, "Command R+ 08-2024 pricing is $2.50/1M tokens for input and $10.00/1M tokens for output", "`command-r-plus-08-2024 `Live `command-r-plus-08-2024` is an update of the Command R+ model, delivered in August 2024. Text 128k 4k"),
    ("command-r-03-2024", "Command R 03-2024", "deprecated", 0.50, 1.50, 128000, 4000, "Command R 03-2024 pricing is $0.50/1M tokens for input and $1.50/1M tokens for output", "`command-r-03-2024 `Deprecated Sept 15, 2025 Command R is an instruction-following conversational model ... Text 128k 4k"),
    ("command-r-plus-04-2024", "Command R+ 04-2024", "deprecated", 3.00, 15.00, 128000, 4000, "Command R+ 04-2024 pricing is $3.00/1M tokens for input and $15.00/1M tokens for output", "`command-r-plus-04-2024 `Deprecated Sept 15, 2025 Command R+ is an instruction-following conversational model ... Text 128k 4k"),
    ("command", "Command", "deprecated", 1.00, 2.00, 4000, 4000, "Command pricing is $1.00/1M tokens for input and $2.00/1M tokens for output", "`command `Deprecated Sept 15, 2025 An instruction-following conversational model ... Text 4k 4k"),
    ("command-light", "Command Light", "deprecated", 0.30, 0.60, 4000, 4000, "Command-light pricing is $0.30/1M tokens for input and $0.60/1M tokens for output", "`command-light `Deprecated Sept 15, 2025 A smaller, faster version of `command`. Almost as capable, but a lot faster.Text 4k 4k"),
    ("c4ai-aya-expanse-32b", "Aya Expanse 32B", "ga", 0.50, 1.50, 128000, 4000, "Aya Expanse models (8B and 32B) on the API are charged at $0.50/1M tokens for input and $1.50/1M tokens for output.", "`c4ai-aya-expanse-32b `Live Aya Expanse is a highly performant 32B multilingual model ... Text 128k 4k"),
]
for model_id, name, status, inp, out, context, max_out, price_quote, model_quote in cohere_entries:
    facts.append(entry(
        "cohere",
        model_id,
        name,
        status,
        {"input": inp, "output": out},
        {"input": ["text"], "output": ["text"]},
        [
            src(COHERE_PRICING, pricing_fields(False), price_quote),
            src(COHERE_MODELS, ["model_id", "status", "modalities", "context_window_tokens", "max_output_tokens"], model_quote),
        ],
        context=context,
        max_output=max_out,
    ))

assert len(facts) == 40, len(facts)

data_dir = ROOT / "data"
data_dir.mkdir(exist_ok=True)
(data_dir / "facts.json").write_text(json.dumps(facts, indent=2) + "\n", encoding="utf-8")

gap_fields = [
    "release_date",
    "deprecation_date",
    "retirement_date",
    "pricing.cached_input_per_mtok",
    "pricing.batch_discount_pct",
    "context_window_tokens",
    "max_output_tokens",
    "knowledge_cutoff",
]
lines = [
    "# ModelWire Gaps",
    "",
    "Null fields below were left unset because the collected primary source snippets did not confirm a value in the required form.",
    "",
]
for item in facts:
    pricing = item["pricing"]
    values = {
        "release_date": item["release_date"],
        "deprecation_date": item["deprecation_date"],
        "retirement_date": item["retirement_date"],
        "pricing.cached_input_per_mtok": pricing["cached_input_per_mtok"],
        "pricing.batch_discount_pct": pricing["batch_discount_pct"],
        "context_window_tokens": item["context_window_tokens"],
        "max_output_tokens": item["max_output_tokens"],
        "knowledge_cutoff": item["knowledge_cutoff"],
    }
    for field in gap_fields:
        if values[field] is None:
            looked = ", ".join(sorted({source["url"] for source in item["sources"]}))
            lines.append(f"- {item['provider']}/{item['model_id']}: `{field}` - not confirmed in collected primary source pages. Looked: {looked}")
(ROOT / "gaps.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
