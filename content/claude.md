---
tags:
  - 
  - tempus
date: 2026-02-05
title: CLAUDE
author:
  - Mark Molea
---
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Obsidian vault** for managing a D&D 5e campaign called "Tempus." It contains session notes, character sheets, locations, items, homebrew rules, and campaign recaps spanning 45+ sessions (November 2022 - October 2025).

## Directory Structure

The vault uses numbered prefixes for organization:

- `01 - session-notes/` - Per-session DM prep notes (45 sessions)
- `02 - characters/` - NPCs, party members, adversaries, monster stat blocks
  - `main-party/` - Player characters and party reference sheet
  - `adversaries/` - Villain stat blocks (CR up to 17)
  - `allies/` - NPC allies
  - `monsters/` - Creature stat blocks
- `03 - locations/` - Setting descriptions and maps
- `04 - items/` - Magical and homebrew equipment
- `05 - planning/` - Campaign arcs, encounter design, session prep
- `06 - factions/` - Organizations (Chained Library, Massa'Ista)
- `07 - rules/` - Homebrew mechanics (Minion Rules)
- `08 - recap/` - Campaign summaries, quest log, timeline, dramatized narratives

## Automation Scripts (Hugo Integration)

These scripts ensure frontmatter compatibility for publishing campaign notes to a Hugo-based website. A separate project contains the Hugo site and copy scripts.

### `obsidian_frontmatter_script.py`
Processes all markdown files to add/update YAML frontmatter. Run from the `tempus-campaign` directory:
```bash
python obsidian_frontmatter_script.py
```
- Adds standardized frontmatter (tags, date, title, author)
- Derives section tags from parent directory names
- Preserves existing frontmatter values

### `add_yaml_frontmatter.py`
Adds frontmatter specifically to session note files matching pattern `Tempus Session [NUMBER] (YYYY-MM-DD).md`. Run from `01 - session-notes/`:
```bash
python ../add_yaml_frontmatter.py
```

## File Conventions

**Frontmatter format:**
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

**Session note naming:** `Tempus Session [NUMBER] (YYYY-MM-DD).md`

**Internal linking:** Uses Obsidian wiki-style links `[[Character Name]]`, `[[Location]]`

**Index files:** Each directory has `_index.md` for navigation

## DM Style and Prep Evolution

The DM's session prep has evolved through three phases (detailed in `08 - recap/Session Prep Evolution.md`):

1. **Experimental (Sessions 00-05)** - Theater of mind philosophy, simple structure, light prep
2. **Structured Consistency (Sessions 10-23)** - Adopted Sly Flourish's "Return of the Lazy Dungeon Master" template with consistent sections (Strong Start, Scenes, Secrets/Clues, Fantastic Locations, NPCs, Monsters, Treasure)
3. **Enhanced Preparation (Sessions 30-47)** - Visual formatting (emojis), exhaustive stat blocks with DPR calculations, elaborate encounter frameworks (d12 tables with multiple scenarios), narrative "Cold Open" prose sections

Key insight: Despite "lazy DM" philosophy, prep has become more detailed over time—preparing multiple contingencies and frameworks that enable better improvisation rather than minimal notes.
