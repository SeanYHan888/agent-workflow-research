# MIT 6.5840 / former 6.824 — course fit

Researched September 28, 2026. Recommendation for this workspace; no student work assigned or completed. Read the current official home, general information, Spring 2026 schedule, all five lab specifications, Go/setup and debugging guidance, selected lecture notes, and the public past-exam index plus 2025 exams. No starter repository was cloned and no lab runtime was tested. The linked landing page is mutable; this review identifies the Spring 2026 offering rather than silently mixing older 6.824 lab sequences.

## What the course contributes

[MIT's current course](https://pdos.csail.mit.edu/6.824/) is **6.5840 Distributed Systems**, a 12-unit graduate subject. Its organizing questions concern replication, fault tolerance and consistency. It expects prior computer architecture and systems/OS education, or equivalent competence, and substantial programming experience. The old number was 6.824 before 2023. [General information](https://pdos.csail.mit.edu/6.824/general.html).

The format combines papers, discussions, programming, examinations and code explanations. The current schedule also includes storage, transactions, coordination, verification, Ray and Byzantine-failure case studies. This is a strong foundation for explaining why an agent coordinator remains correct when requests time out, workers disappear or replicas disagree. It is not a model-inference or Kubernetes administration course. [Spring 2026 schedule](https://pdos.csail.mit.edu/6.824/schedule.html).

Our recommendation: use a selected route as the **M7 theoretical foundation**, connected to the existing RabbitMQ/Kafka experiments, then revisit the claims in M8/M10. Full completion remains an optional specialization. A course link already exists in [the systems map](../materials/systems-reading-map.md); this report makes its selection and limits concrete.

## Current programming sequence

These are the 2026 specifications, not the different lab numbering found in many older tutorials.

| Lab | Actual scope and dependency | Proposed role here |
|---|---|---|
| [1: MapReduce](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html) | Implement a coordinator and parallel workers, RPC task assignment and worker-failure recovery. The lab runs processes on one machine and relies on a shared filesystem. | Best optional first implementation; directly comparable to our worker adapter. It does not demonstrate real multi-host capstone operation. |
| [2: Key/Value Server](https://pdos.csail.mit.edu/6.824/labs/lab-kvsrv1.html) | Single-server linearizable Get/conditional Put and a lock, including dropped requests/replies. At-most-once writes may still have an uncertain outcome (`ErrMaybe`). Clients holding locks do not crash in the lab. | Read the specification for M7 uncertain-outcome reasoning; optional implementation after Go readiness. Add a discussion of the missing crashed-lock-holder case. |
| [3: Raft](https://pdos.csail.mit.edu/6.824/labs/lab-raft1.html) | 3A leader election, 3B log, 3C persistence, 3D log compaction. Supplies the replicated-log implementation needed downstream. Membership changes are excluded; persistence uses the provided Persister abstraction rather than requiring disk I/O. | Read protocol and trace failures in the core route. Full implementation is an optional substantial sequence, not a six-hour side project. |
| [4: Fault-tolerant Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-kvraft1.html) | Builds on Lab 3: 4A generic replicated state machine, 4B replicated KV, 4C snapshot support from 3D. Lab 2 code may be reused but is not required. | Optional continuation once Raft is sound; useful for understanding the gap between consensus and a complete service. |
| [5: Sharded Key/Value Service](https://pdos.csail.mit.edu/6.824/labs/lab-shard1.html) | Uses Lab 2 KV plus Lab 4 RSM/Raft. 5A shard movement, 5B failed/partitioned controller, 5C concurrent controllers, 5D learner extension. Shard assignment changes are distinct from Raft membership changes. | Optional advanced specialization. MIT allows an approved final project instead; our capstone can borrow the research discipline without claiming to satisfy MIT's course. |

These implementation dependencies prevent treating every interesting lab as an interchangeable standalone exercise. A narrow specification analysis can stand alone; a functioning Lab 5 cannot honestly be promised without its prerequisites.

## Selected route inside our milestones

The following is **our teaching selection and estimate**, not an MIT assignment or official workload. It strengthens existing coordination/failure outcomes without adding a new milestone ID.

| Slot | Source selection | Learner evidence | Hours |
|---|---|---|---|
| M7 entry | MapReduce paper and RPC/thread lecture from the [schedule](https://pdos.csail.mit.edu/6.824/schedule.html); Lab 1 failure model | Draw the coordinator/worker protocol; explain timeout versus proof of failure and identify its storage assumptions | 3–4 |
| M7 state correctness | [Linearizability notes](https://pdos.csail.mit.edu/6.824/notes/l-linearizability.txt) and the scheduled paper through §3.1; Lab 2 specification | Classify small concurrent histories; explain a lost response without equating at-most-once with a known successful outcome | 4–5 |
| M7 replication | [Raft notes](https://pdos.csail.mit.edu/6.824/notes/l-raft.txt), extended paper §§2–5 and §7, especially Figure 2; optional safety-detail follow-up | Trace a partition/re-election and defend which operations can be acknowledged; distinguish safety from progress | 5–7 |
| M7 coordination | [ZooKeeper lecture](https://pdos.csail.mit.edu/6.824/notes/l-zookeeper.txt) and the scheduled paper | Explain what state the agent coordinator owns, what must outlive it, and how a stale owner can remain dangerous | 3–4 |
| M7/M10 bridge | [Ray ownership lecture](https://pdos.csail.mit.edu/6.824/notes/l-ray.txt) and its scheduled paper | Compare task/future ownership with our durable jobs and external effects; identify what cannot safely be recomputed | 3–4 |
| M7 assessment | Selected public exam problems and one unfamiliar agent-failure scenario | Independent written attempt, oral defense, then correction with evidence | 2–3 |

Total selected route: **20–27 hours**, including discussion and assessment. This excludes implementing MIT labs. Use the existing 10-hour core allocation, spread across the active M7 period. It occupies roughly 2–3 core weeks before other M7 work; it is not an additional weekly lane or a new deadline. Count shared queue/retry/consistency evidence once, and subtract demonstrably equivalent existing lessons at activation. The current broker estimate remains a separate starting estimate, not proof that their combined scope already fits old dates.

GFS and Spanner are useful optional case studies for storage/transaction questions arising in M7/M10. Broad Paxos, formal verification, blockchain and Byzantine-fault coverage can wait unless a project requires them. This selection is not represented as completing the entire MIT syllabus.

## Relationship to message brokers, Kubernetes and inference

RabbitMQ and Kafka teach the behavior of real messaging interfaces and operations. The MIT route asks what guarantees a coordination protocol can provide under a stated failure model. Use the same lost-response, duplicate-delivery and stale-worker incident across both lessons, but assess different claims: a transport acknowledgement is not by itself proof that an external action happened once; a replicated record does not remove uncertainty about an outside API call. These are our integration questions, not claims that MIT teaches either product.

M8 can reuse replication/consistency reasoning when explaining persistent control state and application recovery. M9 is not an automatic destination merely because a paper says “distributed”: Ray's ownership discussion can support model-serving architecture, while numerical kernels, KV caches and GPU parallelism remain owned by our inference materials. M10 must still include actual multi-host experiments; local lab test processes cannot replace that evidence.

## Programming bridge and optional lab budget

MIT specifies **Go 1.22 or later**, supplies local-machine setup guidance and recommends familiarity with the language. [Go setup](https://pdos.csail.mit.edu/6.824/labs/go.html). Do not install a copied Linux amd64 command on an arbitrary ARM VPS. Check the actual runtime when a lab is activated.

Before implementing, diagnose readiness in structs/interfaces, slices/maps, errors, goroutines/channels, mutexes, RPC, files, testing and the race detector. A learner who can already program confidently may need **8–12 hours** for our narrow Go bridge; a beginner can need substantially more. Use the linked Go Tour and a small unrelated concurrency exercise. Language learning is not hidden inside a distributed-systems debugging estimate.

Provisional teacher estimates, to be recalibrated after the first learner attempt:

- Lab 1: **12–20 hours** after the bridge. Split a healthy-path coordinator/worker artifact and a recovery/testing artifact, approximately 6–10 hours each. If using only the three-hour project slot, split any slice above nine hours further; alternatively make it the primary core lab and account for those hours explicitly.
- Lab 2: **8–14 hours**, split reliable-service/lock and dropped-message analysis/testing. This is optional added implementation scope unless chosen as an equivalent practical exercise.
- Lab 3: **40–70 hours**; Lab 4: **20–35 hours**; Lab 5: **25–45 hours**. These are uncertainty ranges for planning, not guarantees or official lab durations. Split each part into useful, independently reviewed increments and reforecast after each.

MIT's own [lab guidance](https://pdos.csail.mit.edu/6.824/labs/guidance.html) describes moderate tasks as roughly six hours per week and hard ones as exceeding six, emphasizing that debugging can dominate code size. The official **12 units** is a course designation; the ranges above are not a conversion of those units. A full lab route needs a separate deliberate schedule choice and cannot be folded into spare exploration time.

## Assessment, access and AI boundaries

Use the [past-exam collection](https://pdos.csail.mit.edu/6.824/quizzes.html) selectively after teaching the relevant material. The [2025 first exam](https://pdos.csail.mit.edu/6.824/quizzes/q25-1.pdf) includes MapReduce and linearizability questions suited to our selected route; the [second](https://pdos.csail.mit.edu/6.824/quizzes/q25-2.pdf) covers additional papers that are not all in it. Both allow personal source material while prohibiting network/AI assistance during the attempt. Our proposed 45–60-minute checkpoint uses selected questions, followed by feedback; it is not the full MIT examination or an MIT grade.

For any implementation, retain our artifact + explanation + unfamiliar change rubric. Passing supplied tests alone does not establish understanding. The student explains one failure trace and investigates a changed condition; the teacher provides hints and review, not the exercise solution.

MIT's [collaboration policy](https://pdos.csail.mit.edu/6.824/general.html) requires individual lab work, forbids using others' solutions, cautions that AI-written code reduces learning, and expects students to explain their submissions. It does not state an absolute ban on all AI tutoring. It also asks that lab solutions not be made available to present or future students. Keep implementations private and avoid pasting solutions into this research repository if its publication status is uncertain. The public materials are readable, while [submission instructions](https://pdos.csail.mit.edu/6.824/labs/submit.html) lead to Gradescope; this review does not establish access to enrollment, grading, office hours or a credential.

No live Obsidian owner was read for this research-only recommendation, so it creates no dated assignment, progress claim or deadline change. Activation must inspect that owner under the [charter](../course/CHARTER.md) and preserve the [roadmap](../ROADMAP.md)'s 15-hour limit.
