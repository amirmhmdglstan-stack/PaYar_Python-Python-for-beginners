#!/usr/bin/env python3
"""
1-Command GitHub Uploader for PaYar_Python-Python-for-beginners
Uploads all project files and triggers the GitHub Actions APK Release workflow.
"""
import base64
import json
import os
import urllib.request

REPO = "amirmhmdglstan-stack/PaYar_Python-Python-for-beginners"
# Security fix: never hardcode tokens in source files (they get leaked in public
# repos and auto-revoked by GitHub secret scanning). Read from the environment:
TOKEN = os.environ.get("GITHUB_TOKEN", "")

FILES_TO_PUSH = [
    "README.md",
    ".github/workflows/build-apk.yml",
    "settings.gradle",
    "build.gradle",
    "gradle.properties",
    "app/build.gradle",
    "app/src/main/AndroidManifest.xml",
    "app/src/main/java/com/payar/python/MainActivity.java",
    "app/src/main/res/drawable/ic_launcher.xml",
    "app/src/main/assets/www/index.html",
    "www/index.html",
]

def api_req(method, path, payload=None):
    url = f"https://api.github.com/repos/{REPO}{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "PaYar-Uploader"
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    print(f"Connecting to {REPO}...")
    repo_info = api_req("GET", "")
    branch = repo_info.get("default_branch", "main")
    for rel_path in FILES_TO_PUSH:
        if not os.path.exists(rel_path):
            continue
        with open(rel_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        sha = None
        try:
            existing = api_req("GET", f"/contents/{rel_path}?ref={branch}")
            sha = existing.get("sha")
        except Exception:
            pass
        body = {
            "message": f"Add/update {rel_path} for PaYar v1.0.0 APK Release",
            "content": b64,
            "branch": branch,
        }
        if sha:
            body["sha"] = sha
        print(f"Uploading {rel_path}...")
        api_req("PUT", f"/contents/{rel_path}", body)
    print("All files pushed! GitHub Actions is now building your Release APK.")

if __name__ == "__main__":
    main()
