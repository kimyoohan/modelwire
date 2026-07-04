#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FACTS_PATH = ROOT / "data" / "facts.json"
CHANGELOG_PATH = ROOT / "data" / "changelog.json"
AUDIT_PATH = ROOT / "data" / "audit.json"
SITE_DIR = ROOT / "site"
FEED_PATH = SITE_DIR / "feed.json"
SITE_CHANGELOG_PATH = SITE_DIR / "changelog.json"
SITE_AUDIT_PATH = SITE_DIR / "audit.json"
INDEX_PATH = SITE_DIR / "index.html"
CHANGELOG_HTML_PATH = SITE_DIR / "changelog.html"
AUDIT_HTML_PATH = SITE_DIR / "audit.html"


def main():
    facts = json.loads(FACTS_PATH.read_text(encoding="utf-8"))
    changelog = json.loads(CHANGELOG_PATH.read_text(encoding="utf-8"))
    latest_version = changelog.get("releases", [{}])[0].get("version", "0.1")
    feed = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "count": len(facts),
        "version": latest_version,
        "models": facts,
    }
    SITE_DIR.mkdir(exist_ok=True)
    FEED_PATH.write_text(json.dumps(feed, indent=2) + "\n", encoding="utf-8")
    SITE_CHANGELOG_PATH.write_text(CHANGELOG_PATH.read_text(encoding="utf-8"), encoding="utf-8")
    if AUDIT_PATH.exists():
        SITE_AUDIT_PATH.write_text(AUDIT_PATH.read_text(encoding="utf-8"), encoding="utf-8")

    if INDEX_PATH.exists():
        html = INDEX_PATH.read_text(encoding="utf-8")
        start = "<script id=\"modelwire-feed\" type=\"application/json\">"
        end = "</script>"
        start_index = html.find(start)
        if start_index != -1:
            content_start = start_index + len(start)
            end_index = html.find(end, content_start)
            if end_index != -1:
                replacement = json.dumps(feed, separators=(",", ":"))
                html = html[:content_start] + replacement + html[end_index:]
                INDEX_PATH.write_text(html, encoding="utf-8")

    if CHANGELOG_HTML_PATH.exists():
        html = CHANGELOG_HTML_PATH.read_text(encoding="utf-8")
        start = "<script id=\"modelwire-changelog\" type=\"application/json\">"
        end = "</script>"
        start_index = html.find(start)
        if start_index != -1:
            content_start = start_index + len(start)
            end_index = html.find(end, content_start)
            if end_index != -1:
                replacement = json.dumps(changelog, separators=(",", ":"))
                html = html[:content_start] + replacement + html[end_index:]
                CHANGELOG_HTML_PATH.write_text(html, encoding="utf-8")

    if AUDIT_HTML_PATH.exists() and AUDIT_PATH.exists():
        html = AUDIT_HTML_PATH.read_text(encoding="utf-8")
        start = "<script id=\"modelwire-audit\" type=\"application/json\">"
        end = "</script>"
        start_index = html.find(start)
        if start_index != -1:
            content_start = start_index + len(start)
            end_index = html.find(end, content_start)
            if end_index != -1:
                audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
                replacement = json.dumps(audit, separators=(",", ":"))
                html = html[:content_start] + replacement + html[end_index:]
                AUDIT_HTML_PATH.write_text(html, encoding="utf-8")

    print(f"Wrote {FEED_PATH.relative_to(ROOT)} with {len(facts)} models")
    print(f"Wrote {SITE_CHANGELOG_PATH.relative_to(ROOT)}")
    if AUDIT_PATH.exists():
        print(f"Wrote {SITE_AUDIT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
