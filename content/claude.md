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
  - `adversaries/` - Villain narrative lore pages and stat blocks (CR up to 17)
  - `allies/` - NPC ally narrative lore pages (Arbiter, Trius, Elara Sunforge, Vidrir, etc.)
  - `monsters/` - Creature stat blocks
- `03 - locations/` - Setting descriptions and maps
- `04 - items/` - Magical and homebrew equipment
- `05 - planning/` - Campaign arcs, encounter design, session prep, DM reference material (reveal FAQs, guest player briefings, encounter tables)
- `06 - factions/` - Organizations (Chained Library, Massa'Ista)
- `07 - rules/` - Homebrew mechanics (Minion Rules)
- `08 - recap/` - Campaign summaries, quest log, timeline, dramatized narratives

## Automation Scripts

### `_link_characters.py`
Scans markdown files for unlinked character name references and converts them to Obsidian `[[wiki-links]]`. Run from the `tempus-campaign` directory:
```bash
python _link_characters.py          # apply changes
python _link_characters.py --dry-run  # preview without modifying files
```
- Targets: `01 - session-notes/`, `02 - characters/`, `03 - locations/`, `05 - planning/`, `06 - factions/`, `08 - recap/` (recursive)
- Skips: `Tempus Campaign Dramatization.md`
- Links 21 characters from `02 - characters/adversaries/` and `02 - characters/allies/`
- Case-insensitive matching with proper display text (e.g., `serenity` → `[serenity](/02---characters/adversaries/serenity)`)
- Uses pipe syntax for partial names (e.g., `Elara` → `[Elara](/02---characters/allies/elara-sunforge)`)
- Skips: frontmatter, code blocks, headings, text already inside `[[...]]`, self-references (e.g., `Manus.md` won't link to `[Manus](/02---characters/adversaries/manus)`)
- Safe to re-run — idempotent (0 changes if already linked)
- To add new characters: update the `CHARACTERS` list at the top of the script

### `_link_factions.py`
Scans markdown files for unlinked faction name references and converts them to Obsidian `[[wiki-links]]`. Run from the `tempus-campaign` directory:
```bash
python _link_factions.py          # apply changes
python _link_factions.py --dry-run  # preview without modifying files
```
- Targets: `01 - session-notes/`, `02 - characters/`, `03 - locations/`, `05 - planning/`, `06 - factions/`, `08 - recap/` (recursive)
- Skips: `Tempus Campaign Dramatization.md`
- Links 8 factions: Cult of the Eclipse, Order of Seasons, Chained Library, Massa'Ista, Summer Court, Winter Court, Spring Court, Autumn Court
- Handles both curly and straight apostrophe variants for Massa'Ista
- Case-insensitive matching with proper display text
- Skips: frontmatter, code blocks, headings, text already inside `[[...]]`, self-references
- Safe to re-run — idempotent (0 changes if already linked)
- To add new factions: update the `FACTIONS` list at the top of the script

### `_link_locations.py`
Scans markdown files for unlinked location name references and converts them to Obsidian `[[wiki-links]]`. Run from the `tempus-campaign` directory:
```bash
python _link_locations.py          # apply changes
python _link_locations.py --dry-run  # preview without modifying files
```
- Targets: `01 - session-notes/`, `02 - characters/`, `03 - locations/`, `05 - planning/`, `06 - factions/`, `08 - recap/` (recursive)
- Skips: `Tempus Campaign Dramatization.md`
- Links locations from `03 - locations/` (currently: Tannis)
- Case-insensitive matching with proper display text
- Skips: frontmatter, code blocks, headings, text already inside `[[...]]`, self-references
- Safe to re-run — idempotent (0 changes if already linked)
- To add new locations: update the `LOCATIONS` list at the top of the script

### Hugo Integration

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

## Narrative Lore Page Format

Character and location files follow a consistent narrative structure (established with Nidhogg, then applied across adversaries, allies, and locations):

- **Adversaries:** Nidhogg, Weaver, Serenity, Manus
- **Allies:** Trius, Arbiter, Elara Sunforge, Vidrir
- **Locations:** Tannis

Format:

- **Frontmatter:** `tags` (Villain, Ally, Location, etc.), `date`, `title`, `created`
- **`# Heading`** followed by **top-level identity bullets** summarizing the entity at a glance
- **`##` thematic sections** organized by narrative significance (not stat-block-first)
- **`[[wiki-links]]`** throughout for cross-referencing characters, locations, and factions
- **Stat blocks** go in separate files (e.g., `Manus - Original StatBlock.md`, `Manus - Chaos Duelist.md`) linked from the narrative page under a `## Stat Block` section
- **DM reference material** (reveal FAQs, roleplay guides, encounter tables) goes in separate files in `05 - planning/`, linked from the narrative page (e.g., `[Vidrir - Odin Reveal](/05---planning/vidrir---odin-reveal)`, `[Trius Quick Reference](/05---planning/final-battle/trius-quick-reference)`)
- **Quotes** from session notes or journals included where available for flavor
- **Images** are preserved at the bottom of the file

## DM Style and Prep Evolution

The DM's session prep has evolved through three phases (detailed in `08 - recap/Session Prep Evolution.md`):

1. **Experimental (Sessions 00-05)** - Theater of mind philosophy, simple structure, light prep
2. **Structured Consistency (Sessions 10-23)** - Adopted Sly Flourish's "Return of the Lazy Dungeon Master" template with consistent sections (Strong Start, Scenes, Secrets/Clues, Fantastic Locations, NPCs, Monsters, Treasure)
3. **Enhanced Preparation (Sessions 30-47)** - Visual formatting (emojis), exhaustive stat blocks with DPR calculations, elaborate encounter frameworks (d12 tables with multiple scenarios), narrative "Cold Open" prose sections

Key insight: Despite "lazy DM" philosophy, prep has become more detailed over time—preparing multiple contingencies and frameworks that enable better improvisation rather than minimal notes.
