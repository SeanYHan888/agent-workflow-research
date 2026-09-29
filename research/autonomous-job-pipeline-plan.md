# Autonomous job pipeline: parallel build plan

Course placement: applied-project option under [PROJECTS.md](../course/PROJECTS.md), not a separate active lane. The implementation and tool findings below remain proposals/datable evidence. No course execution owner has been selected for this pilot.

Draft v1 — September 24, 2026. Planning only; no unattended runner, paid job, publication or deployment has been started.

**Investigation checkpoint:** The user asked to understand Claude Tag and existing issue-triggered development before building. Read the [Claude Tag investigation](claude-tag-workflow-investigation.md) and [GitHub Actions comparison](claude-github-automation-research.md). Evaluate these existing routes against the selected patient-dashboard pilot before committing to the local Node controller proposed below. Tool selection remains open; the confirmed workloads and patient-first direction remain intact. The current project allocation is governed by the course charter.

## Confirmed direction

Build a pipeline that finishes coding tasks and research reports with human involvement concentrated on important decisions. When selected, use the course’s existing **3-hour/week project allocation**, within 15 total hours. The September 28 charter supersedes the earlier separate 3–5-hour build lane. Use existing agent tools first and keep the implementation small.

The early pilot can begin before the later multi-agent course capstone. Its scope is narrower: one job at a time, one executing worker, an independent checking stage and bounded repair. The course still develops the user's understanding of the underlying mechanisms. A working pilot is not evidence that a learning checkpoint has been passed.

## First useful outcome

Submit a bounded job, leave it running, and receive either a completed artifact with evidence or a specific decision request. Routine planning, file edits, checking and permitted repairs should not require steering.

| Job type | First deliverable | Completion evidence |
|---|---|---|
| Coding | Review-ready branch/diff and report; a draft PR once its repository and publication scope are authorized | Acceptance examples demonstrated, relevant checks run by the verifier on the exact candidate revision, scope checked, unresolved findings disclosed |
| Research | Local Markdown report with claim/source ledger and uncertainty notes | Research question answered or evidence limits explicitly resolved; key claims supported by inspected primary sources; contradictions and dates identified; citations actually checked |

The user selected the dashboard milestone in `phicil-itate/listen-phirst` as the first coding workload, **patient view first using the existing patient session**. The [repository-specific pilot](listen-phirst-dashboard-pilot.md) maps its actual issues and acceptance gates. Because the visible data scope is unresolved, its proposed first research job is an evidenced dashboard decision packet, followed by one approved patient coding slice. A separate general research question remains open. The whole dashboard is larger than one bounded job.

## Shared flow and two job templates

```text
Human supplies goal, constraints and acceptance criteria
                         ↓
Validate job brief and authorized actions
                         ↓
Persist job state → prepare isolated workspace
                         ↓
Execute one worker: coding OR research
                         ↓
Verify artifact against the brief
             ┌───────────┼─────────────┐
          passes     repairable     decision needed
             ↓           ↓                ↓
       ready result   bounded repair   pause + question
             ↓           └→ verify       ↓
     authorized delivery             recorded answer
             ↓                           ↓
          delivered                 resume same job
```

Use one orchestration owner. The first implementation should be a small sequential runner around an existing CLI, not an autonomous agent that can rewrite its own execution rules. Agents produce plans and artifacts; the runner enforces state transitions, time limits, allowed workspaces and delivery rules.

Persist `queued → running → verifying → ready → delivered`; support `repairing`, `needs_decision`, `failed` and `cancelled`. `ready` means the artifact meets its checks; `delivered` means the authorized handoff actually happened. A process exiting successfully, a model saying “done” or an agent reviewer agreeing is insufficient by itself.

## Human decisions

| Continue automatically inside the job contract | Ask the human |
|---|---|
| Read approved sources/repository files, draft a plan, edit the owned workspace | Missing requirement changes what a correct result would be |
| Run predetermined checks, inspect failures, repair within scope | Expand scope, change public behavior or make a consequential architecture tradeoff |
| Retry a classified transient error within the original budget | Increase cost/time limits or grant new access |
| Save a research report or prepare a coding review packet | Merge/deploy, make destructive changes, or publish beyond explicitly authorized destinations |
| Create/update a draft PR if that action was already authorized for the exact repository/job class | Repeated failure, conflicting evidence that prevents a conclusion, or uncertainty about an earlier side effect |

