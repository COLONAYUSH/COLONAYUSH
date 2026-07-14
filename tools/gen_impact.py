#!/usr/bin/env python3
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
# impact.svg — bespoke, self-contained metrics readout (real numbers, no 3rd-party
# dependency that can 404). Replaces flaky github-readme-stats cards.
W, H = 1280, 284
P = dict(void="#04060d", panel="#080e1a", ink="#eaf0fb", dim="#93a3c0",
         faint="#55658a", line="#22314d", cyan="#5cdcff", gold="#f4b063", green="#63e6a4")
OUT = _ROOT + "/assets/impact.svg"
MONO="'SFMono-Regular','JetBrains Mono','DejaVu Sans Mono',Consolas,monospace"
SANS="'Helvetica Neue',Helvetica,Arial,sans-serif"

# (big number, unit-suffix, label line1, label line2, accent)
CELLS = [
 ("800","+","tickets auto-resolved","per month · five-tier fleet", P["cyan"]),
 ("45→4","","minutes MTTR","−88% · saga-compensated", P["green"]),
 ("240","+","agent-callable tools","15+ MCP servers · 7 layers", P["cyan"]),
 ("17.6","k★","SuperAGI","founding engineer", P["gold"]),
 ("12","","detection engines","MANTIS autonomous SOC", P["cyan"]),
 ("2","","peer-reviewed papers","DOI-registered · verifiable", P["gold"]),
]
COLS, ROWS = 3, 2
PADX, TOP = 26, 58
cw = (W - PADX*2) / COLS
ch = (H - TOP - 22) / ROWS

s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" fill="none" role="img" aria-label="Impact by the numbers: 800+ tickets/month, MTTR 45 to 4 min, 240+ tools, SuperAGI 17.6k stars, 12 detection engines, 2 peer-reviewed papers.">']
s.append(f'''<defs><linearGradient id="pnl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P['panel']}"/><stop offset="1" stop-color="{P['void']}"/></linearGradient>
 <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{P['cyan']}" stop-opacity="0"/><stop offset="0.5" stop-color="{P['cyan']}"/><stop offset="1" stop-color="{P['cyan']}" stop-opacity="0"/></linearGradient></defs>''')
s.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#pnl)" stroke="{P["line"]}"/>')
s.append(f'<text x="{PADX}" y="36" font-family="{MONO}" font-size="14" letter-spacing="1.5" fill="{P["dim"]}"><tspan fill="{P["cyan"]}">$ </tspan>cat ./impact.log <tspan fill="{P["faint"]}"># real numbers, not repo stars</tspan></text>')
s.append(f'<rect x="{PADX}" y="46" width="150" height="1.5" fill="url(#scan)"><animate attributeName="x" values="{PADX};{W-PADX-150};{PADX}" dur="7s" repeatCount="indefinite"/></rect>')

for i,(num,suf,l1,l2,acc) in enumerate(CELLS):
    r,c = divmod(i, COLS)
    x = PADX + c*cw; y = TOP + r*ch
    # separators
    if c>0: s.append(f'<line x1="{x:.0f}" y1="{y+14:.0f}" x2="{x:.0f}" y2="{y+ch-14:.0f}" stroke="{P["line"]}"/>')
    s.append(f'<rect x="{x+14:.0f}" y="{y+15:.0f}" width="22" height="2.5" fill="{acc}"/>')
    s.append(f'<text x="{x+14:.0f}" y="{y+62:.0f}" font-family="{SANS}" font-size="40" font-weight="800" letter-spacing="-1.5" fill="{P["ink"]}">{num}<tspan fill="{acc}" font-size="28">{suf}</tspan></text>')
    s.append(f'<text x="{x+15:.0f}" y="{y+83:.0f}" font-family="{MONO}" font-size="12.5" fill="{P["dim"]}">{l1}</text>')
    s.append(f'<text x="{x+15:.0f}" y="{y+99:.0f}" font-family="{MONO}" font-size="11" fill="{P["faint"]}">{l2}</text>')
if ROWS==2: s.append(f'<line x1="{PADX+14}" y1="{TOP+ch:.0f}" x2="{W-PADX-14}" y2="{TOP+ch:.0f}" stroke="{P["line"]}"/>')
s.append('</svg>')
open(OUT,"w").write("\n".join(s)); print("wrote", OUT)
