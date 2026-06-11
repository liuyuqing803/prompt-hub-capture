# Prompt Hub Categories

Use one primary category per prompt. When multiple categories seem plausible, choose based on the prompt's main reusable job, not incidental keywords.

## Current Categories

| Category | Use for | Common signals |
| --- | --- | --- |
| `writing` | Writing, social posts, articles, copywriting, content creation | article, essay, WeChat, Xiaohongshu, title, hook, rewrite, tone |
| `product` | PRD, product design, requirements, user research, prototypes | PRD, feature, requirement, user story, page spec, workflow, prototype |
| `coding` | Programming, debugging, code review, engineering implementation | code, bug, repo, API, test, refactor, implementation, stack trace |
| `data-analysis` | Spreadsheets, CSV/Excel analysis, metrics, dashboards, reports | Excel, CSV, KPI, chart, dashboard, analysis, report, cohort |
| `agent-workflow` | Agent workflows, automation, tool use, multi-step AI procedures | agent, workflow, tool, automation, skill, prompt chain, MCP |
| `business` | Business analysis, operations, sales, strategy, market analysis | sales, ops, strategy, revenue, competitor, customer, business model |
| `uncategorized` | Temporary holding area when the user explicitly postpones classification | unsure, decide later, temporary |

## Decision Rules

- Prefer the category that describes the prompt's intended output.
- Prefer `agent-workflow` when the prompt is about how an AI agent should operate across steps or tools.
- Prefer `product` when the prompt creates specs, product decisions, page flows, or requirements.
- Prefer `writing` when the prompt's final artifact is publishable text or content.
- Prefer `data-analysis` when the prompt depends on tabular data, metrics, or visualized findings.
- Prefer `coding` when the prompt asks for code changes, debugging, tests, architecture, or review.
- Prefer `business` when the prompt frames commercial decisions, operations, sales, or strategy.

## Low Confidence Handling

Ask the user before saving when:

- Two or more categories are equally plausible.
- The prompt is mostly meta-instructions without a clear domain.
- The prompt introduces a domain not covered by current categories.
- A new durable category may be more useful than forcing an existing one.

When asking, show:

1. The current category list.
2. The 1-2 recommended categories with reasons.
3. The option to add a new category.

If the user adds a new category, propose a lowercase hyphen-case English folder name first and wait for confirmation.
