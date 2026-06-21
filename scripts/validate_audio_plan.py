#!/usr/bin/env python3
"""Lightweight checks for generated audio learning Markdown plans."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_HEADINGS = [
    'Hoersitzung',
    'Ziel',
    'Vorleseskript',
    'Checkfragen',
]


def main() -> int:
    parser = argparse.ArgumentParser(description='Audio-Lernplan pruefen')
    parser.add_argument('markdown')
    args = parser.parse_args()
    text = Path(args.markdown).read_text(encoding='utf-8')
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading.lower() not in text.lower():
            errors.append(f'fehlt: {heading}')
    long_paragraphs = [p for p in re.split(r'\n\s*\n', text) if len(p) > 1200]
    if long_paragraphs:
        errors.append(f'{len(long_paragraphs)} Absatz/Absaetze sind laenger als 1200 Zeichen')
    if '|---' in text:
        errors.append('Markdown-Tabelle gefunden; fuer Vorleseskript besser in gesprochene Sprache umwandeln')
    if errors:
        print('Validierung fehlgeschlagen:')
        for error in errors:
            print(f'- {error}')
        return 1
    print('Audio-Lernplan wirkt TTS-freundlich.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
