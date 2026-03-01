# Tempus Campaign Site

Hugo static site for the Tempus D&D 5e campaign. Content is authored in Obsidian, converted to Hugo-compatible markdown via Python scripts, and deployed to DreamHost via GitHub Actions.

## Prerequisites

- [Hugo](https://gohugo.io/installation/) (extended, v0.148+)
- Python 3
- Git with submodule support

## Setup

```bash
git clone --recurse-submodules git@github.com:stoicrogue/tempus-hugo.git
cd tempus-hugo
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

## Content Pipeline

Content originates in the Obsidian vault at:
```
C:/Users/markm/obsidian/Mark/01 - Projects/tempus-campaign
```

Run `update.sh` from the repo root to sync vault content into Hugo:

```bash
./update.sh
```

This runs two scripts:
- **`convert_wikilinks.py`** — Converts `[[wiki-links]]` to Hugo-relative URLs, handles anchors and pipe aliases, removes orphan links (`--clean`)
- **`sync-obsidian-images.py`** — Converts `![[image.png]]` embeds to standard markdown and copies images to `static/images/`

## Local Development

```bash
hugo serve
```

Site available at `http://localhost:1313`.

## Build

```bash
hugo --minify
```

Output goes to `public/`.

## Deployment

Push to `main` triggers GitHub Actions → `hugo --minify` → rsync to DreamHost. No manual steps required.

## Content Structure

| Directory | Contents |
|---|---|
| `01---session-notes/` | Per-session write-ups |
| `02---characters/` | Player characters, allies, adversaries |
| `03---locations/` | Towns, dungeons, regions |
| `04---items/` | Notable items and artifacts |
| `05---planning/` | DM reference: encounters, stat blocks, FAQs |
| `06---factions/` | Organizations and factions |
| `07---rules/` | House rules and rulings |
| `08---recap/` | Campaign recaps and summaries |

Each directory requires an `_index.md` for navigation. All content files require frontmatter:

```yaml
---
tags:
  - [section-name]
  - tempus
date: YYYY-MM-DD
title: [Title]
author:
  - Mark Molea
---
```

Internal links should use Obsidian `[[wiki-links]]` — `convert_wikilinks.py` handles the conversion. Do not write Hugo-style relative URLs manually.

## Theme & Customization

- **Theme**: [`panr/hugo-theme-terminal`](https://github.com/panr/hugo-theme-terminal) v4.2.0 (git submodule at `themes/terminal/`)
- **Custom styles**: `static/style.css` (auto-loaded by the theme)
- **Layout overrides**: `layouts/` directory in repo root
- Do not edit the theme submodule directly
