#!/usr/bin/env python3
"""Restore image assets into the build output.

The site's images (logo + client logos) were removed from git in the
"Remove site/ from git" commit. They still exist in git history at commit
42cd5fc, so we fetch them from there at build time and write them into
site/img/ so the deployed pages can reference them.
"""
import os
import urllib.request

BASE = "https://raw.githubusercontent.com/Stevenfree1/expansionvideos-site/42cd5fc/site/img/"
SITE_IMG = os.path.join(os.path.dirname(__file__), "site", "img")

FILES = [
    "logo.png",
    "clients/aigo.png",
    "clients/deloitte.png",
    "clients/metaforce.png",
    "clients/ridian.jpg",
    "clients/toyota.png",
    "clients/veritas.png",
]

ok = 0
for rel in FILES:
    url = BASE + rel
    dest = os.path.join(SITE_IMG, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "pages-build"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(dest, "wb") as f:
            f.write(data)
        ok += 1
        print(f"OK  img/{rel} ({len(data):,} bytes)")
    except Exception as e:
        print(f"ERR img/{rel}: {e}")

print(f"Image restore complete: {ok}/{len(FILES)} files")
