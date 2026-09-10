# Project context

This file preserves the working decisions from the Codex task **Design terminal agent workflows** (`01a0886a-08d4-7c70-9f4d-a62bc3494115`). Read this first when continuing in a new task. A readable conversation snapshot is in CHAT-HISTORY.md; it is not a native Codex history import.

## Location and user preference

Project root: `/Users/seanmacbook/Projects/agent-workflow-research`.
The user reserves Documents for personal information. Keep this project and its new artifacts in Projects. The directory was moved from Documents on 2026-09-09; five files were verified byte-for-byte before updating embedded paths.

## Objective

Develop two personal coding-agent workflows:
1. Human-in-the-loop, single active harness per task: Ghostty or cmux, Herdr, Claude Code/Codex/Pi, optional Paseo GUI/mobile.
2. Later: larger delegated work with human review, evaluating OMP and Orca.

The user wants concrete app boundaries, use cases, and hands-on instruction, not vague recommendations. Current priority is workflow 1, specifically learning and configuring Ghostty and cmux before proceeding to Herdr and harness integration.

## Agreed working model

- Ghostty and cmux are alternative terminal interfaces. cmux additionally supplies a project sidebar, browser, and notifications.
- Herdr manages persistent CLI terminals; the harness manages its conversation and tools.
- One writer and one session owner per task. Switching harnesses uses code plus explicit task notes.
- Paseo is an alternative GUI/mobile session owner; seamless takeover of Herdr sessions is unverified.
- OMP is a separate Pi-derived harness, so keeping it with Claude Code, Codex, and Pi means four harnesses. Defer that choice.

## Verified local setup

Installed versions checked in this conversation: Ghostty 1.3.1, cmux 0.64.22, Herdr 0.8.0, Claude Code 2.1.237, Codex CLI 0.147.0. Pi was not found on the shell PATH. Recheck before version-dependent changes.

Shared terminal config: `/Users/seanmacbook/Library/Application Support/com.mitchellh.ghostty/config`.
cmux config: `/Users/seanmacbook/.config/cmux/cmux.json`.
Herdr config: `/Users/seanmacbook/.config/herdr/config.toml` (not changed).

Changes already made:
- Ghostty: font-size 15, opaque background, padding 8, window-save-state always, inherited working directories, close confirmation.
- cmux: stable sidebar order, inherited working directories, quit confirmation, native terminal input, supported-agent auto-resume, routine hibernation off.
- Original Shift+Enter mapping and shell configuration preserved.
- Both edited configs have sibling backups ending `.20260909-194452.bak`.
- Ghostty config validation and cmux JSONC validation passed; cmux reloaded successfully.

## UI and verification boundaries

cmux has an existing research workspace that must be preserved. We added **Terminal Practice** with **Agent** and **Checks** panes. Neither contains a running coding agent. Pane navigation, zoom/restore, and reading hello.txt were visually verified. Directory references must use the new Projects path after the move.

cmux socket mode permits processes started inside cmux. External socket access was denied; no access settings were weakened. For UI operations use approved computer-use tools. Computer control explicitly denied access to Ghostty and Codex apps. Do not work around those denials with another UI automation mechanism.

No global agent hooks installed; no full quit/relaunch recovery test; no agent multiline/image input test; no macOS banner-delivery test. Ghostty UI appearance remains a manual user check.

## Continuation verification (2026-09-09)

- Saved Codex project registration is now verified by `list_projects`: `agent-workflow-research`, path `/Users/seanmacbook/Projects/agent-workflow-research`, project ID `ee9512c7-c4be-46d3-bc59-7afd0afc4489`. This task read both continuity files. CHAT-HISTORY.md remains an archive, not native imported history.
- Verified cmux Checks directory and a new tab's inherited directory use the Projects path; closed only the new idle test tab.
- Created a separate cmux **Herdr Practice** workspace with one outer terminal running `herdr --session terminal-practice`. The existing research and Terminal Practice workspaces remain present.
- Herdr 0.8.0 has two inner shells. Verified split right, H/L navigation to left, zoom/restore, right-pane directory inheritance, detach, and reattach. The left shell printed PID 85637 and in-memory marker `still-here` before and after detachment. Session is left attached for hands-on practice.
- No harness launched, hooks installed, or global config modified in this continuation. Ghostty UI and full app/server restart remain untested.
- Hands-on continuation: `terminal-practice/HERDR.md`.

## Next work (supersedes the original list below)

1. User practices the inner/outer controls in HERDR.md; manual Ghostty visual check and named-session attachment remain outstanding.
2. Configure one chosen harness and test input, interruption, notifications, and native conversation resume.
3. Test full recovery separately when existing work can be safely interrupted.

## Original next-work list (historical)

1. Register this folder as a saved Codex project in the app. Tooling could list projects but did not expose project creation or reassignment of the current task, and Codex UI control was denied. This app step is not yet complete.
2. Keep the original task history if the app supports moving this task to the saved project. Otherwise create a task there and explicitly read PROJECT-CONTEXT.md and CHAT-HISTORY.md; do not claim the archive is native imported history.
3. Finish the terminal exercises in terminal-practice/START-HERE.md.
4. Add Herdr deliberately and teach inner versus outer pane controls.
5. Configure one harness and test its actual input, notifications, and resume before adding more integrations.

No global Codex memory files were modified. This is project-local continuity context requested by the user.
