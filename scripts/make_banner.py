from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def icon_scenes(stroke: str, accent: str, muted: str) -> str:
    # SMIL opacity transitions intentionally keep the same terminal frame while the visual map cycles.
    timeline = '0;0.08;0.22;0.30;0.44;0.52;0.66;0.74;0.88;0.96;1'
    key = '0;1;1;0;0;1;1;0;0;1;1'
    return f'''<g transform="translate(78 154)">
      <g opacity="0"><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="{key}" keyTimes="{timeline}"/>
        <path d="M88 112 48 164l40 52M212 112l40 52-40 52" fill="none" stroke="{stroke}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="m142 92-42 144" stroke="{accent}" stroke-width="10" stroke-linecap="round"/>
        <circle cx="150" cy="64" r="7" fill="{accent}"/><text x="150" y="302" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="15" letter-spacing="3">MARKUP / 01</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0;0;0;0" keyTimes="{timeline}"/>
        <path d="M116 82 72 118l44 36M184 82l44 36-44 36" fill="none" stroke="{stroke}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M146 68 124 170" stroke="{accent}" stroke-width="10" stroke-linecap="round"/>
        <path d="M82 218h160" stroke="{muted}" stroke-width="2" stroke-dasharray="3 10"/><text x="162" y="302" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="15" letter-spacing="3">TYPESCRIPT / 02</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;0;0;1;1;0;0;0;0;0" keyTimes="{timeline}"/>
        <ellipse cx="150" cy="92" rx="76" ry="22" fill="none" stroke="{stroke}" stroke-width="10"/><path d="M74 92v95c0 18 34 33 76 33s76-15 76-33V92M74 140c0 18 34 33 76 33s76-15 76-33" fill="none" stroke="{stroke}" stroke-width="10"/><circle cx="102" cy="245" r="7" fill="{accent}"/><circle cx="130" cy="245" r="7" fill="{accent}" opacity=".7"/><circle cx="158" cy="245" r="7" fill="{accent}" opacity=".45"/><text x="150" y="302" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="15" letter-spacing="3">SQL / 03</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;0;0;0;0;1;1;0;0;0" keyTimes="{timeline}"/>
        <path d="M68 206V130M68 206h184" stroke="{muted}" stroke-width="7" stroke-linecap="round"/><path d="m82 182 42-44 37 22 62-72" fill="none" stroke="{stroke}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="182" r="8" fill="{accent}"/><circle cx="124" cy="138" r="8" fill="{accent}"/><circle cx="161" cy="160" r="8" fill="{accent}"/><circle cx="223" cy="88" r="8" fill="{accent}"/><text x="150" y="302" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="15" letter-spacing="3">SIGNAL / 04</text>
      </g>
      <g opacity="0"><animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;0;0;0;0;0;0;1;1;0" keyTimes="{timeline}"/>
        <circle cx="150" cy="148" r="72" fill="none" stroke="{stroke}" stroke-width="10" stroke-dasharray="12 13"/><circle cx="150" cy="148" r="38" fill="none" stroke="{accent}" stroke-width="10"/><path d="M150 80v68l44 27" stroke="{accent}" stroke-width="10" stroke-linecap="round"/><text x="150" y="302" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="15" letter-spacing="3">SYSTEM / 05</text>
      </g>
    </g>'''


def banner(dark: bool) -> str:
    bg = "#0a101f" if dark else "#f8fafc"
    panel = "#111a2b" if dark else "#ffffff"
    inner = "#0e1728" if dark else "#eef2f7"
    text = "#f8fafc" if dark else "#0f172a"
    muted = "#94a3b8" if dark else "#64748b"
    chrome = "#22d3ee" if dark else "#0891b2"
    icon = "#a78bfa" if dark else "#7c3aed"
    accent = "#10b981"
    border = "#24334a" if dark else "#dbe4ee"
    dot = "#203348" if dark else "#dbe7f0"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610" role="img" aria-labelledby="title desc">
