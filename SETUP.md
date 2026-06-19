# Setup — your GitHub Profile README

This folder is a ready-to-push **GitHub Profile README**. When live it renders at the top of
`github.com/COLONAYUSH`. Everything is hand-built and themed (the `agent-os` amber console look),
distinct from your portfolio so the two read as one person, two surfaces.

```
github-profile/
├── README.md                     ← the profile page
├── assets/                       ← hand-built animated SVGs (banner, telemetry, typing, system map, headers)
└── .github/workflows/
    ├── snake.yml                 ← generates the contribution-snake (amber)
    └── activity.yml              ← auto-refreshes the "recent activity" list daily
```

---

## 1. Create the magic repo

GitHub shows a repo's README on your profile **only** when the repo name == your username.

1. New repository → name it exactly **`COLONAYUSH`** (must match your username, case-insensitive).
2. Make it **Public**. Tick **"Add a README"**.

## 2. Push these files

Copy the **contents of this `github-profile/` folder** into the root of that repo:

```bash
# from inside your cloned COLONAYUSH repo
cp -r /path/to/github-profile/* .
cp -r /path/to/github-profile/.github .
git add .
git commit -m "feat: agent-os profile README"
git push
```

> Important: `README.md`, the `assets/` folder, and `.github/` must sit at the **repo root** — not inside a `github-profile/` subfolder. The image paths (`assets/banner.svg`) are relative to the root.

## 3. Turn on the contribution snake 🐍

1. Repo → **Settings → Actions → General →** allow **"Read and write permissions"** (Workflow permissions).
2. Repo → **Actions** tab → enable workflows.
3. Open **"generate snake animation"** → **Run workflow** (it also runs twice daily).
4. It publishes `snake.svg` to an **`output`** branch; the README already points there. First run takes ~1 min, then the snake appears.

## 4. Include PRIVATE contributions (so the stats reflect reality)

A lot of your work (Lilly, AEGIS, CyberWay) is private. One toggle surfaces it:

- **github.com → Settings → Profile →** scroll to **Contributions & Activity** →
  tick **"Include private contributions on my profile."**

This makes the **streak**, **activity graph**, and **contribution calendar / snake** count private work (anonymized — no repo names leak).

> For the **stats card's** private *commit/star* counts too, deploy your own instance of
> `github-readme-stats` (free on Vercel) and point the README's stats URL at it with a PAT.
> Guide: https://github.com/anuraghazra/github-readme-stats#deploy-on-your-own — optional.

## 5. Two things to personalize

- **X / Twitter:** the README has an `X` badge pointing at `https://x.com/`. Replace with your handle
  (search `https://x.com/` in `README.md`). Remove the badge if you don't want it.
- **Recent activity:** the `activity.yml` workflow fills the `<!--START_SECTION:activity-->` block daily.
  It appears inside the collapsible "recent activity" disclosure under the stats. Safe to delete that
  `<details>` block + `activity.yml` if you'd rather keep it fully static.

---

## What's live vs. generated

| Piece | Source | Updates |
| :-- | :-- | :-- |
| Banner, telemetry, typing, system-map, section headers | hand-built SVGs in `assets/` (SMIL animation) | static files |
| Stats card · streak · top languages · activity graph | live services, themed via URL params | on every page view |
| Contribution snake | `snake.yml` Action → `output` branch | twice daily |
| Recent activity list | `activity.yml` Action → README markers | daily |
| Profile-views counter | komarev.com | on every view |

## Editing the SVGs

They're plain SVG with SMIL `<animate>` — open in any editor. Palette:
amber `#ffb627` / highlight `#ffe0a3` / ink `#e9ead6` / muted `#8a8f6c` / surface `#0d1117` / stroke `#4a3c16`.

## Preview locally

Open `github-readme-preview.html` (in the project root) — it renders this exact README with GitHub's
own markdown CSS on the real dark canvas, so what you see is what ships.
