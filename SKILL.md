---
name: prompt-hub-capture
description: Save, classify, and index long prompts into the user's local Prompt Hub. Use when the user gives a reusable prompt and asks to save, archive, collect, classify, organize, store in PromptHub, put in the local prompt hub, or keep it for future reuse.
---

# Prompt Hub Capture

## Overview

Use this skill to save reusable prompts into the user's local PromptHub as Markdown files with category metadata, tags, usage notes, and an index entry. The save script uses `$PROMPT_HUB_ROOT` when set; otherwise it defaults to `~/Documents/PromptHub`.

## Workflow

1. Identify the exact prompt text to save. If the user's message includes instructions plus the prompt, save only the reusable prompt content.
2. Create a concise title in the same language as the prompt unless the user requests otherwise.
3. Choose one primary category from the existing category list. Read `references/classification.md` when category choice is not obvious.
4. Generate 3-6 lowercase tags. Use short English tags when possible; preserve specific product or domain names.
5. Write a one- or two-sentence usage note and a short category rationale.
6. If category confidence is high, run `scripts/save_prompt.py` with the title, category, tags, usage note, category rationale, and original prompt.
7. Reply with the saved file path, category, tags, and whether the index was updated.

## Category Uncertainty

Do not force a category when confidence is low.

If uncertain, ask the user before saving:

- Show the current categories from `references/classification.md`.
- Recommend 1-2 likely categories with brief reasons.
- Ask whether to use one of them or add a new category.

If the user wants a new category:

- Suggest a lowercase hyphen-case English directory name.
- Wait for user confirmation before creating the category directory or saving the prompt there.
- After confirmation, add the category to `references/classification.md` before saving.

Use `uncategorized` only when the user explicitly asks to save without deciding now.

## Save Command

Use the bundled script from the installed skill directory:

```bash
python3 ~/.codex/skills/prompt-hub-capture/scripts/save_prompt.py \
  --title "Prompt title" \
  --category "product" \
  --tags "prd,ai-tutor,product-design" \
  --usage "Use this prompt to draft a product requirement document." \
  --rationale "The main use case is product requirements and page design." \
  --prompt-file "/path/to/temp-prompt.txt"
```

Prefer `--prompt-file` for long prompt text to avoid shell quoting issues.

If the user's PromptHub is not under `~/Documents/PromptHub`, run the same command with `PROMPT_HUB_ROOT=/path/to/PromptHub`.

## Output Format

After saving, respond briefly:

- Saved path
- Category
- Tags
- Index path
- Any follow-up needed, such as category confirmation

Do not rewrite or optimize the prompt unless the user explicitly asks.
