# tools · asset generators

The SVGs in [`../assets`](../assets) are **generated**, not hand-edited — deterministic,
self-contained (Python 3 standard library only), and written straight into `../assets`.
Re-run any script after editing to regenerate:

```bash
python3 tools/gen_hero.py      # hero.svg     — deep-space swarm banner
python3 tools/gen_gateway.py   # gateway.svg  — 7-layer MCP gateway centerpiece
python3 tools/gen_impact.py    # impact.svg   — by-the-numbers panel
python3 tools/gen_bits.py      # divider.svg + console section headers (h-*.svg)
```

`gen_preview.py` renders this README through GitHub's own Markdown API into a local
`preview.html` — a faithful check before pushing (it isn't part of the profile).

Every script keeps its theme in a `P` palette dict at the top (deep-space void + cyan
swarm, matched to [ayushsec.vercel.app](https://ayushsec.vercel.app)); edit those tokens
to re-colour everything. Animation is SMIL, so it plays when GitHub serves the SVGs.
