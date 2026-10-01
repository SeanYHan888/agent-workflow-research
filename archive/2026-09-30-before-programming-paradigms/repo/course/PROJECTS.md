# Course project catalog

This catalog maps work to learning outcomes. The [charter](CHARTER.md) owns workload/activation rules; Obsidian owns execution tasks, dates and evidence. A catalog entry is not an active assignment. Keep one primary module and one active project; a module's lab can supply its practical work.

## Existing project mappings

| Project or project family | Role and milestone | Entry and bounded outcome | Progress owner |
|---|---|---|---|
| Tool-cycle orientation | Core M1 | Trace execution and change a dispatcher; preserve demonstrated September 13 evidence | [Archived agent loop](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Archive/terminal-agent-01-agent-loop.md>) |
| JS/Node runner | Core M2 | Relevant JS basics → task-file runner, output and failure handling | [JS/Node](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-02-javascript-node.md>) |
| Engineering delivery/recovery lab | Required M11, introduced with M2 and practiced through M3/M4 | Read-only Git inspection first; later one bounded change with tests, ADR where justified, review, acceptance and recovery. Full topic 12–18h spread across modules; a hands-on delivery slice can use up to 6 project hours over two weeks. | Reuse the current learning project for a short exercise; assign one owner when a separate bounded lab is activated. [Module](modules/engineering-practice.md) |
| Small typed agent | Core M3 | Language/async/process checkpoints → validated tools, bounded loop and persistence | [TS agent](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-03-typescript-agent.md>) |
| Source/extension and real-worker adapter | Core M4 | Small-agent understanding → one source trace/extension, then a bounded worker contract | [Pi extension](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-04-pi-extension.md>) · [worker adapter](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-05-worker-adapter.md>) |
| Terminal and GUI collaboration | Required workflow outcomes | One reviewed real task, interruption/resume; later a bounded client/server ownership comparison | [Terminal](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-human-in-the-loop.md>) · [GUI](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/gui-human-in-the-loop.md>) |
| Linux/runtime and coordination | Core M5/M7 | Single-host operation first; then durable two-worker recovery. Split overloaded scope at activation/reforecast. | [Existing Linux note](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-06-linux-coordination.md>) |
| Existing-tool team | Core M7; evidence reused in M10 | Bounded coordinated work, separate review and failed-worker recovery; not automatically the expanded capstone | [Team project](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/multi-agent-human-review.md>) |
| Daily Task Panel | Elective or equivalent TS exercise | TS unions/narrowing; select a bounded slice from the [lab](projects/typescript-plugin-lab.md). Preserve agent-specific criteria. | [Stage 01](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/ts-panel-01-strict-flags.md>) |

These links preserve existing ownership; they do not imply unchanged old scopes satisfy every new milestone. Map evidence and explicitly add missing criteria during the approved reforecast. No new completion is recorded by this catalog.

## Required systems project families — September 30, 2026

[Systems module](modules/systems-foundations.md) owns criteria and teaching-block estimates. Each implementation slice below is at most 6–9 project hours (two or three project weeks), with theory charged to the primary module. Split again if the entry diagnostic shows this is too small. No new dates or active projects are created by this catalog.

| Family | Small independently useful deliverable | Ownership and reuse |
|---|---|---|
| M12 compiler | Separately: expression parser; scope/type checker; evaluator; bytecode expressions; branch/call-frame extension; one optimization; tiny backend experiment | Assign only the next owner at activation. Optional existing [Rust CLI](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/agent-rust-first-cli.md>) can demonstrate part of R1; do not duplicate its tasks or treat it as all of M12. |
| M5 OS/network/security | One process/pipe diagnosis; one memory/synchronization experiment; framed socket service; packet/failure report; one access-boundary verification | Existing Linux/coordination note retains ownership until an authorized split. Its old 30h envelope cannot contain the expanded M5/M7 scope. |
| M7 storage | Append-log KV fixture and, separately, crash/torn-record recovery; transaction-history comparison | Assign a bounded owner at activation; reuse the N1 protocol fixture and M7 failure histories where appropriate. No production database rewrite required. |
| Python extensions / embedded | A later measured native-extension or simulated device experiment | Electives only, with their own scope/time decision; no required hours or activation. |

