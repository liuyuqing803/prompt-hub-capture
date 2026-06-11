# Prompt Hub Capture

Agent skill for saving reusable prompts into a local PromptHub as Markdown
files. It classifies each prompt, writes category metadata, and updates a
prompt index.

This package is not tied to one agent runtime. Any agent that supports
filesystem skills with a `SKILL.md` entrypoint can install it by placing this
folder in that agent's skill directory.

## What It Includes

- `SKILL.md`: Agent skill instructions and save workflow.
- `scripts/save_prompt.py`: CLI helper that writes prompt files and updates the index.
- `references/classification.md`: Category definitions and classification rules.
- `agents/openai.yaml`: Optional OpenAI/Codex display metadata. Other agents can ignore or adapt it.

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

## Install Into Any Compatible Agent

Choose the skill directory used by your agent. For Codex this is usually
`~/.codex/skills`; for another agent, use that agent's documented skill root.

```bash
export AGENT_SKILLS_DIR="$HOME/.codex/skills"
```

Clone this repository into the agent's skill directory:

```bash
mkdir -p "$AGENT_SKILLS_DIR"
git clone https://github.com/liuyuqing803/prompt-hub-capture.git \
  "$AGENT_SKILLS_DIR/prompt-hub-capture"
```

If the folder already exists, update it instead:

```bash
cd "$AGENT_SKILLS_DIR/prompt-hub-capture"
git pull
```

Create a PromptHub folder, unless you already have one:

```bash
mkdir -p ~/Documents/PromptHub
```

If your PromptHub lives somewhere else, set `PROMPT_HUB_ROOT` before running
your agent or before using the script:

```bash
export PROMPT_HUB_ROOT="/path/to/PromptHub"
```

Then restart or reload your agent so it can discover the newly installed skill.

## Verify Installation

Run a test save into your PromptHub:

```bash
python3 "$AGENT_SKILLS_DIR/prompt-hub-capture/scripts/save_prompt.py" \
  --title "Prompt Hub Capture Test" \
  --category "agent-workflow" \
  --tags "agent,skill,test" \
  --usage "Verify that the prompt-hub-capture skill is installed." \
  --rationale "This is a temporary installation test." \
  --prompt "Save this temporary prompt to verify installation."
```

The command should print `saved_path=...` and `index_path=...`.

## Agent Compatibility

This skill expects the agent to:

- Load skill folders that contain `SKILL.md`.
- Allow the skill instructions to run a local Python script.
- Have Python 3 available on the machine.
- Have filesystem write access to the configured PromptHub root.

Agents with a different manifest format can still reuse the package by pointing
their manifest at `SKILL.md` and keeping `scripts/save_prompt.py` available.

## Maintenance

Typical update flow for maintainers:

```bash
git clone https://github.com/liuyuqing803/prompt-hub-capture.git
cd prompt-hub-capture
git status
git add .
git commit -m "Update prompt hub capture skill"
git push
```
