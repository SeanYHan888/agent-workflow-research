---
type: project
status: later
area: tools
start: 2026-09-30
deadline: 2026-10-13
outcome: Complete and review one real task using a persistent terminal agent session, including interruption and resume.
created: 2026-09-09
tags:
  - project-file
order: 10
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 0
---
# Terminal — Human in the Loop: one real task

**Planned window:** September 30–October 13, 2026 (two weeks). **Effort budget:** about four focused hours, drawn from the existing ten hours/week study budget. These are planning targets, not an external deadline or proof that work has started.

## Project goal:

Use a terminal coding agent as a practical assistant: I choose a small task, provide direction when needed, inspect the changes and checks, and decide whether the result is acceptable. Herdr keeps the terminal session available; Pi is the initial agent to trial. This project uses existing tools rather than building a new agent or coordinator.

## Done when:

- One bounded real task has an agreed output and a reviewed result, with the relevant checks recorded.
- I can detach and reattach the Herdr session while the host remains available, and explain what this does and does not preserve.
- I have tried interrupting and resuming the agent task and recorded any limitations.
- I have a short repeatable routine and a decision about whether to keep this workflow.

## Start here:

Start on the planned date, September 30, with a 30–45 minute session: choose one small task in a designated practice checkout, define its expected result, and open or verify a named Herdr session. Use the existing HERDR.md guide. Full JS/TS study is not a prerequisite for operating and reviewing an existing tool.

Use about two hours per week for this pilot, within the shared study budget. Continue JS/Node in its own project; reassess its existing target against actual progress rather than silently adding study hours.

## Tasks:

- [ ] Choose one small real task and write its acceptance criteria before agent execution
- [ ] Validate Herdr as the terminal session layer for the Pi workflow
    - [ ] Practice named-session detach/reattach and pane controls using the existing HERDR.md guide
    - [ ] Run the first Pi task inside Herdr; verify session continuity after detach/reattach
- [ ] Validate Pi on the chosen real task
    - [ ] Verify Pi setup, available model and credentials; start with the existing Pi/DeepSeek plan if usable
    - [ ] Test tool use, interruption, and session resume; record result and review effort
- [ ] Review the resulting diff and relevant checks; record the outcome, limits and a short daily-use routine

## Decisions and blockers:

- 2026-09-24: User requires every execution project to fit within three weeks. The old December 9 deadline described a whole learning track and is replaced by this bounded two-week pilot.
- A setup problem is a blocker to record and resolve within scope, not a reason to expand this into months of platform development. If remaining work will exceed three weeks, split it into a separate project with its own outcome.
- Herdr continuity while the host remains available is distinct from recovery after host restart. Linux services, VPS deployment and multi-worker coordination belong to later projects.
- No new learning or practical task was marked complete during this restructuring.

## Follow-on projects:

- [[Projects/Active/agent-magpie-trial|Magpie fit trial]] — one week when activated; currently unfinished.
- [[Projects/Active/agent-harness-instructions|Harness instructions and skills trial]] — one week when activated.
- [[Projects/Active/agent-rust-first-cli|Rust first CLI]] — two weeks when activated; optional and later.
- [[Projects/Active/terminal-agent-05-worker-adapter|Worker adapter]] owns the later optional Effect comparison.
- [[Notes/Coding Agent Course/00 Start Here|Course roadmap]] owns the longer path; the JS/TS, Pi, worker and Linux section projects retain their separate tasks.

## Completed setup — original records preserved

- [x] config herdr, claude code (remote access), cmux, t3 code ✅ 2026-09-09
- [x] change key bilnding for ghosty and cmux, also check if there is anyuse like super key for right three function keys ✅ 2026-09-09
- [x] 管理下ssh的instance，codex，vscode ✅ 2026-08-22
- [x] herdr 和 claude code，彻底摆脱cc desktop这个大屎坑 ✅ 2026-09-09

## Progress log:

- 2026-09-26: At the user’s request, shifted the planned start and target finish / deadline four days later (2026-09-26–2026-10-09 → 2026-09-30–2026-10-13) while they work on another project. Duration, effort allocation, task states and completion records are unchanged. Used the current project properties as the baseline; the body still showed the older September 24–October 7 window and is now aligned with the properties.

## Resources:

- [[Notes/Coding Agent Course/05 Terminal Workflow History|Earlier plans, decisions and source links]]
- [[Notes/Coding Agent Course/04 Tools and Progress|Tool map and progress ownership]]
- Local practice repository: `/Users/seanmacbook/Projects/agent-workflow-research`; consult its HERDR.md guide before the first session.
- [[Indexes/System/Project Workflow#Project size: maximum three weeks|Project sizing rule]]
