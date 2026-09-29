# MIT 6.5840 and Stanford CS329Z — course integration

Adopted September 28, 2026 in response to the student's request to add both courses. These are selected required materials and adapted exercises within existing milestones. They do not create two concurrent courses, university enrollment, a claim of full-course completion or new calendar deadlines. Detailed source investigations: [MIT](../research/mit-65840-course-fit.md) and [Stanford](../research/stanford-cs329z-course-fit.md).

## What each contributes

The legacy MIT 6.824 URL currently serves **6.5840 Distributed Systems, Spring 2026**. It is a graduate systems course emphasizing fault tolerance, replication and consistency through papers, programming and assessment. Our existing reading map already linked it generally; this revision turns that pointer into a concrete M7 selection. [MIT overview](https://pdos.csail.mit.edu/6.824/).

**Stanford CS329Z Engineering AI Agents, Fall 2026** addresses designing compound AI applications and agents. We use it to connect component design with empirical evaluation. It complements our source-code studies and systems work; it does not teach the whole OS/networking or inference-kernel curriculum. [Stanford course](https://cs329z.stanford.edu/).

## Required MIT selections — M7, reused in M10

These blocks are our teaching plan, not MIT assignment specifications. Use the Spring 2026 [schedule's notes, paper sections and questions](https://pdos.csail.mit.edu/6.824/schedule.html). A reading is complete when the learner can use its mechanism to explain an observed or constructed failure.

| Block | Selection and question | Evidence and initial effort |
|---|---|---|
| D1. Remote work and uncertainty | Introduction/MapReduce, RPC/threads and Lab 1's failure model | Trace our coordinator/worker protocol; distinguish timeout from proof of failure and identify storage assumptions. 3–4h. |
| D2. State correctness | Linearizability notes/paper selection and Lab 2's uncertain-outcome contract | Classify concurrent histories and explain a lost response without assuming whether the write succeeded. 4–5h. |
| D3. Replication | Selected Raft notes/paper sections, especially protocol rules | Defend election, log and commit behavior under partition/re-election; separate safety from progress. 5–7h. |
| D4. Coordination | ZooKeeper notes and selected paper questions | Explain durable coordinator state and why a stale owner can remain dangerous; connect this to our worker design. 3–4h. |
| D5. Task ownership | Ray ownership case study | Contrast recomputable tasks with external effects and durable jobs; state assumptions before reusing an ownership design. 3–4h. |
| D6. Assessment and transfer | Selected public exam problems plus an unfamiliar agent failure | Independent attempt, short defense and correction with evidence; include one paper claim and counterexample. 2–3h. |

Core selection estimate: **20–27h**, including study, practice and assessment. This is our provisional estimate for bounded selections, not MIT's workload estimate or sufficient time for all its labs. D2/D3 precede claims about broker replication guarantees. Reuse the RabbitMQ/Kafka failure traces when applying the concepts, counting shared evidence once; these readings alone do not satisfy the practical distributed-work criteria.

Optional MIT depth: GFS/Spanner, deeper transaction study and other case studies when a concrete question warrants them; a Go bridge followed by original labs. The full lab progression is a separate substantial implementation commitment, with dependencies between later labs. Do not promise any full original lab fits a six-hour slot. Before activation, diagnose Go/concurrency readiness, inspect its current specification, and split work into independently reviewable projects that meet the 21-day rule. An adapted TypeScript experiment must not be labeled completion of a MIT Go lab.

## Required Stanford selections — M3/M4/M7/M10

These blocks reuse the student's evolving agent. They are our adaptations, not recreated or completed Stanford homework.

| Block | Placement and learning question | Evidence and initial effort |
|---|---|---|
| S1. Components and retrieval | M3/M4: structured inputs/outputs, retrieval, tools and a simple baseline | Use a public/synthetic fixture to compare a fixed workflow with the bounded agent after language/API readiness. Study retrieval design; implement a RAG path only if the project needs it. Keep held-out cases and inspect evidence/errors. 6–8h, with one practical slice capped at 6h. |
| S2. Harness design | M4: memory/state ownership and what a framework abstracts | Trace the existing agent before comparing one framework; defend tool boundaries, stopping/cancellation and memory behavior. Reuse Pi/mini-swe-agent/Codex work. 4–6h. |
| S3. Single versus multiple agents | M7: when does delegation improve the chosen task? | Compare a single-agent baseline with one bounded multi-agent alternative under the same task set and stated resource budget; record costs and failure propagation. 4–6h. |
| S4. Evaluation and responsible operation | Introduce criteria in M3/M4; deepen in M10 with M11 acceptance | Define task/environment/stopping/scoring, separate development and held-out data, use deterministic checks where possible, calibrate a judge against human labels where useful, and test one tool-access/injection failure. Report uncertainty, limitations and recovery. 6–8h, with one practical slice capped at 6h. |

Core selection estimate: **20–28h** across stages, including overlapping tool/evaluation work once. Each practical project uses an existing artifact and has a bounded brief. Optional depth includes DSPy optimization, fine-tuning methods, proactive agents and a broader paper survey. Framework names are comparisons, not a mandate to learn every listed framework.

## Prerequisites and availability

- MIT assumes substantial systems/programming readiness. Our M4 worker contracts and M5 operation/failure checkpoints come first; original Go labs require an additional Go/concurrency bridge. [MIT general information](https://pdos.csail.mit.edu/6.824/general.html).
- Stanford lists NLP-course background or equivalent. Check Python/API literacy if using its Python examples, tokens/context/embeddings, basic model behavior and evaluation/data-split reasoning; use an appropriate M6 bridge for gaps. This does not require finishing every advanced M9 inference topic before studying agent design. [Stanford logistics](https://cs329z.stanford.edu/logistics.html).
- On September 28, Stanford's first two slide sets are linked; future materials are still being released. Homework descriptions are published, with releases scheduled for October 5 and October 26. Use released sources and public readings, then recheck at lesson preparation. Detailed future handouts/tests are not assumed available. [Course schedule](https://cs329z.stanford.edu/).
- Stanford recordings require Canvas; public reading access is distinct from formal auditing or course services. We do not depend on private recordings, grading or peer access. [Logistics](https://cs329z.stanford.edu/logistics.html).

## Workload, overlap and assessment

The two selected routes total **40–55 provisional hours of study activity**, spread through the relevant milestones. This is neither a net addition of 40–55h nor a new overall course estimate: the existing program already requires much of the same material, and the [overall workload forecast](../course/WORKLOAD.md) now includes these selections inside the owning milestone estimates. When preparing a block, name the existing lesson/experiment it replaces and estimate only genuinely additional work. Preserve explicit resource-completion goals such as the Claude API course; shared experiments count once, while any remaining course content remains assigned.

Stay within **15h/week**: 10 core/labs, 3 project, 2 exploration. A six-hour project slice uses two project weeks; no parallel second primary module. Leave dates blank until the owning Obsidian project is reviewed. MIT and Stanford semester deadlines do not become the student's deadlines. M1's demonstrated tool cycle is credited rather than repeated.

Use a paper claim → assumptions → counterexample/experiment → defense structure. Add a short closed-resource explanation of the learner's own design and a fresh failure scenario. For Stanford-inspired work, preserve a simple baseline, evaluation inputs and error analysis; for MIT-inspired work, preserve a system history and explicit safety/liveness assumptions. Apply our pass/revise rubric and M11 acceptance packet. These are our assessments, not university grades or an imitation of university enrollment.

AI can explain, question, review and give bounded hints; learner-authored reasoning and changes establish mastery. Consult the original assignment's current collaboration rules if taking an original lab. A teacher-generated finished solution is not assessment evidence. Keep the inference route (CS336/vLLM, M6/M9), Linux/networks, brokers and Kubernetes outcomes intact.
