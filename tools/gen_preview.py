#!/usr/bin/env python3
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
# Render the README via GitHub's own Markdown API → a GitHub-dark preview page.
import json, urllib.request, os
REPO = _ROOT + ""
md = open(REPO+"/README.md").read()
req = urllib.request.Request("https://api.github.com/markdown",
    data=json.dumps({"text": md, "mode": "markdown"}).encode(),
    headers={"Content-Type":"application/json","Accept":"application/vnd.github+json","User-Agent":"preview"})
html = urllib.request.urlopen(req, timeout=30).read().decode()
CSS = """
body{background:#0d1117;margin:0;padding:28px;display:flex;justify-content:center}
.markdown-body{color:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:16px;line-height:1.6;max-width:1012px;width:100%}
.markdown-body img{max-width:100%;vertical-align:middle}
.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4{border:0;font-weight:600;margin:22px 0 14px;color:#e6edf3}
.markdown-body a{color:#58a6ff;text-decoration:none}
.markdown-body code{background:#161b22;padding:.2em .4em;border-radius:6px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:85%}
.markdown-body pre{background:#161b22;padding:16px;border-radius:8px;overflow:auto;line-height:1.45}
.markdown-body pre code{background:0;padding:0;font-size:13.5px;color:#c9d1d9}
.markdown-body table{border-collapse:collapse;margin:16px 0;display:block;overflow:auto;width:max-content;max-width:100%}
.markdown-body th,.markdown-body td{border:1px solid #30363d;padding:7px 13px;text-align:left}
.markdown-body th{background:#161b22}
.markdown-body tr:nth-child(2n){background:#0d1117}
.markdown-body blockquote{border-left:3px solid #3fb950;color:#8b949e;padding:0 1em;margin:16px 0}
.markdown-body hr{display:none}
"""
out = f"<!doctype html><meta charset='utf-8'><style>{CSS}</style><article class='markdown-body'>{html}</article>"
open(REPO+"/preview.html","w").write(out)
print("wrote preview.html ·", len(html), "bytes of rendered HTML")
