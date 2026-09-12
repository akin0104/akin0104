from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
image = base64.b64encode((ROOT / "profile-avatar.png").read_bytes()).decode()


def banner(dark: bool) -> str:
    bg = "#0a101f" if dark else "#f8fafc"
    panel = "#111a2b" if dark else "#ffffff"
    inner = "#0e1728" if dark else "#eef2f7"
    text = "#f8fafc" if dark else "#0f172a"
    muted = "#94a3b8" if dark else "#64748b"
    chrome = "#22d3ee" if dark else "#0891b2"
    portrait = "#a78bfa" if dark else "#7c3aed"
    accent = "#10b981"
    border = "#24334a" if dark else "#dbe4ee"
    dot = "#203348" if dark else "#dbe7f0"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1180" height="610" viewBox="0 0 1180 610" role="img" aria-labelledby="title desc">
<title id="title">Bimbola Coker — business operations, data, and systems</title>
<desc id="desc">Terminal-style profile banner with a portrait map and system information.</desc>
<defs>
  <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{chrome}" stop-opacity=".22"/><stop offset="1" stop-color="{portrait}" stop-opacity=".06"/></linearGradient>
  <pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.15" fill="{dot}" opacity=".8"/><circle cx="11" cy="12" r=".8" fill="{dot}" opacity=".45"/></pattern>
  <clipPath id="portraitClip"><rect x="54" y="128" width="344" height="376" rx="18"/></clipPath>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000" flood-opacity=".18"/></filter>
</defs>
<rect width="1180" height="610" rx="28" fill="{bg}"/>
<rect x="24" y="24" width="1132" height="562" rx="22" fill="{panel}" stroke="{border}" filter="url(#shadow)"/>
<rect x="24" y="24" width="1132" height="562" rx="22" fill="url(#glow)" opacity=".8"/>
<path d="M24 84h1132" stroke="{border}"/><circle cx="54" cy="54" r="7" fill="#fb7185"/><circle cx="78" cy="54" r="7" fill="#fbbf24"/><circle cx="102" cy="54" r="7" fill="{accent}"/><text x="134" y="59" fill="{muted}" font-family="monospace" font-size="16">profile.sh --live</text><text x="1084" y="59" fill="{accent}" text-anchor="end" font-family="monospace" font-size="13">● LIVE</text>
<rect x="54" y="128" width="344" height="376" rx="18" fill="{inner}" stroke="{border}"/><rect x="54" y="128" width="344" height="376" rx="18" fill="url(#dots)"/>
<image x="76" y="150" width="300" height="332" preserveAspectRatio="xMidYMid slice" clip-path="url(#portraitClip)" opacity=".92" xlink:href="data:image/png;base64,{image}"/>
<rect x="76" y="150" width="300" height="332" rx="12" fill="none" stroke="{portrait}" stroke-opacity=".62" stroke-width="2"/><text x="78" y="526" fill="{portrait}" font-family="monospace" font-size="12" letter-spacing="2">VISUAL.MAP / ID_01</text>
<text x="458" y="136" fill="{chrome}" font-family="monospace" font-size="12" letter-spacing="2">SYSTEM.INFO</text><text x="458" y="180" fill="{muted}" font-family="monospace" font-size="14">NAME</text><text x="1082" y="180" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">BIMBOLA COKER</text><path d="M458 192h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="230" fill="{muted}" font-family="monospace" font-size="14">ROLE</text><text x="1082" y="230" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">BUSINESS SYSTEMS / DATA</text><path d="M458 242h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="280" fill="{muted}" font-family="monospace" font-size="14">FOCUS</text><text x="1082" y="280" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">WORKFLOWS · KPIs · PRODUCTS</text><path d="M458 292h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="330" fill="{muted}" font-family="monospace" font-size="14">STACK</text><text x="1082" y="330" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">SQL · TYPESCRIPT · REACT</text><path d="M458 342h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="380" fill="{muted}" font-family="monospace" font-size="14">STATUS</text><rect x="976" y="358" width="106" height="32" rx="16" fill="{accent}" fill-opacity=".18" stroke="{accent}" stroke-opacity=".45"/><circle cx="994" cy="374" r="5" fill="{accent}"/><text x="1008" y="379" fill="{accent}" font-family="monospace" font-size="12">BUILDING</text><path d="M458 402h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="444" fill="{chrome}" font-family="monospace" font-size="13">$ whoami</text><text x="458" y="476" fill="{text}" font-family="monospace" font-size="18">I make the work visible.</text><text x="458" y="510" fill="{muted}" font-family="monospace" font-size="13">business question → system → signal → decision</text>
</svg>'''

(ROOT / "dark.svg").write_text(banner(True), encoding="utf-8")
(ROOT / "light.svg").write_text(banner(False), encoding="utf-8")
print("generated dark.svg and light.svg")
