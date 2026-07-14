#!/usr/bin/env python3
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
# Generates hero.svg — the profile banner. A deep-space swarm (portfolio-brand)
# with a signature tagline. Deterministic particle field + SMIL drift/twinkle,
# so it animates on GitHub (served as an <img>, camo renders SVG animation).
import math, random

OUT = _ROOT + "/assets/hero.svg"
W, H = 1280, 420
random.seed(7)  # deterministic art

P = dict(void="#04060d", deep="#0a1322", ink="#eaf0fb", dim="#93a3c0",
         faint="#55658a", cyan="#5cdcff", gold="#f4b063", green="#63e6a4",
         coral="#ff6a4d")

FX, FY = 1030, 150   # swarm focal point (far upper-right, clear of the text)

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;")

parts = []  # particles: (x,y,r,color,base_opacity)
# ~62% clustered around the focal point, rest scattered as a faint field
for _ in range(46):
    a = random.uniform(0, 2*math.pi); d = abs(random.gauss(0, 165))
    x, y = FX + math.cos(a)*d*1.15, FY + math.sin(a)*d*0.8
    if -20 < x < W+20 and -20 < y < H+20:
        near = max(0, 1 - d/300)
        col = P["cyan"] if random.random() > 0.14 else random.choice([P["gold"], P["green"]])
        parts.append((x, y, 0.8+near*2.0+random.random()*0.7, col, 0.25+near*0.7))
for _ in range(30):
    x, y = random.uniform(30, W-30), random.uniform(30, H-30)
    parts.append((x, y, 0.6+random.random()*1.3, P["cyan"], 0.12+random.random()*0.3))

def circle(i, x, y, r, col, op):
    dx, dy = random.uniform(-9, 9), random.uniform(-7, 7)
    dur = round(random.uniform(6, 15), 1); tw = round(random.uniform(3, 7), 1)
    beg = round(random.uniform(-8, 0), 1)
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{col}" opacity="{op:.2f}">'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="0 0; {dx:.1f} {dy:.1f}; 0 0" dur="{dur}s" begin="{beg}s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"/>'
            f'<animate attributeName="opacity" values="{op:.2f};{min(1,op*1.7):.2f};{op*0.5:.2f};{op:.2f}" dur="{tw}s" begin="{beg}s" repeatCount="indefinite"/>'
            f'</circle>')

# faint constellation links between nearby bright-ish particles near the focal
links = []
bright = [p for p in parts if p[4] > 0.5]
for i, a in enumerate(bright):
    for b in bright[i+1:]:
        dd = math.hypot(a[0]-b[0], a[1]-b[1])
        if dd < 92 and random.random() > 0.45:
            links.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{P["cyan"]}" stroke-width="0.6" opacity="{max(0.05,0.22-dd/600):.2f}"/>')

