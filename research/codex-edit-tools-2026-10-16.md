# How Codex applies code edits

Inspected October 16, 2026 (America/Los_Angeles). This is implementation research, not a course assignment or evidence of learner mastery.

## Finding

The model generates the replacement code as part of its tool-call output. Codex's `apply_patch` implementation parses that output, checks it against the filesystem and permission policy, applies the changes, and returns results. The patch application itself is ordinary Rust logic, not another coding model. Shell tools provide a separate route for generators, formatters and scripted edits.

This investigation downloaded and read selected public source directories at commit [`e16b631d08cdf82773831f9bbfb793da687d5299`](https://github.com/openai/codex/tree/e16b631d08cdf82773831f9bbfb793da687d5299). It did not compile or execute that checkout. The installed CLI symlink points to version 0.162.1; neither that binary nor the desktop application's exact build was established as matching this source revision.

## Source trace

All links below are pinned to the inspected revision.

1. **Register the editor.** [`spec_plan.rs`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/spec_plan.rs#L1408) registers `ApplyPatchHandler` when the model metadata enables the patch tool. This means availability is configuration dependent.
2. **Describe its input.** [`apply_patch_spec.rs`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/handlers/apply_patch_spec.rs#L9) creates a freeform tool named `apply_patch` with a Lark grammar. The direct tool receives patch text, not a JSON edit object.
3. **Parse and verify.** [`ApplyPatchHandler::handle_call`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/handlers/apply_patch.rs#L302) extracts the custom input, calls `parse_patch`, resolves the target environment, and calls `verify_apply_patch_args`. Invalid input produces an error for the model.
4. **Apply policy and execute.** [`execute_verified_patch`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/handlers/apply_patch.rs#L481) prepares file permissions and approval requirements, emits change events, and invokes the tool orchestrator with `ApplyPatchRuntime`.
5. **Run the patch algorithm.** [`ApplyPatchRuntime::run`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/runtimes/apply_patch.rs#L181) calls `codex_apply_patch::apply_patch_with_options` against the selected environment's filesystem and sandbox context.
6. **Write the files.** [`apply_hunks_to_files`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/apply-patch/src/lib.rs#L438) handles add/delete/update operations; updates derive the new contents from chunks before calling filesystem methods such as `write_file`. Moves write the destination and remove the source. The runtime returns output and committed-change information.

## Input example

Illustrative tool input, not an edit performed during this investigation:

```diff
*** Begin Patch
*** Update File: app.py
@@
-timeout = 10
+timeout = 30
*** End Patch
```

The parser also supports adding files, deleting files, and an optional move destination on updates. This is Codex's own patch grammar; it is not simply a call to `git apply`. See [`parser.rs`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/apply-patch/src/parser.rs#L1).

## Details that matter

- Context matching is deterministic but tolerant: [`seek_sequence.rs`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/apply-patch/src/seek_sequence.rs#L12) tries exact matching, trailing-whitespace trimming, trimming both ends, then normalization of selected Unicode punctuation and spaces. It does not ask an LLM to repair a mismatched hunk.
- A shell-shaped `apply_patch` invocation can be intercepted and routed through the same verified patch executor. See [`intercept_apply_patch`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/handlers/apply_patch.rs#L435). Thus seeing a shell tool in a transcript does not necessarily mean the editing mechanism differs.
- Not every edit must use this tool. One bundled model prompt explicitly permits scripts for bulk replacement and generators/formatters for generated changes; other bundled prompts are stricter. See [`gpt_5_codex_prompt.md`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/gpt_5_codex_prompt.md#L11). These are model-specific prompt examples, not proof of this desktop session's exact prompt.
- A multi-file patch is not guaranteed to roll back as one transaction. The runtime records committed changes even when a later operation fails. See [`apply_patch.rs`](https://github.com/openai/codex/blob/e16b631d08cdf82773831f9bbfb793da687d5299/codex-rs/core/src/tools/runtimes/apply_patch.rs#L213).
- The OpenAI Responses API's built-in `apply_patch` interface is related but has a different API envelope: applications receive operations and return their results. Do not conflate that API schema with the CLI's freeform tool. See [official OpenAI documentation](https://developers.openai.com/api/docs/guides/tools-apply-patch).

## Claude Code comparison

See the companion [Claude Code investigation](claude-code-edit-tools-2026-10-16.md) for the separately verified public interfaces and source-availability limits. The key comparison is patch text in Codex versus `Edit` old/new strings and `Write` full content in Claude Code. Both interfaces carry code already generated by the model; they are not, by themselves, a request to a second coding model.
