# Project context

This file preserves the working decisions from the Codex task **Design terminal agent workflows** (`01a0886a-08d4-7c70-9f4d-a62bc3494115`). Read this first when continuing in a new task. A readable conversation snapshot is in CHAT-HISTORY.md; it is not a native Codex history import.

## Location and user preference

Project root: `/Users/seanmacbook/Projects/agent-workflow-research`.
The user reserves Documents for personal information. Keep this project and its new artifacts in Projects. The directory was moved from Documents on 2026-09-09; five files were verified byte-for-byte before updating embedded paths.

## Objective

### Current course redesign — 2026-09-10

The user wants to redesign the course from outcomes and the purpose of each resource. They explicitly report that the generated `agent-learning` chapters are poorly designed, unclear, and did not help them learn. Do not use those chapters or the existing mini-agent as the syllabus or assume their correctness. Keep Tau and Pi source as valuable references.

Confirmed baseline: the user can write small Python scripts, but async, subprocesses and larger codebases are unfamiliar. No lesson completion has been demonstrated. Teach small mechanisms before introducing full async agent implementations. Use a few Python exercises for orientation, then TypeScript for the main build.

Read [ROADMAP.md](ROADMAP.md) for the redesigned sequence: one tool cycle → JS/Node process runner → small typed agent → selected Tau/Pi investigation and Pi extension → one real worker → bounded coordination and Linux recovery. Only Step 1 is active. The opening block traces a scripted file-read request, modifies a tiny tool dispatcher, then locates that mechanism in actual source. Expand lessons interactively; do not generate the entire course or implement the learner's exercises upfront.

The five goals remain: a useful terminal workflow; agent construction through Tau/Pi/Claude Code; Obsidian progress tracking; Boot.dev JS/TS; Bash/Linux. Initial workflow hypothesis: cmux or Ghostty → Herdr → Pi with DeepSeek V4.1 Flash → Claude Code/Codex workers. Actual daily harness use can begin alongside learning. DeepSeek fit and delegation remain unverified. Herdr terminal persistence is distinct from conversation/task recovery. Pi source exists; its executable was not on the inspected PATH earlier September 10.

Resource roles: Boot.dev teaches languages; YDKJS supplies selected depth; Node docs/labs bridge languages to processes; YSAP teaches Bash; LFS101 supplies Linux foundations with focused operational labs. System Design Primer supplies tradeoffs, System Design 101 visual reinforcement, and the SDE interview roadmap optional references. Effect is a later comparison after an understood plain-TS adapter. The third-party learn-claude-code repo is not Anthropic's internal source; select chapters by mechanism rather than requiring all seventeen current chapters.

The user confirmed **10 focused hours/week** when requesting the consolidated roadmap. Current planning estimate: **230–330 hours / 23–33 weeks**, working allocation **280 hours / 28 weeks** including reserve. First full week September 14, 2026; working finish March 28, 2027, range February 21–May 2. Stage targets: loop Sep 20; JS/Node runner Nov 8; typed agent Dec 27; Pi extension Jan 17; first worker Feb 14; full coordination/Linux Mar 28. These are provisional estimates, not learning evidence. Review actual pace September 27 and revise. Full Boot.dev JS/TS plus selected Node/Bash/Linux/design/source work are included; exhaustive books/certificates and Effect are excluded. The earlier April 11 forecast is historical in archive/2026-09-10-before-course-redesign/.

Progress belongs in the six section projects linked by `/Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-human-in-the-loop.md`; that note is now the overview. Preserve completed tasks and the exact `## Tasks:` heading. Materials present, studied, and demonstrated are different states. The separate setup-matt-pocock-skills draft remains pending final review; default triage labels were confirmed but applying that setup was not approved.

### Obsidian split into dated section projects — 2026-09-10

The user explicitly requested multiple Obsidian project notes labeled with start and finish/deadline dates. Six notes now exist under Projects/Active: terminal-agent-01-agent-loop (2026-09-14–2026-09-20, now), terminal-agent-02-javascript-node (2026-09-21–2026-11-08, next), terminal-agent-03-typescript-agent (2026-11-09–2026-12-27, later), terminal-agent-04-pi-extension (2026-12-28–2027-01-17, later), terminal-agent-05-worker-adapter (2027-01-18–2027-02-14, later), terminal-agent-06-linux-coordination (2027-02-15–2027-03-28, later).

Each note uses type: project, start_date, deadline, existing project-file tag and exact Tasks: heading, with goal, evidence, resources and progress log. Dates are planned targets, not actual completion. Main terminal-human-in-the-loop.md remains the overview (order -1), with the shared early Herdr/Pi tasks, optional setup and all completed historical records. The 46 pre-existing tasks were conserved exactly once across seven notes; one previously implicit Pi-extension task was added. Update tasks in their owning section, not by recreating a complete checklist in the overview. Original snapshot and ownership audit: archive/2026-09-10-project-split/. Other vault projects, project templates and global plugin settings were not changed.

### Immediate study workflow — 2026-09-10

The user asked what to do now and how to follow Obsidian tasks. Teach through short guided sessions plus narrow source readings, not bulk generated chapters. Today's 30–45-minute assignment: explain model request vs harness execution, read only current learn-claude-code s01 `agent_loop()` (lines 87–117), trace the message/result flow, and answer who executes, what changes, and what stops this example. No API call/install is needed. Review the learner's answers before the tiny Python dispatcher exercise. A separate Boot.dev JS session starts at Variables. Obsidian now has an explicit task queue and ordered task groups; parent tasks span stages and are not meant to be completed wholesale in sequence. No learning completion is recorded.

### Node.js material added — 2026-09-10

The user explicitly requested Node.js material. Required sources are official Node.js Learn (short explanations) and API docs (implementation details); the resource catalog contains selected readings and project checkpoints. Step 2 covers CLI/environment, files, async I/O and a fake-worker subprocess runner; streaming/cancellation are revisited for Step 5's real adapter and Step 6's Linux process-tree cleanup. Begin after the relevant JS prerequisites, not after completing all TS. The active Step 1, provisional schedule and existing runtime/package-manager setup remain unchanged. No Node exercise has been completed by this addition.

### Material and Herdr refresh — 2026-09-10

All six local material repositories now match their fetched upstream default branches; full before/after evidence is in [material-versions.md](material-versions.md). Tau source package 0.4.2, Pi coding-agent source package 0.85.1. learn-claude-code now has 17 current chapters, not the previously inspected 20. Recheck source details and chapter numbering before lessons; dependencies/executables were not installed by these Git updates.

Herdr client was already 0.9.0. The named terminal-practice server was 0.8.0; user explicitly approved stopping its processes and restarting it. It now runs 0.9.0 with compatible protocol 22 and no restart required. State/config backup: /tmp/herdr-terminal-practice-before-0.9.0. Started headlessly; attach with `herdr --session terminal-practice`. Earlier 0.8.0 shell markers/PIDs below are historical and no longer live. Other sessions/remote hosts were not restarted. UI/layout restoration remains unverified.

### Previous scope — retained for context

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

Historical initial versions (Herdr superseded by the refresh above): Ghostty 1.3.1, cmux 0.64.22, Herdr 0.8.0, Claude Code 2.1.237, Codex CLI 0.147.0. Pi was not found on the shell PATH. Recheck before version-dependent changes.

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
