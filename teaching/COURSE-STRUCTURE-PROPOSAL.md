# Accepted course structure proposal — historical review copy

Accepted September 28, 2026 with explicit adaptability and the VPS idea. Implementation is now governed by [the charter](../course/CHARTER.md) and [roadmap](../ROADMAP.md). The proposal text below records what was reviewed; its pending-review language is historical.

Status: proposed organization following two confirmed interview rounds on September 28, 2026. This is a reviewable design, not an adopted schedule or evidence of learner completion. Confirmed policies are in [DECISIONS.md](DECISIONS.md).

## Course contract already agreed

Design, build, evaluate and operate reliable distributed AI agent systems, and explain the model-serving layer they depend on. The core includes programming and agent internals, operating systems/Linux, networks/VPS operations, containers/Kubernetes, model inference/serving and distributed systems.

Budget: 15 focused hours/week, normally 10 core study/labs, 3 project work and 2 exploration. Assessments count inside the budget. One primary learning module and one active project; a lab within the module is not automatically another project. A course project can implement the module's mechanism, with each hour counted once.

The teacher maintains the core and defines milestone requirements. The student may request additions. Routine ordering and equivalent substitutions are delegated to the teacher; new required milestones, changed core outcomes and agreed milestone deadline changes need student agreement.

## Proposed stages and milestone boundaries

IDs below are proposed destinations, not an assertion that every row is one three-week project. The live vault's project policy requires each execution project to have an independently finishable deliverable within 21 calendar days at available capacity; larger milestones use several projects. Unscheduled follow-ons keep dates blank.

| Stage | Milestone | Boundary and demonstration |
|---|---|---|
| I. Foundations | M1. Explain and implement an agent tool cycle | Model output versus harness execution; messages, validation, stop conditions and failures. Preserve the existing Section 1 evidence rather than assigning it again. |
| I. Foundations | M2. Write and control a program | JS/TS, Node, async, errors, files, subprocesses and basic Bash/process/network literacy. Build and explain a bounded task runner. |
| I. Foundations | M3. Build a small typed agent | Provider/tool contracts, runtime validation, context, persistence, cancellation and tests. Extend the runner rather than starting several independent agents. |
| II. Reliable single-host systems | M4. Explain real harnesses and integration boundaries | Selected mini-swe-agent/Pi source, Pi extension and real-worker adapter; terminal and GUI session ownership. Retain required Codex source study with a scoped Rust reading bridge, sequenced after the smaller source traces. |
| II. Reliable single-host systems | M5. Operate an isolated service on Linux | OS processes/threads, virtual memory, files/I/O, permissions and scheduling; Linux services/logs, SSH, DNS/TCP/HTTP/TLS, routing/firewalls, VPS recovery, Docker images/volumes/networks and resource isolation. Diagnose failures before adding orchestration. |
| II. Reliable single-host systems | M6. Explain and measure model inference | Tensor/attention prerequisites, one-token generation, sampling, KV cache, prefill/decode, memory/latency accounting and single-host serving. Keep model execution distinct from the harness tool loop. |
| III. Distributed systems | M7. Coordinate durable distributed work | State ownership, queues, concurrency, idempotency, retry/backoff, leases, uncertain outcomes, consistency and recovery under partial failure. Reuse worker adapters and demonstrate worker loss and duplicate delivery. |
| III. Distributed systems | M8. Operate services with Kubernetes | Workload lifecycle, scheduling/resources, service discovery, networking, configuration/secrets, persistent state, rollout and recovery. Compare behavior with the understood single-host deployment. |
| III. Distributed systems | M9. Analyze efficient and distributed inference | Kernels, batching, KV allocation, vLLM source, quantization, speculative decoding, parallelism and interconnect costs. Use controlled benchmarks and distinguish simulated multi-device reasoning from hardware measurements. |
| IV. Integrated capstone | M10. Build and defend a distributed agent system | Join durable job coordination, isolated workers and a model-serving boundary. Demonstrate evaluation, observability, cancellation, overload and failure recovery; defend architecture and report correctness, latency, resource use and human intervention. |

This is a dependency-led route, not six simultaneous subject tracks. M5 and M6 each receive dedicated primary-module time. Detailed lessons are prepared only as their prerequisites are demonstrated. Real multi-host execution is part of the destination; host/provider and spend choices remain separate decisions when the lab is specified.

## Proposed depth and assessments

Use graduate-level applied systems depth: mechanisms, selected authoritative readings/source, derivations where relevant, controlled experiments and defended tradeoffs. OS/networking receive dedicated modules, not only command tutorials. Kernel development, complete protocol-stack implementation and model pretraining are optional specializations, not assumed core projects.

Each milestone requires (1) a working artifact or reproducible experiment, (2) the student's explanation and (3) an unfamiliar modification or diagnosis. Assess correctness, explanation, failure reasoning and evidence quality separately; all must be demonstrated. Use pass/revise with targeted retries. At advanced milestones add a short research comparison or reproduction of a bounded claim. The capstone includes a design defense and measured failure experiments.

Assistance may be used during practice; assessment questions must reveal the student's understanding. Record the assistance and remaining gaps. A useful AI-produced project can supply study material without certifying learner mastery.

## Existing commitments and additions

