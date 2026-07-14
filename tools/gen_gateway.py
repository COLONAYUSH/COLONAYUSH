#!/usr/bin/env python3
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
# gateway.svg — signature centerpiece: one tool call travels the enterprise
# 7-layer MCP gateway. A clean call reaches the tools; the annotation shows an
# attack dying at the safety gate. SMIL-synced (animates on GitHub as <img>).
W, H = 1280, 250
P = dict(void="#04060d", panel="#080e1a", ink="#eaf0fb", dim="#93a3c0",
         faint="#55658a", line="#22314d", cyan="#5cdcff", gold="#f4b063",
         green="#63e6a4", coral="#ff6a4d")
OUT = _ROOT + "/assets/gateway.svg"

SPINE_Y = 138
AX, TX = 96, 1184                      # agent, tools node x
GATES = [("L1","EDGE"),("L2","WAF"),("L3","ALB"),("L4","NET"),
         ("L5","OAUTH"),("L6","RBAC"),("L7","SAFETY")]
GX = [210 + i*(852/6) for i in range(7)]     # gate x positions
DUR = 6.0
TRAVEL = 0.6                                   # fraction of loop spent travelling
def t_at(x): return round(TRAVEL*(x-AX)/(TX-AX)*DUR, 2)   # when packet reaches x

s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" fill="none" role="img" aria-label="Enterprise 7-layer MCP gateway: a clean tool call reaches the tools; every attack dies at the layer built to catch it.">']
s.append(f'''<defs>
 <linearGradient id="pnl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P['panel']}"/><stop offset="1" stop-color="{P['void']}"/></linearGradient>
 <radialGradient id="tg" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{P['green']}" stop-opacity="0.9"/><stop offset="1" stop-color="{P['green']}" stop-opacity="0"/></radialGradient>
 <filter id="g" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="3"/></filter>
</defs>''')
# panel
s.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#pnl)" stroke="{P["line"]}"/>')
MONO="'SFMono-Regular','JetBrains Mono','DejaVu Sans Mono',Consolas,monospace"
# header + caption
s.append(f'<text x="34" y="42" font-family="{MONO}" font-size="15" letter-spacing="1.5" fill="{P["dim"]}"><tspan fill="{P["cyan"]}">$ </tspan>send ./tool-call --through 7-layer-gateway</text>')
s.append(f'<text x="34" y="{H-26}" font-family="{MONO}" font-size="12.5" letter-spacing="0.4" fill="{P["faint"]}">a clean call reaches the tools · every attack dies at the one layer built to catch it · 15+ MCP servers · 240+ tools</text>')
# spine
s.append(f'<line x1="{AX}" y1="{SPINE_Y}" x2="{TX}" y2="{SPINE_Y}" stroke="{P["line"]}" stroke-width="1.5"/>')
# progress overlay: a bright cyan segment that grows along the spine with the packet
s.append(f'<line x1="{AX}" y1="{SPINE_Y}" x2="{TX}" y2="{SPINE_Y}" stroke="{P["cyan"]}" stroke-width="1.5" stroke-opacity="0.55" stroke-dasharray="{TX-AX}" stroke-dashoffset="{TX-AX}"><animate attributeName="stroke-dashoffset" values="{TX-AX};0;0;{TX-AX};{TX-AX}" keyTimes="0;{TRAVEL};0.86;0.9;1" dur="{DUR}s" repeatCount="indefinite"/></line>')
# endpoints
s.append(f'<circle cx="{AX}" cy="{SPINE_Y}" r="7" fill="{P["cyan"]}"/><circle cx="{AX}" cy="{SPINE_Y}" r="13" fill="none" stroke="{P["cyan"]}" stroke-opacity="0.4"/>')
s.append(f'<text x="{AX}" y="{SPINE_Y+34}" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="1" fill="{P["dim"]}">AGENT</text>')
# tools node + green arrival pulse
s.append(f'<circle cx="{TX}" cy="{SPINE_Y}" r="30" fill="url(#tg)" opacity="0"><animate attributeName="opacity" values="0;0;0.8;0" keyTimes="0;{TRAVEL-0.02};{TRAVEL+0.04};0.9" dur="{DUR}s" repeatCount="indefinite"/></circle>')
s.append(f'<circle cx="{TX}" cy="{SPINE_Y}" r="11" fill="none" stroke="{P["green"]}" stroke-width="1.5"/><circle cx="{TX}" cy="{SPINE_Y}" r="5" fill="{P["green"]}" opacity="0.5"><animate attributeName="opacity" values="0.5;0.5;1;0.5" keyTimes="0;{TRAVEL-0.02};{TRAVEL+0.04};1" dur="{DUR}s" repeatCount="indefinite"/></circle>')
s.append(f'<text x="{TX}" y="{SPINE_Y+34}" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="1" fill="{P["green"]}">TOOLS</text>')
# gates
for i,(tag,name) in enumerate(GATES):
    x=GX[i]; tt=t_at(x); safety = (i==6)
    # gate bar (scans cyan as the packet passes)
    s.append(f'<rect x="{x-1.25:.1f}" y="{SPINE_Y-34}" width="2.5" height="68" rx="1.25" fill="{P["cyan"]}" opacity="0.28"><animate attributeName="opacity" values="0.28;1;0.55;0.28;0.28" keyTimes="0;0.03;0.16;0.4;1" begin="{tt}s" dur="{DUR}s" repeatCount="indefinite"/></rect>')
    s.append(f'<circle cx="{x:.1f}" cy="{SPINE_Y}" r="4.5" fill="{P["cyan"]}" opacity="0.5"><animate attributeName="opacity" values="0.5;1;0.5" keyTimes="0;0.06;0.3" begin="{tt}s" dur="{DUR}s" repeatCount="indefinite"/><animate attributeName="r" values="4.5;7;4.5" keyTimes="0;0.06;0.3" begin="{tt}s" dur="{DUR}s" repeatCount="indefinite"/></circle>')
    s.append(f'<text x="{x:.1f}" y="{SPINE_Y-44}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="600" fill="{P["ink"] if not safety else P["gold"]}">{name}</text>')
    s.append(f'<text x="{x:.1f}" y="{SPINE_Y+52}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{P["faint"]}">{tag}</text>')