## Required foundation project families — September 30, 2026

[M13–M15](modules/core-foundations.md) add independently assessable foundations. At activation select only one bounded slice: M13 small ALU/instruction simulator or cache/object-file report; M14 a hash table/heap, dependency-graph analyzer or DP comparison; M15 a proof/counterexample portfolio with a bounded protocol or probability simulation. Each practical slice uses at most 6–9 project hours and at most 21 days; instruction is separately charged within the milestone. Reuse compiler/worker/store fixtures and existing valid evidence. Larger scopes must split; do not assign three simultaneous projects. No new execution owner or date is created here.

## Options awaiting activation

| Option | Course fit | Smallest next deliverable | Status |
|---|---|---|---|
| VPS lab | M5, preparatory M2 exploration | [Imported VPS roadmap](projects/vps-lab-roadmap.md), using prior Oracle/Tailscale/Herdr context; I001 exploration then a bounded remote-service slice | Existing VPS tasks belong to the Linux project above; The old VPS plan is stopped and its Oracle monitor deleted; wait for replacement-host details. [VPS operations and recommendations](../operations/vps/README.md) now live here; reuse or explicitly split course task ownership during reforecast. |
| Autonomous pipeline / Listen Phirst | M4/M5/M7 applied project | One bounded job brief with verification; retain patient-first scope decision before coding | [Pipeline proposal](../research/autonomous-job-pipeline-plan.md) and [patient pilot](../research/listen-phirst-dashboard-pilot.md); no course progress owner found in inspected folders |
| Inference experiments | M6/M9 | One generation/cache experiment, then separately scoped serving/benchmark labs | Materials selected; create project owners when activated |
| RabbitMQ reliable-job lab | Required M7 B2 | Up to 6h / two project weeks: two workers, confirms/acks, bounded retries, crash/duplicate effect checks | [Broker module](modules/message-brokers.md); unscheduled, owner assigned at activation; no duplicate Linux tasks |
| Kafka lifecycle/replay lab | Required M7 B3 | Separate up to 6h / two project weeks: independent groups, retained replay, offset/crash behavior and projection checks | Runs after the prior lab, using one active project slot; no cluster purchase implied |
| Kubernetes deployment | M8 | One understood service deployment and recovery demonstration | Prerequisites and lab environment pending |
| Stanford-inspired workflow/agent comparison | M3/M4 selected practice | Up to 6h: compare the existing agent with a simple workflow on a public/synthetic fixture; traces, errors and design defense | [University integration](../materials/university-course-integration.md); use the current learner artifact and owner, not a parallel harness project |
| Stanford-inspired evaluation slice | M4/M10 selected practice | Up to 6h: held-out cases, scoring, repeated trials and error analysis on the same artifact | May replace equivalent planned evaluation work; dates/owner checked at activation |
| MIT original Go lab route | Optional deeper M7 implementation | Diagnose Go readiness; then scope independently reviewable parts from an original lab | [MIT research](../research/mit-65840-course-fit.md); full labs may exceed a project slot and require splitting/reforecast, not automatic activation |
| Distributed capstone | M10 | Design brief first; implementation divided into bounded delivery projects | No calendar commitment or paid infrastructure selected |

## Brief required for an activated project

Name its milestone or elective purpose; entry evidence; one independently useful deliverable; in/out scope; acceptance cases; estimated focused hours; allocated weekly hours; affected work; existing/new Obsidian owner; resource and external-action constraints. Keep execution checkboxes only in that owner. At three hours/week, a 12–15-hour elective needs smaller slices or an explicitly reallocated budget to fit the 21-day rule.

Projects can change with the course. Revise the brief and milestone mapping, retain valid evidence, and use the charter's change review when required outcomes or agreed deadlines would change. Do not quietly turn an optional product deliverable into a graduation requirement.
