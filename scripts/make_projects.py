from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

projects = [
    ("insighthub", "InsightHub", "Client-operations decision intelligence", "Analytics", ["SQL", "React", "KPI"], "I", "#22d3ee", "Data product"),
    ("opsflow", "OpsFlow", "Business process and CRM automation", "Systems", ["TS", "Workflows", "tRPC"], "O", "#10b981", "Automation"),
    ("aligniq", "AlignIQ", "Explainable workforce alignment", "Evidence", ["Scoring", "Taxonomy", "UX"], "A", "#a78bfa", "Data product"),
    ("trustdesk", "TrustDesk", "Citation-grounded knowledge assistant", "AI app", ["Retrieval", "Citations", "Tests"], "T", "#f59e0b", "Responsible AI"),
    ("growthlab", "GrowthLab", "Digital strategy and conversion intelligence", "Growth", ["Events", "Funnels", "Experiments"], "G", "#22d3ee", "Analytics"),
    ("operating-principles", "Operating principles", "Business question → system → signal → decision", "Method", ["Clarity", "Traceability", "Delivery"], "→", "#10b981", "Working style"),
]

W, H = 1180, 790
bg, panel, card, line, ink, muted = "#0a101f", "#0d1526", "#0e1728", "#243752", "#f8fafc", "#94a3b8"
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">Bimbola Coker featured projects</title>
<desc id="desc">Dark two-column project board for InsightHub, OpsFlow, AlignIQ, TrustDesk, GrowthLab, and operating principles.</desc>
<defs><filter id="shadow"><feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity=".22"/></filter><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#10233b"/><stop offset="1" stop-color="#0a101f"/></linearGradient></defs>
<rect width="{W}" height="{H}" rx="16" fill="{bg}"/><rect x="22" y="22" width="{W-44}" height="{H-44}" rx="12" fill="url(#wash)" stroke="#1b2d47"/>
<text x="48" y="62" fill="#22d3ee" font-family="monospace" font-size="14" letter-spacing="3">PROJECTS.LIST</text><text x="232" y="62" fill="#526a84" font-family="monospace" font-size="13">/projects.sh --all</text><circle cx="1102" cy="57" r="5" fill="#10b981"/><text x="1088" y="84" fill="#526a84" text-anchor="end" font-family="monospace" font-size="11">6 SYSTEMS · 100% SHIPPED</text>''']

for idx, (slug, name, desc, category, chips, mark, accent, kind) in enumerate(projects):
    col, row = idx % 2, idx // 2
    x, y = 48 + col * 542, 112 + row * 212
    parts.append(f'''<g filter="url(#shadow)"><rect x="{x}" y="{y}" width="510" height="182" rx="14" fill="{card}" stroke="{line}"/><path d="M{x} {y+42}h510" stroke="{line}"/><circle cx="{x+20}" cy="{y+21}" r="3" fill="#22d3ee"/><text x="{x+32}" y="{y+26}" fill="#c0cfdf" font-family="monospace" font-size="12">akin0104/{slug}</text><circle cx="{x+484}" cy="{y+21}" r="4" fill="{accent}" opacity=".85"/>
<rect x="{x+18}" y="{y+61}" width="48" height="48" rx="11" fill="{accent}" fill-opacity=".16" stroke="{accent}" stroke-opacity=".7"/><text x="{x+42}" y="{y+94}" fill="{accent}" text-anchor="middle" font-family="monospace" font-size="25" font-weight="bold">{mark}</text><text x="{x+82}" y="{y+80}" fill="{ink}" font-family="monospace" font-size="17" font-weight="bold">{name}</text><text x="{x+82}" y="{y+103}" fill="{muted}" font-family="monospace" font-size="11">{desc}</text>
<text x="{x+82}" y="{y+129}" fill="{accent}" font-family="monospace" font-size="10">{category.upper()}</text>
<circle cx="{x+445}" cy="{y+85}" r="30" fill="none" stroke="#22344d" stroke-width="8"/><circle cx="{x+445}" cy="{y+85}" r="30" fill="none" stroke="{accent}" stroke-width="8" stroke-linecap="round" stroke-dasharray="188" transform="rotate(-90 {x+445} {y+85})"/><text x="{x+445}" y="{y+90}" fill="{ink}" text-anchor="middle" font-family="monospace" font-size="12" font-weight="bold">100%</text><text x="{x+445}" y="{y+108}" fill="#617890" text-anchor="middle" font-family="monospace" font-size="8">SHIPPED</text>
{''.join(f'<rect x="{x+18+i*92}" y="{y+144}" width="82" height="22" rx="11" fill="{accent}" fill-opacity=".14" stroke="{accent}" stroke-opacity=".4"/><text x="{x+59+i*92}" y="{y+159}" fill="{accent}" text-anchor="middle" font-family="monospace" font-size="9">{chip}</text>' for i, chip in enumerate(chips))}<text x="{x+430}" y="{y+160}" fill="#617890" text-anchor="end" font-family="monospace" font-size="9">{kind}</text></g>''')

parts.append('</svg>')
(ROOT / "projects.svg").write_text("".join(parts), encoding="utf-8")
print("generated projects.svg")
