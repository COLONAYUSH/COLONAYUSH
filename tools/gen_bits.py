#!/usr/bin/env python3
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
# divider.svg (animated scan line) + section-header SVGs (cyan console style).
A = _ROOT + "/assets/"
P = dict(void="#04060d", ink="#eaf0fb", dim="#93a3c0", faint="#55658a",
         cyan="#5cdcff", line="#22314d")
MONO = "&#39;SFMono-Regular&#39;,&#39;JetBrains Mono&#39;,&#39;DejaVu Sans Mono&#39;,Consolas,&#39;Courier New&#39;,monospace"

# ---- divider: hairline with a travelling cyan glow segment -----------------
divider = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 22" width="1280" height="22" fill="none" role="img" aria-label="">
 <defs><linearGradient id="seg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{P['cyan']}" stop-opacity="0"/><stop offset="0.5" stop-color="{P['cyan']}"/><stop offset="1" stop-color="{P['cyan']}" stop-opacity="0"/></linearGradient></defs>
 <line x1="0" y1="11" x2="1280" y2="11" stroke="{P['line']}"/>
 <rect x="0" y="8" width="2" height="6" fill="{P['cyan']}"/><rect x="1278" y="8" width="2" height="6" fill="{P['cyan']}"/>
 <rect x="0" y="10.2" width="150" height="1.6" fill="url(#seg)"><animate attributeName="x" values="-150;1280" dur="5.5s" repeatCount="indefinite"/></rect>
 <rect x="0" y="10.4" width="90" height="1.2" fill="{P['cyan']}" opacity="0.7"/>
</svg>'''
open(A+"divider.svg","w").write(divider)

# ---- section headers -------------------------------------------------------
HEADERS = {
 "h-whoami":      "cat ~/whoami",
 "h-now":         "tail -f ./now.log",
 "h-work":        "ls ./selected-work",
 "h-stack":       "cat ./arsenal.toml",
 "h-research":    "ls ./research --papers",
 "h-recognition": "cat ./recognition",
 "h-connect":     "ssh ayush@swarm",
}
CW = 10.5  # monospace advance at 18px
for fn, label in HEADERS.items():
    tw = len("$ " + label) * CW
    LP = 15
    W = int(LP + 22 + tw + 22)
    curx = LP + 22 + tw + 4
    # Chip fill == GitHub dark bg (#0d1117): blends away in dark mode (reads as a clean
    # terminal line), but becomes a legible dark chip in LIGHT mode — so the light label
    # text is never invisible on a white page. Faint cyan outline + underline in both.
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 42" width="{W}" height="42" fill="none" '
           f'font-family="{MONO}" role="img" aria-label="{label}">'
           f'<rect x="0.6" y="0.6" width="{W-1.2}" height="40.8" rx="8" fill="#0d1117" stroke="{P["cyan"]}" stroke-opacity="0.14"/>'
           f'<text x="{LP}" y="27" font-size="18" fill="{P["cyan"]}" font-weight="700">&#9656;</text>'
           f'<text x="{LP+22}" y="27" font-size="18" fill="{P["ink"]}" letter-spacing="0.5">'
           f'<tspan fill="{P["faint"]}">$ </tspan>{label}</text>'
           f'<rect x="{curx:.0f}" y="13" width="9" height="18" fill="{P["cyan"]}">'
           f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>'
           f'<rect x="{LP}" y="36" width="26" height="2" rx="1" fill="{P["cyan"]}" opacity="0.85"/>'
           f'</svg>')
    open(A+fn+".svg","w").write(svg)
print("wrote divider + %d headers" % len(HEADERS))
