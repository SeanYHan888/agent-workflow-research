# Course project catalog

This catalog maps work to learning outcomes. The [charter](CHARTER.md) owns workload/activation rules; Obsidian owns execution tasks, dates and evidence. A catalog entry is not an active assignment. Keep one primary module and one active project; a module's lab can supply its practical work.

## Select the next hands-on slice

Follow the [project route](../ROADMAP.md#project-route), check the current owner's evidence, and define one useful behavior with a normal case and relevant failure case. Name the milestone criterion, entry skills, focused-hour allowance and evidence owner before assignment. Lessons and labs can share an artifact; they do not create parallel project backlogs. The charter's project-first allocation keeps hands-on work inside existing hours.

For the current JS/Node restart, use these incremental choices after the diagnostic. Estimates include explanation, attempts, testing and feedback, and are planning assumptions rather than assigned tasks:

| Increment | Acceptance evidence | Initial core/lab allowance |
|---|---|---:|
| Task-file CLI | Read a tiny fixture, print a task summary, reject malformed input with an explained error | 4–6h |
| Observable fake worker | Launch a fixed harmless command; distinguish failed startup, output and nonzero exit | 5–7h |
| Controllable runner | Handle a split JSONL record, bound retained output, cancel a slow fixture and establish it stopped | 5–7h |

The combined 14–20h estimate is inside the existing 30h core/lab restart envelope, leaving 10–16h for remaining language-course work and gaps; that allowance is not proof all Boot.dev work fits. Scope only the next ready increment using observed pace. If the whole deliverable does not fit, split remaining execution work before activation and review any affected dates under the charter. Keep the current JS/Node owner, task states and explicit resource-completion goals. The terminal pilot retains its own project allowance.

Later rows are families to split using the same rule, not a sequence of oversized execution projects.

## Existing project mappings

| Project or project family | Role and milestone | Entry and bounded outcome | Progress owner |
|---|---|---|---|
| Tool-cycle orientation | Core M1 | Trace execution and change a dispatcher; preserve demonstrated September 13 evidence | Archived agent loop |
| JS/Node runner | Core M2 | Relevant JS basics → task-file runner, output and failure handling | JS/Node |
| Engineering delivery/recovery lab | Required M11, introduced with M2 and practiced through M3/M4 | Read-only Git inspection first; then the [agent review/CI experiment](projects/agent-review-ci-lab.md): one bounded change, seeded defects, deterministic checks, separate review, bounded repair, acceptance and recovery; ADR where justified. Up to 6 project hours over two weeks, inside the full topic's 12–18h. | Reuse the current learning project for a short exercise; assign one owner when a separate bounded lab is activated. [Module](modules/engineering-practice.md) |
| Small typed agent | Core M3 | Language/async/process checkpoints → validated tools, bounded loop and persistence | TS agent |
| Source/extension and real-worker adapter | Core M4 | Small-agent understanding → one source trace/extension, then a bounded worker contract | Pi extension · worker adapter |
| Terminal and GUI collaboration | Required workflow outcomes | One reviewed real task, interruption/resume; later a bounded client/server ownership comparison | Terminal · GUI |
| Linux/runtime and coordination | Core M5/M7 | Single-host operation first; then durable two-worker recovery. Split overloaded scope at activation/reforecast. | Existing Linux note |
| Existing-tool team | Core M7; evidence reused in M10 | Bounded coordinated work, separate review and failed-worker recovery; not automatically the expanded capstone | Team project |
| Daily Task Panel | Elective or equivalent TS exercise | TS unions/narrowing; select a bounded slice from the [lab](projects/typescript-plugin-lab.md). Preserve agent-specific criteria. | Stage 01 |

These links preserve existing ownership; they do not imply unchanged old scopes satisfy every new milestone. Map evidence and explicitly add missing criteria during the approved reforecast. No new completion is recorded by this catalog.

## Required systems project families — September 30, 2026

[Systems module](modules/systems-foundations.md) owns criteria and teaching-block estimates. Each implementation slice below is at most 6–9 project hours (two or three project weeks), with theory charged to the primary module. Split again if the entry diagnostic shows this is too small. No new dates or active projects are created by this catalog.

| Family | Small independently useful deliverable | Ownership and reuse |
|---|---|---|
| M12 compiler | Separately: expression parser; scope/type checker; evaluator; bytecode expressions; branch/call-frame extension; one optimization; tiny backend experiment | Assign only the next owner at activation. Optional existing Rust CLI can demonstrate part of R1; do not duplicate its tasks or treat it as all of M12. |
| M5 OS/network/security | One process/pipe diagnosis; one memory/synchronization experiment; framed socket service; packet/failure report; one access-boundary verification | Existing Linux/coordination note retains ownership until an authorized split. Its old 30h envelope cannot contain the expanded M5/M7 scope. |
| M7 storage | Append-log KV fixture and, separately, crash/torn-record recovery; transaction-history comparison | Assign a bounded owner at activation; reuse the N1 protocol fixture and M7 failure histories where appropriate. No production database rewrite required. |
| Python extensions / embedded | A later measured native-extension or simulated device experiment | Electives only, with their own scope/time decision; no required hours or activation. |

## Required foundation project families — September 30, 2026

[M13–M15](modules/core-foundations.md) add independently assessable foundations. At activation select only one bounded slice: M13 small ALU/instruction simulator or cache/object-file report; M14 a hash table/heap, dependency-graph analyzer or DP comparison; M15 a proof/counterexample portfolio with a bounded protocol or probability simulation. Each practical slice uses at most 6–9 project hours and at most 21 days; instruction is separately charged within the milestone. Reuse compiler/worker/store fixtures and existing valid evidence. Larger scopes must split; do not assign three simultaneous projects. No new execution owner or date is created here.

## Programming paradigms and design — required M16

Use [one bounded task-lifecycle/retry-policy component](modules/programming-paradigms.md) for both functional and object-oriented designs. Separate practical slices: one variant with fixtures; the other against the same contract; then a small Rust transfer and change comparison. Each slice is at most 6–9 project hours and 21 days at actual capacity; P1–P4 already include this effort. Reuse the current learning owner or create only the next bounded owner on activation. No new active project, schedule or completed exercise is implied.

## Options awaiting activation

| Option | Course fit | Smallest next deliverable | Status |
|---|---|---|---|
| VPS lab | M5, preparatory M2 exploration | [Imported VPS roadmap](projects/vps-lab-roadmap.md), using prior Oracle/Tailscale/Herdr context; I001 exploration then a bounded remote-service slice | Existing VPS tasks belong to the Linux project above; The old VPS plan is stopped and its Oracle monitor deleted; wait for replacement-host details. [VPS operations and recommendations](../operations/vps/README.md) now live here; reuse or explicitly split course task ownership during reforecast. |
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

## Agentic Linux project family — October 4, 2026

The [M17 course](modules/agentic-linux.md) and [M10 distribution brief](projects/agentic-linux-distribution.md) define the required outcomes. The [project folder and M1–M17 map](projects/agentic-linux-distribution/README.md) connect existing projects to the six goals. Prefer the current runner, agent and service as the evolving product. The whole distribution is a long-term direction; each execution slice needs its own owner at activation.

| Slice | Budget and useful result | Ownership |
|---|---|---|
| T1 request/source trace | Existing M4 GUI allocation; one explained request path | Existing GUI note above; preserve its tasks and evidence. |
| T2 Linux service | 6–9h; observed lifecycle, denied action and recovery | New bounded owner at activation; reuse M5 foundations. |
| Q1 Quattro trace | 6–9h; one explained desktop-to-OS action | New bounded owner at activation. |
| Q2 reversible extension | 6–9h; one tested change and removal/recovery | New bounded owner after Q1. |
| C1 comparison | 6–9h; design decision, target user and release boundary | New bounded owner; reused by M10. |
| M10 distribution | Separate bootable baseline, integration, update/recovery, evaluation and release slices | See the release brief. Each project uses at most 6–9 project hours across 21 days; any additional lesson time is explicitly allocated from core study. |

The existing team project supplies bounded coordination evidence. It is not the owner of the entire distribution. No new tasks, dates or completion are implied by this catalog.

## Agent Skills — required M18, October 16, 2026

The [M18 brief](modules/agent-skills.md) adds one learner-authored workflow with baseline comparison and maintenance evidence. Reuse the existing 智能体指令与技能试验 for an appropriate first slice: live status `later`, no dates, three-hour minimal trial, read October 16. Do not expand that trial silently to the full 12–18h course. Subsequent bounded slices are authoring with fixtures and, separately, evaluation/transfer. Each uses at most 6–9 project hours and fits 21 days at actual capacity; teaching hours come from the primary module allocation. Record shared effort once and choose only the next owner at activation. No new execution checklist or active project is created here.

## Model Context Protocol — required M19, October 17, 2026

The [M19 brief](modules/mcp.md) adds one learner-built MCP server over the runner, a two-host comparison and boundary experiments. No Obsidian owner exists yet; create or select one at activation. The natural first slice is MC2 (server with fixtures and tests); MC3/MC4 can form a second. Each uses at most 6–9 project hours and fits 21 days at actual capacity; teaching hours come from the primary module allocation. Count shared runner, M4 Pi trace and M18 evaluation work once. No execution checklist, active project, installation or remote endpoint is created here.