# attack annotation at the safety gate (L7): coral ✕ that pulses to show attacks die here
sx=GX[6]
s.append(f'<g opacity="0.9"><circle cx="{sx:.1f}" cy="{SPINE_Y-70}" r="9" fill="none" stroke="{P["coral"]}" stroke-width="1.4"><animate attributeName="opacity" values="0.3;1;0.3" dur="2.6s" repeatCount="indefinite"/></circle>'
         f'<path d="M{sx-3.5:.1f} {SPINE_Y-73.5} l7 7 M{sx+3.5:.1f} {SPINE_Y-73.5} l-7 7" stroke="{P["coral"]}" stroke-width="1.6"/></g>')
s.append(f'<text x="{sx:.1f}" y="{SPINE_Y-86}" text-anchor="middle" font-family="{MONO}" font-size="9.5" letter-spacing="0.5" fill="{P["coral"]}">injection ✕ blocked</text>')
# the packet: cyan diamond with glow, travelling agent -> tools then hidden on reset
def packet():
    cxv=f'{AX};{TX};{TX};{AX};{AX}'; kt=f'0;{TRAVEL};0.86;0.865;1'
    opv='0;1;1;0;0'; okt=f'0;0.04;0.82;0.88;1'
    return (f'<g><animateTransform attributeName="transform" type="translate" values="{cxv.replace(";"," 0;")} 0" keyTimes="{kt}" dur="{DUR}s" repeatCount="indefinite" additive="sum"/>'
            f'<g opacity="0"><animate attributeName="opacity" values="{opv}" keyTimes="{okt}" dur="{DUR}s" repeatCount="indefinite"/>'
            f'<circle cx="0" cy="{SPINE_Y}" r="10" fill="{P["cyan"]}" opacity="0.5" filter="url(#g)"/>'
            f'<path d="M0 {SPINE_Y-7} L7 {SPINE_Y} L0 {SPINE_Y+7} L-7 {SPINE_Y} Z" fill="{P["cyan"]}"/>'
            f'<line x1="-10" y1="{SPINE_Y}" x2="-34" y2="{SPINE_Y}" stroke="{P["cyan"]}" stroke-width="2" stroke-opacity="0.3"/></g></g>')
s.append(packet())
s.append('</svg>')
open(OUT,"w").write("\n".join(s)); print("wrote",OUT)
