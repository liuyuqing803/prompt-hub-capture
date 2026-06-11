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
~/Documents/PromptHub
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

## Install Directly From GitHub

Install the skill into Codex's local skill folder:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/liuyuqing803/prompt-hub-capture.git \
  ~/.codex/skills/prompt-hub-capture
```

If the folder already exists, update it instead:

```bash
cd ~/.codex/skills/prompt-hub-capture
git pull
```

Create a PromptHub folder, unless you already have one:

```bash
mkdir -p ~/Documents/PromptHub
```

If your PromptHub lives somewhere else, set `PROMPT_HUB_ROOT` before running
Codex or before using the script:

```bash
export PROMPT_HUB_ROOT="/path/to/PromptHub"
```

Then restart Codex so it can discover the newly installed skill.

## Verify Installation

Run a test save into your PromptHub:

```bash
python3 ~/.codex/skills/prompt-hub-capture/scripts/save_prompt.py \
  --title "Prompt Hub Capture Test" \
  --category "agent-workflow" \
  --tags "codex,skill,test" \
  --usage "Verify that the prompt-hub-capture skill is installed." \
  --rationale "This is a temporary installation test." \
  --prompt "Save this temporary prompt to verify installation."
```

The command should print `saved_path=...` and `index_path=...`.

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
