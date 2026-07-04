#!/usr/bin/env python3
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://factquire.com"
KEY_PATH = ROOT / "ops" / "indexnow-key.txt"
SITEMAP_PATH = ROOT / "site" / "sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"


def main():
    key = KEY_PATH.read_text(encoding="utf-8").strip()
    tree = ET.parse(SITEMAP_PATH)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text for node in tree.findall(".//sm:loc", ns) if node.text]
    payload = {
        "host": "factquire.com",
        "key": key,
        "keyLocation": f"{BASE_URL}/{key}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        print(f"IndexNow response: {response.status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