| Existing item | Proposed home and scheduling treatment |
|---|---|
| Foundation Sections 1–6 | Backbone of M1–M5 and M7; preserve evidence and split overloaded Linux work into bounded projects. |
| Terminal, GUI and existing-tool team workflows | Retain outcomes: terminal use throughout, bounded GUI/client-state comparison in M4, team coordination in M7 and capstone integration. Product comparisons support capabilities rather than define course progression. |
| Official Claude courses | Material mapped to agent/tool/context/delegation/API/MCP outcomes; assign relevant lessons when needed. Existing course selections stay on the shelf; completing every catalog item is not a new graduation condition. |
| Agent source expansion | Mini-swe-agent/Pi/Codex form the main source route; nanocode/Tau are focused supporting comparisons, OpenCode optional. Preserve the local Claude snapshot's unverified-provenance label. |
| Inference C1–C12 | Retain coverage, divided between M6 and M9; reliable serving contributes to M10. C13 remains specialization. |
| Autonomous pipeline / Listen Phirst pilot | Candidate applied project in the existing 3-hour slot, contributing evidence where relevant. No independent extra weekly lane and no new requirement to deliver the whole dashboard. Selecting/activating a slice requires its own bounded brief. |
| Daily Task Panel TypeScript lab | Elective application after its language entry gate. It can occupy the project slot or substitute for an equivalent bounded TS exercise; retain required agent-specific demonstrations. Preserve existing stage 01 state; later stages remain proposals. |
| Magpie, Claude Tag and GitHub automation investigations | Research/elective candidates with evidence and open questions, not adopted runtime requirements. |
| Historical plans, version checks and setup records | Preserve as dated evidence; exclude from current scheduling authority. |

## Idea intake and scheduling

Every new idea receives a short record: the student's question, related milestone, proposed role, prerequisites, smallest useful exploration, time source, outcome and revisit condition.

1. Capture the idea before planning implementation.
2. Map it to an example, equivalent exercise, project option, elective, proposed milestone or deferred/out-of-scope idea. Explain the classification.
3. Use the exploration allowance for a small investigation. For more work, identify the project slot or study work it would replace. A two-hour investigation is a timebox, not a promise to finish the idea.
4. Preserve protected outcomes. Equivalent substitution must still satisfy the original assessment.
5. Obtain agreement for a new required milestone, core-outcome change or agreed deadline change; record the impact and decision.
6. Review the idea after the investigation: integrate, continue within a bounded allocation, defer with a revisit condition, or close with findings. Capture does not promise eventual implementation.

Review allocations weekly and forecast at milestone boundaries. Maintain one authoritative calendar in Obsidian. Later milestones have prerequisite order and effort forecasts until calendar commitments are agreed. The current dated projects need an evidence-based reforecast, not an automatic shift based on the new 15-hour budget. The course's one-active-project rule also remains subject to the vault's maximum of three `now` projects across all areas.

## Proposed document structure and ownership

| Location | Owns | Does not own |
|---|---|---|
| `README.md` | Short entry point and navigation | Duplicate syllabus or progress |
| `course/CHARTER.md` | Destination, instructor/student authority, workload and idea-change rules | Daily tasks |
| `ROADMAP.md` | Current stages, milestone map, prerequisites, subsection boundaries and link to live schedule | Independent learner completion record |
| `course/ASSESSMENT.md` | Common mastery rubric, assessment method and retries | Learner answers |
| `course/PROJECTS.md` | Project briefs/options, outcomes, entry gates and links to execution projects | Duplicate task checklists |
| `course/IDEAS.md` | Idea intake, curricular disposition and rationale | A second implementation backlog |
| `materials/` | Material roles, source links, pins and selection notes | Progress inferred from downloaded sources |
| `teaching/` | Session preparation, original handouts and decision history | Overwriting personal annotations |
| `research/` | Investigations, comparisons and design proposals | Implicit new curriculum commitments |
| Obsidian reading room | Student readings and annotations | Duplicate execution tasks |
| Existing Obsidian project notes | Live schedule, tasks, status, hours and learning evidence | Unbounded umbrella courses as execution projects |
| `archive/` | Superseded plans and historical records | Current instructions |

Live vault inspection on September 28 confirms that the course overview is [Notes/Coding Agent Course/00 Start Here.md](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Notes/Coding Agent Course/00 Start Here.md>), with live project views. The former `Projects/coding-agent-course.md` no longer exists. Section 1 is archived as done with September 13 evidence; JS/Node remains active with a September 17–October 2 forecast and no newly recorded checkpoint completion. Its dates overlap the October 1 TypeScript start. These are reconciliation inputs, not evidence of failure or automatic advancement. The inference expansion is not yet reflected in the live Study Route, and no pipeline/Listen Phirst project owner was found in the inspected course/project folders; do not create one implicitly.

Keep `CONTEXT.md` as the glossary and `PROJECT-CONTEXT.md` as a concise continuation pointer. Add a short course-work pointer to repository `AGENTS.md` so future chats consult the charter, roadmap and idea policy when teaching or adding scope. Preserve its Obsidian connection instructions.

Migration: retain historical copies of replaced plans; move root investigations into `research/` and resource assessments/catalogs into `materials/`; repair affected links and preserve linked source repositories. Provide redirects where external notes may still reference old root paths. Keep learner exercise code and external project repositories in place. Reconcile outdated active-session pointers. Keep Obsidian as the existing progress owner and preserve all task states, completion evidence and personal annotations.

Implement the repository structure after approval. Inspect live Obsidian evidence and prepare a concrete calendar reforecast separately; moving existing milestone deadlines still requires the agreed review. Do not create a second schedule in the repo to avoid that review.

## Final review questions

1. Adopt the proposed applied systems/research depth and milestone map?
2. Adopt the existing-item placements and idea-intake policy, including allowing some ideas to remain deferred or outside course scope?
3. Adopt the document ownership and repository migration above, retaining Obsidian progress ownership and reviewing a concrete reforecast before changing deadlines?

An affirmative answer confirms shared understanding and authorizes the repository reorganization. It does not spend money, provision hosts, deploy systems, complete student exercises or change milestone deadlines.
