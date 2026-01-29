#!/usr/bin/env python3
import os
import re
import sys
import shutil
import argparse
import unicodedata
from pathlib import Path

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
WIKILINK_RE = re.compile(r'(?P<embed>!?)\[\[(?P<body>[^\]]+)\]\]')

def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[#/]+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s._-]', '', text)
    text = re.sub(r'\s+', '-', text.strip())
    return text.lower()

def anchor_slug(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'\s+', '-', text)

def build_note_index(vault_dir: Path):
    index = {}
    for md in vault_dir.rglob('*.md'):
        rel = md.relative_to(vault_dir)
        parts = list(rel.parts[:-1]) + [slugify(md.stem) + '.md']
        hugo_rel_path = Path(*[slugify(p) for p in parts]).as_posix()
        index[md.stem] = hugo_rel_path
        index[slugify(md.stem)] = hugo_rel_path
        index[rel.with_suffix('').as_posix()] = hugo_rel_path
    return index

def is_image_like(body: str) -> bool:
    name = body.split('|', 1)[0].split('#', 1)[0].strip()
    return os.path.splitext(name)[1].lower() in IMAGE_EXTS

def resolve_target(body: str, index: dict):
    alias = None
    page = body
    frag = None
    if '|' in page:
        page, alias = page.split('|', 1)
    if '#' in page:
        page, frag = page.split('#', 1)
        frag = anchor_slug(frag)
    page = page.strip()
    alias = alias.strip() if alias else None

    candidates = [page, page.replace('\\', '/'), slugify(page)]
    target = None
    for c in candidates:
        if c in index:
            target = index[c]
            break
    if not target:
        return None, None

    text = alias or page
    if frag:
        target += f'#{frag}'
    return text, target

def _to_site_path(target_with_optional_frag: str) -> str:
    """
    Convert a content-relative file path like 'lore/spring-court.md#tavern'
    into a site-root URL like '/lore/spring-court#tavern'.
    """
    if '#' in target_with_optional_frag:
        path_part, frag = target_with_optional_frag.split('#', 1)
        frag = '#' + frag
    else:
        path_part, frag = target_with_optional_frag, ''

    # normalize separators, drop the .md suffix, and ensure single leading slash
    path_part = path_part.replace('\\', '/')
    if path_part.lower().endswith('.md'):
        path_part = path_part[:-3]
    if not path_part.startswith('/'):
        path_part = '/' + path_part

    return path_part + frag

def replace_wikilinks(md_text: str, index: dict) -> str:
    def repl(m: re.Match):
        embed = m.group('embed')
        body  = m.group('body')

        # Leave images and page-embeds alone so your image pass can handle them
        if is_image_like(body) or embed:
            return m.group(0)

        text, target = resolve_target(body, index)
        if not target:
            return m.group(0)

        url = _to_site_path(target)
        return f'[{text}]({url})'

    return WIKILINK_RE.sub(repl, md_text)

def convert_vault(vault_dir: Path, content_dir: Path, clean=False):
    if clean and content_dir.exists():
        shutil.rmtree(content_dir)
    index = build_note_index(vault_dir)
    for src in vault_dir.rglob('*.md'):
        rel = src.relative_to(vault_dir)
        print(f"Processing: {rel}")
        out_parts = [slugify(p) for p in rel.parts[:-1]] + [slugify(src.stem) + '.md']
        dst = content_dir.joinpath(*out_parts)
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding='utf-8')
        dst.write_text(replace_wikilinks(text, index), encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True)
    ap.add_argument('--content', required=True)
    ap.add_argument('--clean', action='store_true')
    args = ap.parse_args()
    convert_vault(Path(args.vault), Path(args.content), clean=args.clean)
    print("✅ Markdown converted and copied.")

if __name__ == '__main__':
    main()
