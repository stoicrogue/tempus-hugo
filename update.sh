#!/usr/bin/env bash
set -euo pipefail

# Paths — adjust if your mount points differ in Git Bash
VAULT_PATH="/c/Users/markm/obsidian/Mark/01 - Projects/tempus-campaign"
CONTENT_PATH="/c/projects/tempus/content"
PROJECT_PATH="/c/projects/tempus"

cd "$PROJECT_PATH"

echo "=== Converting Obsidian notes to Hugo markdown ==="
python -u convert_wikilinks.py \
  --vault "$VAULT_PATH" \
  --content "$CONTENT_PATH" \
  --clean

echo "=== Copying and fixing image links ==="
python sync-obsidian-images.py

echo "✅ Sync complete!"