# two soft swarm trails with a travelling glow dash
def trail(path, dur, op):
    return (f'<path d="{path}" fill="none" stroke="{P["cyan"]}" stroke-width="1.4" opacity="{op}" '
            f'stroke-linecap="round" stroke-dasharray="26 340"><animate attributeName="stroke-dashoffset" '
            f'from="366" to="0" dur="{dur}s" repeatCount="indefinite"/></path>')

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" fill="none" role="img" aria-label="Ayush Kumar — AI agents are getting hands. I make sure they can\'t be turned against you.">')
svg.append(f'''<defs>
  <radialGradient id="bg" cx="0.72" cy="0.28" r="0.95">
    <stop offset="0" stop-color="{P['deep']}"/><stop offset="0.55" stop-color="#060a13"/><stop offset="1" stop-color="{P['void']}"/>
  </radialGradient>
  <radialGradient id="focal" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{P['cyan']}" stop-opacity="0.30"/><stop offset="0.5" stop-color="{P['cyan']}" stop-opacity="0.06"/><stop offset="1" stop-color="{P['cyan']}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="scrim" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{P['void']}" stop-opacity="0.92"/><stop offset="0.42" stop-color="{P['void']}" stop-opacity="0.78"/><stop offset="0.8" stop-color="{P['void']}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="cyanfade" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{P['cyan']}"/><stop offset="1" stop-color="{P['cyan']}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{P['faint']}" stroke-opacity="0.14" stroke-width="1"/></pattern>
  <filter id="soft" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="3.4"/></filter>
</defs>''')
svg.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
svg.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
svg.append(f'<circle cx="{FX}" cy="{FY}" r="360" fill="url(#focal)"/>')
# trails
svg.append(trail(f"M1240 40 C1080 90 1180 210 980 250 S760 300 900 360", 7.5, 0.5))
svg.append(trail(f"M1270 210 C1120 240 1140 120 960 150 S720 120 840 60", 9.5, 0.35))
# particle field (glow layer + crisp layer)
svg.append(f'<g filter="url(#soft)" opacity="0.7">')
for i, (x, y, r, col, op) in enumerate(parts):
    if op > 0.55: svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r*1.8:.2f}" fill="{col}" opacity="{op*0.5:.2f}"/>')
svg.append('</g>')
svg.append('<g>'); svg += links; svg += [circle(i,*p) for i,p in enumerate(parts)]; svg.append('</g>')
# scrim for text legibility
svg.append(f'<rect width="{W}" height="{H}" fill="url(#scrim)"/>')
# corner brackets
svg.append(f'<g stroke="{P["cyan"]}" stroke-width="1.5" opacity="0.55" fill="none">'
           f'<path d="M30 30 H70 M30 30 V70"/><path d="M1250 30 H1210 M1250 30 V70"/>'
           f'<path d="M30 390 H70 M30 390 V350"/><path d="M1250 390 H1210 M1250 390 V350"/></g>')

MONO = "'SFMono-Regular','JetBrains Mono','DejaVu Sans Mono',Consolas,monospace"
SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"
# eyebrow with pulsing dot
svg.append(f'<circle cx="78" cy="119" r="5" fill="{P["cyan"]}"><animate attributeName="opacity" values="1;0.35;1" dur="2.4s" repeatCount="indefinite"/></circle>')
svg.append(f'<text x="95" y="124" font-family="{MONO}" font-size="15" letter-spacing="4" fill="{P["dim"]}">AGENTIC AI · SECURITY &amp; RUNTIME</text>')
# headline + subhead (heavy sans)
svg.append(f'<text x="74" y="212" font-family="{SANS}" font-size="62" font-weight="800" letter-spacing="-1.5" fill="{P["ink"]}">AI agents are getting hands.</text>')
svg.append(f'<text x="74" y="272" font-family="{SANS}" font-size="40" font-weight="700" letter-spacing="-0.8" fill="{P["dim"]}">I make sure they can\'t be turned against you.</text>')
# role line
svg.append(f'<text x="74" y="330" font-family="{MONO}" font-size="18" letter-spacing="1" fill="{P["cyan"]}">AYUSH KUMAR<tspan fill="{P["faint"]}">  ·  Lead AI Security Architect · LLMs, agents &amp; MCP, build → runtime</tspan></text>')
# baseline scan hairline
svg.append(f'<rect x="74" y="356" width="220" height="1.5" fill="url(#cyanfade)"><animate attributeName="width" values="0;220;220" keyTimes="0;0.6;1" dur="2.2s" begin="0.3s" fill="freeze"/></rect>')
svg.append(f'<text x="74" y="384" font-family="{MONO}" font-size="12.5" letter-spacing="2" fill="{P["faint"]}">700K-AGENT SWARM · ENFORCEMENT NOT ALERTING · THE SWARM IS LISTENING</text>')
svg.append('</svg>')

open(OUT, "w").write("\n".join(svg))
print("wrote", OUT, "· particles:", len(parts), "· links:", len(links))
