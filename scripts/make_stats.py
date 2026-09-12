from pathlib import Path
import json
import re
import subprocess
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OWNER = "akin0104"

def api(path):
    out = subprocess.check_output(["gh", "api", path], text=True)
    out = re.sub(r"\x1b\[[0-9;]*m", "", out)
    start = min([i for i in (out.find("["), out.find("{")) if i >= 0])
    return json.loads(out[start:])

repos = api("user/repos?per_page=100&affiliation=owner&sort=updated")
repos = [r for r in repos if not r.get("fork")]

stars = sum(r.get("stargazers_count", 0) for r in repos)
issues = sum(r.get("open_issues_count", 0) for r in repos)
commits = api("search/commits?q=author%3Aakin0104").get("total_count", 0)
pull_requests = api("search/issues?q=author%3Aakin0104%20is%3Apr").get("total_count", 0)
bytes_by_language = Counter()
for repo in repos:
    try:
        languages = api(f"repos/{OWNER}/{repo['name']}/languages")
        bytes_by_language.update(languages)
    except subprocess.CalledProcessError:
        pass

language_items = bytes_by_language.most_common(6)
total_bytes = sum(bytes_by_language.values()) or 1
language_colors = {
    "TypeScript": "#22d3ee", "JavaScript": "#facc15", "Python": "#60a5fa",
    "HTML": "#f97316", "CSS": "#a78bfa", "Shell": "#10b981", "SQL": "#fb7185",
}

def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def svg(dark=True):
    bg = "#0b1019" if dark else "#ffffff"
    panel = "#0d121b" if dark else "#ffffff"
    ink = "#f8fafc" if dark else "#0f172a"
    muted = "#94a3b8" if dark else "#64748b"
    cyan = "#22d3ee" if dark else "#0e7490"
    purple = "#a78bfa" if dark else "#7c3aed"
    line = "#26364b" if dark else "#dbe4ee"
    width, height = 1180, 410
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">GitHub stats and most used languages for {OWNER}</title><desc id="desc">Repository statistics and a horizontal language distribution chart.</desc><defs><filter id="shadow"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000" flood-opacity=".2"/></filter></defs><rect width="{width}" height="{height}" rx="14" fill="{bg}"/><rect x="24" y="24" width="530" height="362" rx="13" fill="{panel}" stroke="{line}" filter="url(#shadow)"/><rect x="578" y="24" width="578" height="362" rx="13" fill="{panel}" stroke="{line}" filter="url(#shadow)"/><text x="54" y="72" fill="{cyan}" font-family="monospace" font-size="24" font-weight="bold">GitHub Stats</text><text x="608" y="72" fill="{cyan}" font-family="monospace" font-size="24" font-weight="bold">Top Languages by Code</text>''']
    stats = [("Total stars earned", stars), ("Total commits", commits), ("Total pull requests", pull_requests), ("Total issues", issues), ("Contributed to (featured)", 5)]
    for i, (label, value) in enumerate(stats):
        y = 116 + i * 43
        symbol = ["☆", "◌", "⑂", "!", "▣"][i]
        parts.append(f'<text x="56" y="{y}" fill="{purple}" font-family="monospace" font-size="20">{symbol}</text><text x="88" y="{y}" fill="{muted}" font-family="monospace" font-size="16">{esc(label)}</text><text x="480" y="{y}" fill="{ink}" text-anchor="end" font-family="monospace" font-size="18" font-weight="bold">{value}</text>')
    parts.append(f'<path d="M54 334h470" stroke="{line}"/><text x="56" y="365" fill="{muted}" font-family="monospace" font-size="12">public portfolio snapshot · {len(repos)} repositories tracked</text>')
    x, y, total_w = 608, 112, 500
    cur = x
    for lang, amount in language_items:
        w = max(4, total_w * amount / total_bytes)
        color = language_colors.get(lang, "#64748b")
        parts.append(f'<rect x="{cur:.1f}" y="{y}" width="{w:.1f}" height="18" fill="{color}"/>')
        cur += w
    parts.append(f'<rect x="{x}" y="{y}" width="{total_w}" height="18" fill="none" stroke="{line}"/><text x="608" y="166" fill="{muted}" font-family="monospace" font-size="12">distribution by reported language bytes</text>')
    for i, (lang, amount) in enumerate(language_items):
        col = i % 2; row = i // 2
        lx, ly = 608 + col * 260, 216 + row * 48
        pct = amount / total_bytes * 100
        color = language_colors.get(lang, "#64748b")
        parts.append(f'<circle cx="{lx}" cy="{ly-5}" r="6" fill="{color}"/><text x="{lx+16}" y="{ly}" fill="{muted}" font-family="monospace" font-size="14">{esc(lang)}</text><text x="{lx+240}" y="{ly}" fill="{ink}" text-anchor="end" font-family="monospace" font-size="14">{pct:.1f}%</text>')
    parts.append('</svg>')
    return ''.join(parts)

(ROOT / "stats-dark.svg").write_text(svg(True), encoding="utf-8")
(ROOT / "stats-light.svg").write_text(svg(False), encoding="utf-8")
print(json.dumps({"repositories": len(repos), "stars": stars, "issues": issues, "languages": language_items}))