<title id="title">Bimbola Coker — business operations, data, and systems</title>
<desc id="desc">Animated terminal-style profile banner cycling through markup, TypeScript, SQL, signal, and system icons.</desc>
<defs>
  <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{chrome}" stop-opacity=".22"/><stop offset="1" stop-color="{icon}" stop-opacity=".06"/></linearGradient>
  <pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.15" fill="{dot}" opacity=".8"/><circle cx="11" cy="12" r=".8" fill="{dot}" opacity=".45"/></pattern>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000" flood-opacity=".18"/></filter>
</defs>
<rect width="1180" height="610" rx="28" fill="{bg}"/><rect x="24" y="24" width="1132" height="562" rx="22" fill="{panel}" stroke="{border}" filter="url(#shadow)"/><rect x="24" y="24" width="1132" height="562" rx="22" fill="url(#glow)" opacity=".8"/>
<path d="M24 84h1132" stroke="{border}"/><circle cx="54" cy="54" r="7" fill="#fb7185"/><circle cx="78" cy="54" r="7" fill="#fbbf24"/><circle cx="102" cy="54" r="7" fill="{accent}"/><text x="134" y="59" fill="{muted}" font-family="monospace" font-size="16">profile.sh --live</text><text x="1084" y="59" fill="{accent}" text-anchor="end" font-family="monospace" font-size="13">● LIVE</text>
<rect x="54" y="128" width="344" height="376" rx="18" fill="{inner}" stroke="{border}"/><rect x="54" y="128" width="344" height="376" rx="18" fill="url(#dots)"/><rect x="76" y="150" width="300" height="332" rx="12" fill="none" stroke="{icon}" stroke-opacity=".62" stroke-width="2"/>{icon_scenes(icon, accent, muted)}<text x="78" y="526" fill="{icon}" font-family="monospace" font-size="12" letter-spacing="2">CODE.MAP / LIVE_MORPH</text>
<text x="458" y="136" fill="{chrome}" font-family="monospace" font-size="12" letter-spacing="2">SYSTEM.INFO</text><text x="458" y="180" fill="{muted}" font-family="monospace" font-size="14">NAME</text><text x="1082" y="180" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">BIMBOLA COKER</text><path d="M458 192h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="230" fill="{muted}" font-family="monospace" font-size="14">ROLE</text><text x="1082" y="230" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">BUSINESS SYSTEMS / DATA</text><path d="M458 242h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="280" fill="{muted}" font-family="monospace" font-size="14">FOCUS</text><text x="1082" y="280" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">WORKFLOWS · KPIs · PRODUCTS</text><path d="M458 292h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="330" fill="{muted}" font-family="monospace" font-size="14">STACK</text><text x="1082" y="330" fill="{text}" text-anchor="end" font-family="monospace" font-size="14">SQL · TYPESCRIPT · REACT</text><path d="M458 342h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="380" fill="{muted}" font-family="monospace" font-size="14">STATUS</text><rect x="976" y="358" width="106" height="32" rx="16" fill="{accent}" fill-opacity=".18" stroke="{accent}" stroke-opacity=".45"/><circle cx="994" cy="374" r="5" fill="{accent}"/><text x="1008" y="379" fill="{accent}" font-family="monospace" font-size="12">BUILDING</text><path d="M458 402h624" stroke="{border}" stroke-dasharray="2 8"/>
<text x="458" y="444" fill="{chrome}" font-family="monospace" font-size="13">$ whoami</text><text x="458" y="476" fill="{text}" font-family="monospace" font-size="18">I make the work visible.</text><text x="458" y="510" fill="{muted}" font-family="monospace" font-size="13">business question → system → signal → decision</text>
</svg>'''

(ROOT / "dark.svg").write_text(banner(True), encoding="utf-8")
(ROOT / "light.svg").write_text(banner(False), encoding="utf-8")
print("generated animated dark.svg and light.svg")
