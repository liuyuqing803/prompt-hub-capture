#!/usr/bin/env python3
"""Save a reusable prompt into the local PromptHub."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from pathlib import Path


ROOT = Path(os.environ.get("PROMPT_HUB_ROOT", "/Users/jean/Documents/PromptHub")).expanduser()
PROMPTS_DIR = ROOT / "prompts"
INDEX_PATH = ROOT / "index" / "prompts-index.md"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:60].strip("-") or "prompt"


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def render_prompt_file(
    title: str,
    category: str,
    tags: list[str],
    created: str,
    usage: str,
    rationale: str,
    prompt: str,
) -> str:
    tags_yaml = "\n".join(f'  - "{yaml_escape(tag)}"' for tag in tags)
    return f"""---
title: "{yaml_escape(title)}"
category: "{yaml_escape(category)}"
tags:
{tags_yaml}
created: "{created}"
source: "user-input"
---

# {title}

## Usage

{usage}

## Original Prompt

```text
{prompt.rstrip()}
```

## Applicable Scenarios

- Reuse this prompt for similar tasks.
- Adapt the variables and context before sending it to an agent.

## Category Rationale

{rationale}
"""


def ensure_index() -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    if INDEX_PATH.exists():
        return
    INDEX_PATH.write_text(
        "# Prompt Hub Index\n\n"
        "This index is maintained by `prompt-hub-capture`.\n\n"
        "| Created | Title | Category | Tags | Path |\n"
        "| --- | --- | --- | --- | --- |\n",
        encoding="utf-8",
    )


def update_index(created: str, title: str, category: str, tags: list[str], path: Path) -> None:
    ensure_index()
    rel_path = path.relative_to(ROOT)
    new_row = f"| {created} | {title} | `{category}` | {', '.join(tags)} | `{rel_path}` |\n"
    content = INDEX_PATH.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)
    header_end = 0
    separator_seen = False
    for index, line in enumerate(lines):
        if line.startswith("| --- "):
            header_end = index + 1
            separator_seen = True
            break
    if not separator_seen:
        lines.extend(
            [
                "\n",
                "| Created | Title | Category | Tags | Path |\n",
                "| --- | --- | --- | --- | --- |\n",
            ]
        )
        header_end = len(lines)
    lines.insert(header_end, new_row)
    INDEX_PATH.write_text("".join(lines), encoding="utf-8")


def parse_tags(raw: str) -> list[str]:
    tags = [tag.strip().lower() for tag in raw.split(",") if tag.strip()]
    seen: set[str] = set()
    result: list[str] = []
    for tag in tags:
        safe = re.sub(r"\s+", "-", tag)
        if safe not in seen:
            seen.add(safe)
            result.append(safe)
    return result or ["prompt"]


def unique_path(category_dir: Path, created: str, title: str) -> Path:
    base = f"{created}-{slugify(title)}"
    path = category_dir / f"{base}.md"
    counter = 2
    while path.exists():
        path = category_dir / f"{base}-{counter}.md"
        counter += 1
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Save a prompt into the local PromptHub.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--tags", required=True, help="Comma-separated tags")
    parser.add_argument("--usage", required=True)
    parser.add_argument("--rationale", required=True)
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt")
    prompt_group.add_argument("--prompt-file")
    args = parser.parse_args()

    created = dt.date.today().isoformat()
    category = args.category.strip().lower()
    tags = parse_tags(args.tags)
    prompt = args.prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")

    category_dir = PROMPTS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    path = unique_path(category_dir, created, args.title)
    body = render_prompt_file(
        title=args.title.strip(),
        category=category,
        tags=tags,
        created=created,
        usage=args.usage.strip(),
        rationale=args.rationale.strip(),
        prompt=prompt or "",
    )
    path.write_text(body, encoding="utf-8")
    update_index(created, args.title.strip(), category, tags, path)

    print(f"saved_path={path}")
    print(f"category={category}")
    print(f"tags={','.join(tags)}")
    print(f"index_path={INDEX_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
