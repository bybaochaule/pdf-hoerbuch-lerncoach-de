#!/usr/bin/env python3
"""Split a Markdown read-aloud script into TTS-friendly chunks."""
from __future__ import annotations

import argparse
from pathlib import Path


def split_text(text: str, max_chars: int) -> list[str]:
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for para in paragraphs:
        extra = len(para) + (2 if current else 0)
        if current and current_len + extra > max_chars:
            chunks.append('\n\n'.join(current))
            current = [para]
            current_len = len(para)
        else:
            current.append(para)
            current_len += extra
    if current:
        chunks.append('\n\n'.join(current))
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description='Markdown in TTS-Chunks teilen')
    parser.add_argument('input', help='Markdown-Datei')
    parser.add_argument('--max-chars', type=int, default=3500)
    parser.add_argument('--out-dir', default='tts_chunks')
    args = parser.parse_args()
    if args.max_chars < 500:
        raise SystemExit('fehler: --max-chars sollte mindestens 500 sein')
    text = Path(args.input).read_text(encoding='utf-8')
    chunks = split_text(text, args.max_chars)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for idx, chunk in enumerate(chunks, start=1):
        (out_dir / f'chunk_{idx:03d}.md').write_text(chunk + '\n', encoding='utf-8')
    print(f'{len(chunks)} Chunks geschrieben nach {out_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
