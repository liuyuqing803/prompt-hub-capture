# Prompt Hub Capture

Codex skill for saving reusable prompts into a local PromptHub as Markdown files.
It classifies each prompt, writes category metadata, and updates a prompt index.

## What It Includes

- `SKILL.md`: Codex skill instructions and save workflow.
- `scripts/save_prompt.py`: CLI helper that writes prompt files and updates the index.
- `references/classification.md`: Category definitions and classification rules.
- `agents/openai.yaml`: Skill display metadata.

## Default Storage

By default, saved prompts go to:

```text
/Users/jean/Documents/PromptHub
```

To use another PromptHub root, set `PROMPT_HUB_ROOT`:

```bash
PROMPT_HUB_ROOT="/path/to/PromptHub" python3 scripts/save_prompt.py \
  --title "Prompt title" \
  --category "writing" \
  --tags "writing,reuse,prompt" \
  --usage "Use this prompt for reusable writing workflows." \
  --rationale "The prompt produces reusable writing output." \
  --prompt-file "/path/to/prompt.txt"
```

## Local Maintenance

This directory is a Git working copy connected to:

```text
https://github.com/liuyuqing803/prompt-hub-capture
```

Typical update flow:

```bash
cd /Users/jean/Documents/PromptHub/skills/prompt-hub-capture
git status
git add .
git commit -m "Update prompt hub capture skill"
git push
```

## Install Into Codex

The installed Codex skill path on this machine is:

```text
/Users/jean/.codex/skills/prompt-hub-capture
```

After editing this repo, copy the updated files into the installed skill folder
when you want Codex to use the latest local version.
