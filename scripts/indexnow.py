#!/usr/bin/env python3
"""
IndexNow submission tool for factquire.com

Usage:
  py scripts/indexnow.py                      # submit all URLs from sitemap
  py scripts/indexnow.py --new                # submit only URLs not yet submitted
  py scripts/indexnow.py --provider groq      # submit all models for a provider
  py scripts/indexnow.py https://factquire.com/models/groq/llama-3_1-8b-instant.html
  py scripts/indexnow.py url1 url2 url3       # submit specific URLs
  py scripts/indexnow.py --dry-run            # show what would be submitted (no network)
  py scripts/indexnow.py --log                # show submission history
"""

import argparse
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://factquire.com"
KEY_PATH = ROOT / "ops" / "indexnow-key.txt"
SITEMAP_PATH = ROOT / "site" / "sitemap.xml"
LOG_PATH = ROOT / "ops" / "indexnow-log.jsonl"
ENDPOINT = "https://api.indexnow.org/indexnow"


def load_key() -> str:
    if not KEY_PATH.exists():
        sys.exit(f"Key file not found: {KEY_PATH}")
    return KEY_PATH.read_text(encoding="utf-8").strip()


def sitemap_urls() -> list[str]:
    if not SITEMAP_PATH.exists():
        sys.exit(f"Sitemap not found: {SITEMAP_PATH}\nRun: py scripts/build_site.py")
    tree = ET.parse(SITEMAP_PATH)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [node.text for node in tree.findall(".//sm:loc", ns) if node.text]


def provider_urls(provider: str) -> list[str]:
    all_urls = sitemap_urls()
    pattern = f"/models/{provider}/"
    matched = [u for u in all_urls if pattern in u]
    if not matched:
        sys.exit(f"No URLs found for provider '{provider}'\nAvailable: check site/models/ directory")
    return matched


def previously_submitted() -> set[str]:
    if not LOG_PATH.exists():
        return set()
    seen = set()
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            if entry.get("status") == 200:  # only real successful submissions count
                seen.update(entry.get("urls", []))
        except json.JSONDecodeError:
            pass
    return seen


def append_log(urls: list[str], status: int, dry_run: bool):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "count": len(urls),
        "status": status if not dry_run else "dry-run",
        "urls": urls,
    }
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def submit(urls: list[str], key: str, dry_run: bool) -> int:
    if not urls:
        print("Nothing to submit.")
        return 0

    print(f"{'[DRY RUN] ' if dry_run else ''}Submitting {len(urls)} URL(s) to IndexNow...")
    for u in urls[:5]:
        print(f"  {u}")
    if len(urls) > 5:
        print(f"  ... and {len(urls) - 5} more")

    if dry_run:
        print("Dry run complete. No network request made.")
        return 0

    payload = {
        "host": "factquire.com",
        "key": key,
        "keyLocation": f"{BASE_URL}/{key}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        status = resp.status
        print(f"IndexNow response: {status} OK" if status == 200 else f"IndexNow response: {status}")

    append_log(urls, status, dry_run=False)
    return 0 if status == 200 else 1


def show_log():
    if not LOG_PATH.exists():
        print("No submission history yet.")
        return
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            e = json.loads(line)
            ts = e.get("submitted_at", "?")[:19].replace("T", " ")
            cnt = e.get("count", "?")
            st = e.get("status", "?")
            print(f"{ts}  {cnt:>4} URLs  status={st}")
        except json.JSONDecodeError:
            pass


def main():
    parser = argparse.ArgumentParser(
        description="Submit URLs to IndexNow (Bing/Google/Yandex)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("urls", nargs="*", help="Specific URLs to submit")
    parser.add_argument("--new", action="store_true", help="Submit only URLs not yet submitted")
    parser.add_argument("--provider", metavar="NAME", help="Submit all model pages for a provider")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be submitted without sending")
    parser.add_argument("--log", action="store_true", help="Show submission history")
    args = parser.parse_args()

    if args.log:
        show_log()
        return

    key = load_key()

    if args.urls:
        urls = args.urls
    elif args.provider:
        urls = provider_urls(args.provider)
    elif args.new:
        all_urls = sitemap_urls()
        seen = previously_submitted()
        urls = [u for u in all_urls if u not in seen]
        if not urls:
            print(f"All {len(all_urls)} sitemap URLs already submitted. Nothing new.")
            return
        print(f"Found {len(urls)} new URL(s) (of {len(all_urls)} total)")
    else:
        urls = sitemap_urls()

    sys.exit(submit(urls, key, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