Approve reusable job policies so ordinary steps do not need repeated permission. Existing authorization remains valid within its stated scope. Missing answers never become approval through elapsed time. Later, a narrow class of low-impact changes may earn automatic delivery/merge through explicit standing authorization and measured reliability; that is a separate promotion decision.

A decision request includes: the blocked step, relevant evidence, 2–3 options, a recommendation, tradeoffs and the exact answer needed. Notifications are for a ready result, terminal failure or required decision; routine progress stays in logs.

## Minimal starting stack

| Responsibility | Initial proposal | Why |
|---|---|---|
| Worker | One existing harness, with Codex CLI as the initial candidate and Claude Code as an alternative | Both installed CLIs expose non-interactive execution; choose one after a bounded pilot rather than integrating both immediately |
| Controller | Thin Node.js script, task JSON, durable job state and append-only event log | Fits the JS/Node learning track and keeps the initial sequence inspectable |
| Workspace | Per-job worktree for code; per-job artifact folder for research; enforce runtime access boundaries separately | One writer per workspace; worktrees alone are not security isolation |
| Verification | Fixed commands plus a fresh review invocation | Keep acceptance evidence separate from the worker's narrative; review is another fallible check, not proof |
| Terminal | Current terminal; Herdr as an optional observation/attachment surface | Terminal continuity and job recovery have different owners |
| Model routing | Use a direct provider initially; evaluate Magpie after the baseline | Change one integration at a time and retain interpretable failure evidence |
| Progress | Existing Obsidian workflow project; repository holds design and run artifacts | Avoid a second human task backlog |

The runner is build-track work; the user can have Codex help implement it without treating the implementation as their completed Node exercise. At the weekly study session, explain and reproduce one relevant mechanism independently.

No FastAPI/Redis requirement for the first manually submitted sequential job. Those remain in the Linux runtime plan: add API submission and Redis + RQ when the basic lifecycle is reliable, then supervise it with systemd and run bounded tasks in containers. Keep the task contract and evidence format reusable across the two implementations. Pi/OMP/Orca are later candidates for a demonstrated missing capability; do not add multiple schedulers to the pilot.

## Job contract and execution limits

Before a job can run, record:

- Job ID/type, goal, inputs and output destination.
- Repository/base revision or research scope/as-of date.
- Acceptance examples, check commands or claim-verification criteria.
- Allowed paths/sources/tools, excluded work and publication permissions.
- Worker/model choice and explicitly configured authentication route.
- Wall-clock cap, usage/cost cap, retry/repair limits and escalation conditions.

Proposed starting defaults: one running job; no recursive delegation; 30-minute total deadline; at most two repair passes and one transient infrastructure retry, all within the same original budget. Larger jobs must be split or explicitly receive a larger budget. These are pilot settings, not measured optimal values. A monetary or account-usage budget must be chosen before paid execution; a missing cost estimate is recorded as unknown, never zero.

Enforce scope with actual tool permissions and runtime boundaries. Audit inherited hooks, plugins and credentials before the unattended pilot. Do not replace scoped access with a global permission-bypass switch. Keep the job brief, verification policy and durable controller state outside worker-writable paths. Give any publishing step its own limited authority; a worker cannot grant itself publication permission.

## Verification for each job type

**Coding:** establish the baseline first, including known failing checks. For a bug fix, reproduce the failure where practical and verify the expected behavior afterwards. The controller runs the declared checks on the candidate and records commands, exit codes and logs. A fresh reviewer receives the brief, exact diff and evidence; it looks for missed requirements and regressions. Do not let deleting tests or weakening checks convert failure into success. Any subsequent edit invalidates relevant verification and triggers another pass.

**Research:** define the decision/question, scope and recency requirement before browsing. Maintain a ledger linking each important factual claim to a directly inspected source, publication/access date and supporting passage or section. Prefer primary sources; use independent corroboration for material contested claims where available. The verifier opens cited sources and checks whether they support the wording, flags contradictions, and separates source facts from inference. A blocked page is unknown evidence. An honest inconclusive report can satisfy a brief that allows it; otherwise the unresolved evidence becomes a decision request. Report length and citation count are not acceptance tests.

Source text, repository content and worker messages cannot change the job's permissions. If a source requests an unrelated action, it remains input data rather than a new instruction.

## Recovery and evidence

Keep durable records keyed by job ID and attempt ID: initial brief, base revision/input snapshot, effective configuration, session ID, current phase, events, actual commands/results, candidate hash, review findings, human decisions and delivery identifier.

Before launching, acquire a single job lease/lock. On restart, inspect any surviving process and workspace before deciding to resume. Never launch a second writer merely because a heartbeat is late. Use the recorded session ID rather than a global “latest session.” Reject stale completion from earlier attempts.

