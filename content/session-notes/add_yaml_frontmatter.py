#!/usr/bin/env python3
"""
Script to add YAML frontmatter to Tempus Session markdown files.
Processes files matching pattern: Tempus Session [0-9]+ ([0-9]{4}-[0-9]{2}-[0-9]{2}).md
"""

import os
import re
from pathlib import Path


def parse_filename(filename):
    """
    Parse filename to extract session number and date.
    
    Args:
        filename (str): Filename to parse
        
    Returns:
        tuple: (session_number, date) or (None, None) if parsing fails
    """
    pattern = r'Tempus Session (\d+) \((\d{4}-\d{2}-\d{2})\)\.md'
    match = re.match(pattern, filename)

    if match:
        session_number = match.group(1)
        date = match.group(2)
        return session_number, date

    return None, None


def generate_yaml_frontmatter(session_number, date):
    """
    Generate YAML frontmatter block.
    
    Args:
        session_number (str): Session number
        date (str): Date in YYYY-MM-DD format
        
    Returns:
        str: YAML frontmatter block
    """
    yaml_block = f"""---
tags:
  - session-notes
  - tempus
created: {date}
title: Tempus Session {session_number}
author:
  - Mark Molea
---

"""
    return yaml_block


def has_yaml_frontmatter(content):
    """
    Check if content already has YAML frontmatter.
    
    Args:
        content (str): File content
        
    Returns:
        bool: True if frontmatter exists, False otherwise
    """
    return content.strip().startswith('---')


def process_file(file_path):
    """
    Process a single markdown file to add YAML frontmatter.
    
    Args:
        file_path (Path): Path to the markdown file
        
    Returns:
        bool: True if file was processed, False if skipped
    """
    filename = file_path.name
    session_number, date = parse_filename(filename)

    if not session_number or not date:
        print(f"Skipping {filename}: doesn't match expected pattern")
        return False

    try:
        # Read existing content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if YAML frontmatter already exists
        if has_yaml_frontmatter(content):
            print(f"Skipping {filename}: YAML frontmatter already exists")
            return False

        # Generate YAML frontmatter
        yaml_frontmatter = generate_yaml_frontmatter(session_number, date)

        # Combine frontmatter with existing content
        new_content = yaml_frontmatter + content

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Processed {filename}: added YAML frontmatter")
        return True

    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False


def main():
    """
    Main function to process all matching markdown files in the current directory.
    """
    current_dir = Path('.')
    pattern = 'Tempus Session *.md'

    # Find all matching files
    markdown_files = list(current_dir.glob(pattern))

    if not markdown_files:
        print("No matching markdown files found in current directory")
        return

    print(f"Found {len(markdown_files)} matching files")

    processed_count = 0
    for file_path in sorted(markdown_files):
        if process_file(file_path):
            processed_count += 1

    print(f"\nProcessed {processed_count} out of {len(markdown_files)} files")


if __name__ == "__main__":
    main()
