#!/usr/bin/env python3
import hashlib
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTERNAL_DIR = ROOT / "data" / "external"

DOWNLOADS = {
    "litellm": {
        "url": "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json",
        "filename": "litellm.json",
    },
    "modelsdev": {
        "url": "https://models.dev/api.json",
        "filename": "modelsdev.json",
    },
}


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "ModelWire external audit"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main():
    EXTERNAL_DIR.mkdir(parents=True, exist_ok=True)
    accessed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    meta = {"accessed_at": accessed_at, "urls": {}, "sha256": {}}

    for name, config in DOWNLOADS.items():
        data = fetch(config["url"])
        json.loads(data.decode("utf-8"))
        path = EXTERNAL_DIR / config["filename"]
        path.write_bytes(data)
        meta["urls"][name] = config["url"]
        meta["sha256"][config["filename"]] = hashlib.sha256(data).hexdigest()
        print(f"Wrote {path.relative_to(ROOT)}")

    meta_path = EXTERNAL_DIR / "meta.json"
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {meta_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
