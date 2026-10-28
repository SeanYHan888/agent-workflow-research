# How Claude Code writes and edits files

Role: dated implementation-interface investigation, not a course assignment or evidence of learner mastery. Investigated October 16, 2026, to answer whether a coding agent generates patches itself or calls another coding tool/model.

## Answer and evidence boundary

Claude Code's documented workflow has the Claude model choose actions and produce tool calls; its surrounding harness executes file operations and returns results. Reading, editing, running tests and revising form a feedback loop. Thus an `Edit` call is a concrete file operation, not inherently a request for a second model to invent the code. This conclusion follows the documented model/tool separation; it is not a claim that every feature of Claude Code runs without other model calls. [Anthropic architecture guide](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop)

The public `anthropics/claude-code` repository was inspected at commit `c017428c8c27e604840435048d5bce6a9a22c040` (October 16). Its tree contains plugins, examples and support scripts, but does not provide the core Edit/Write implementation. Its license reserves rights and refers to Anthropic's commercial terms. Therefore this note distinguishes published interfaces and documented behavior from unavailable implementation details. No leaked source or private repository was used. [Pinned repository](https://github.com/anthropics/claude-code/tree/c017428c8c27e604840435048d5bce6a9a22c040), [license](https://github.com/anthropics/claude-code/blob/c017428c8c27e604840435048d5bce6a9a22c040/LICENSE.md)

## What the distributed declarations establish

Inspected `sdk-tools.d.ts` directly from the official npm package `@anthropic-ai/claude-agent-sdk@0.3.302`, without installing or executing it. Relevant declarations:

| Tool | Input fields inspected | Declaration lines |
|---|---|---|
| `Edit` / `FileEditInput` | `file_path`, `old_string`, `new_string`, optional `replace_all` | 864–881 |
| `Write` / `FileWriteInput` | `file_path`, `content` | 904–913 |
| `Bash` / `BashInput` | `command`, optional timeout, description and background execution options | 814 onward |

The edit interface supplies replacement text directly; the write interface supplies file contents directly. Neither asks for a natural-language coding assignment to be delegated to a separate generator. These are type declarations, not the file-operation bodies. [Versioned declarations](https://unpkg.com/@anthropic-ai/claude-agent-sdk@0.3.302/sdk-tools.d.ts), [official package archive](https://registry.npmjs.org/@anthropic-ai/claude-agent-sdk/-/claude-agent-sdk-0.3.302.tgz)

For example, an illustrative call would be:

```json
{
  "file_path": "/workspace/calculator.py",
  "old_string": "return a - b",
  "new_string": "return a + b",
  "replace_all": false
}
```

The model has already supplied the intended new code in this argument. This example was not executed.

## Documented behavior and checks

`Edit` uses exact text matching, including whitespace, rather than regex or fuzzy matching. The old text must identify one occurrence unless `replace_all` is true. A failed or ambiguous match requires a revised edit. `Write` replaces the complete file or creates it; it does not merge or append. `Bash` executes shell commands and can support tests or scripted changes. [Tool reference](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)

Read-before-edit is not universally mandatory in current versions. From v2.1.208, newer models can edit unread or subsequently changed files under documented read-access and matching conditions; older models retain stricter requirements. Write's equivalent relaxation arrived in v2.1.228. Consequently, older descriptions saying every edit always requires a prior `Read` are incomplete. These are documented validation rules, not rules independently tested here. [Edit checks](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior), [Write checks](https://code.claude.com/docs/en/tools-reference#write-tool-behavior)

## Verification limits

The public repository tree, license and distributed declarations were inspected directly. Official documentation supplies runtime semantics. No Claude session was started, model invocation made, package installed, or edit behavior benchmarked. The observed interfaces support comparing Claude's replacement operations with Codex's patch interface; they do not establish internal write atomicity, implementation algorithms or relative reliability. Documentation and package versions can change, so recheck before depending on these details.
