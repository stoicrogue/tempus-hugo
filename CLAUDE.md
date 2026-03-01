# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is the **Hugo static site** for the Tempus D&D 5e campaign. It is distinct from the source Obsidian vault (at `/c/Users/markm/obsidian/Mark/01 - Projects/tempus-campaign`). Content flows from the vault into this repo via Python scripts, then deploys to DreamHost via GitHub Actions.

## Content Pipeline

1. **Source**: Obsidian vault with `[[wiki-links]]` and `![[image]]` embeds
2. **Convert**: `update.sh` runs two Python scripts to transform vault files into Hugo-compatible markdown
3. **Publish**: Push to `main` triggers GitHub Actions → `hugo --minify` → rsync to DreamHost

```bash
# Run from repo root to sync content from Obsidian vault
./update.sh
```

**`convert_wikilinks.py`** — Converts `[[wiki-links]]` to Hugo-relative URLs (e.g., `[[Manus]]` → `[Manus](/02---characters/adversaries/manus)`). Also handles anchors, pipe aliases, and orphan link cleanup via `--clean` flag.

**`sync-obsidian-images.py`** — Converts `![[image.png]]` embeds to standard markdown, copies images to `static/images/`.

## Build & Deploy

```bash
hugo serve          # local dev server
hugo --minify       # production build (output: public/)
```

Deployment is fully automated via `.github/workflows/deploy.yml` on push to `main`. No manual deploy steps needed.

## Content Conventions

**Frontmatter** (required on all content files):
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

**File naming**: kebab-case with directory prefix matching the Hugo URL slug (e.g., `weaver---final-battle-stats.md` → `/05---planning/final-battle/weaver---final-battle-stats`). Hugo uses triple-dash `---` in the URL where directory separators appear.

**Internal links**: Use Obsidian `[[wiki-links]]` in source files — the conversion script handles them. Do not write Hugo-style relative URLs manually in source files.

**Index files**: Each content directory requires `_index.md` for navigation to work.

## Narrative Lore Page Format

Character and location pages follow a consistent structure (see existing adversary/ally pages as reference):

- `# Heading` with top-level identity bullets (role, affiliation, key traits)
- `##` thematic sections organized by narrative significance — **not** stat-block-first
- Stat blocks go in **separate files** linked from the narrative page under a `## Stat Block` section
- DM reference material (reveal FAQs, encounter tables, roleplay guides) goes in `05---planning/`, linked from the narrative page
- `[[wiki-links]]` throughout for cross-referencing
- Quotes from sessions or journals for flavor; images at the bottom

## Theme

The `themes/terminal/` directory is a git submodule (`panr/hugo-theme-terminal` v4.2.0). Custom overrides live in the repo's `layouts/` and `static/` directories — prefer overriding there rather than modifying the submodule.

## Hugo Configuration

Key settings in `hugo.toml`:
- `contentTypeName = "posts"` — content treated as blog posts
- `[frontmatter] lastmod = [':git', ...]` — last-modified dates sourced from git history
- Navigation menu auto-generated from the 8 numbered content sections
- Syntax highlighting uses external CSS classes (`noClasses = false`)