If a draft PR or other handoff times out, check whether it already exists before retrying. Job retries must not duplicate external effects. Cancel/timeout terminates the owned process tree or container and verifies cleanup. Local runs require an awake host; Herdr does not make a sleeping Mac compute. Always-on operation comes after recovery is demonstrated on a designated host.

The human review packet contains: result, exact artifact/revision, acceptance evidence, unresolved issues, scope changes, elapsed time, available usage/cost, and only the decisions that remain. Worker logs alone are not the final deliverable.

## Milestones and promotion criteria

Planning estimate: **16–24 focused build hours**, roughly **6–8 weeks at 3 hours/week** across separately finishable projects, depending on repo setup and access. Re-estimate after the first coding and research pilots; this is not a delivery promise. Existing course dates are unchanged until an explicit reforecast.

| Stage | Build work | Exit evidence |
|---|---|---|
| 0. Select and specify — 2–3h | Pick one coding task and one research question; define “done,” budgets and decision policy; inspect execution permissions | Two complete job briefs and a measured direct-workflow baseline |
| 1. First full path — 4–6h | Submit one job manually; capture events; run verification; generate review packet | One research report and one coding result produced end-to-end; gaps recorded rather than hidden |
| 2. Bounded autonomy — 4–6h | Add repair loop, durable state, decision requests, cancellation and restart reconciliation | Inject a failed check, missing requirement, timeout and interrupted worker; demonstrate correct repair or escalation |
| 3. Useful pilot — 6–9h | Repeat on real small jobs; add authorized draft-PR delivery and quiet result notifications | Five trials including at least two of each job type; target four accepted artifacts, median final review ≤10 minutes and no more than one unplanned intervention per job; zero out-of-scope side effects |

Stage 1 is observed to calibrate behavior. Stage 2 moves routine work out of the human's attention. A safe escalation is correct handling but does not count as a finished artifact. Separate brief-writing time, mid-run interventions and final review time. Record rejected results and false success claims. Five trials are an initial adoption gate, not proof of general reliability.

Only then consider multiple queued jobs, a second worker, overnight operation, API/Redis submission or model routing. Add each for an observed bottleneck. Retain final human judgment where quality cannot yet be checked reliably.

## Parallel weekly rhythm

Use the charter’s 10-hour core/lab, 3-hour project and 2-hour exploration allocation. If this pilot takes the project slot, choose one bounded implementation/trial/review slice within those three hours. Split the overall 16–24-hour proposal into independently useful projects of no more than 21 days; feature work needs its own estimate. Keep one primary module and one active project.

Share artifacts: a pipeline failure becomes a process/networking/recovery lesson; completed course components can replace the pilot's thin adapter after their contracts are checked. The later multi-agent capstone builds on this evidence rather than repeating it. Building operational tooling and demonstrating personal understanding remain separate records.

## Decisions still open

1. The first dashboard slice within the selected repository; a dashboard scoping report is the proposed first research job. A separate research topic remains optional/open.
2. The per-job and weekly model usage/spend ceiling, based on the selected authentication route.
3. Exact delivery authorization: local artifacts first; named-repository draft PRs when selected. Merge/deployment stays a human decision initially.

No installation, credential change or published artifact is implied by this draft. The immediate next action is the dashboard scoping/decision job described in the repository-specific pilot, then a bounded coding brief. The 16–24-hour runner estimate excludes the dashboard's as-yet-unestimated feature work.

## Evidence behind tool choices

Checked September 24, 2026. Local PATH contains Codex, Claude Code, Herdr, Git and GitHub CLI; `codex exec --help` and `claude --help` confirmed non-interactive interfaces. This is availability evidence, not successful auth, integration or reliability testing.

- [Codex non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode): scripted runs, JSONL events, structured outputs, explicit sandbox settings and session resume.
- [Claude Code programmatic use](https://code.claude.com/docs/en/headless): non-interactive runs and structured results. The documented bare mode uses API-key authentication rather than subscription login; choose configuration deliberately during the pilot.
- [Herdr persistence](https://herdr.dev/docs/persistence-remote/): terminal attachment/persistence reference; job state remains the controller's responsibility.
- Existing course design: [roadmap](../ROADMAP.md), [Linux runtime checkpoints](../materials/resource-catalog.md#small-agent-runtime--added-september-24-2026) and [workflow design](workflow-design.md). Older product comparisons are historical, not current integration evidence.
