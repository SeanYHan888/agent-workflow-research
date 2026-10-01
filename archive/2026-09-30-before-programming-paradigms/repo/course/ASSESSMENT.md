# Assessment and feedback

The [roadmap](../ROADMAP.md) specifies each milestone's content. This page owns the common standard. Outcomes are **demonstrated** or **revise**, with dated evidence in the owning Obsidian project.

## Required evidence

Every milestone needs a working artifact or reproducible experiment, an explanation in the student's own words, and an unfamiliar modification or debugging task. A download, reading checkbox, passing build or AI-generated solution alone is insufficient.

| Dimension | Demonstrated when | Revision trigger |
|---|---|---|
| Correctness | Intended behavior and relevant failure cases are observed with reproducible inputs | Only a happy-path demo, missing verification, or incorrect result |
| Understanding | Student traces control/data/state ownership and explains the key mechanism and assumptions | Repeats terminology without explaining an actual example |
| Transfer and diagnosis | Student reasons through an unfamiliar change or failure, tests a hypothesis, and explains the result | Cannot adapt beyond the supplied solution |
| Evidence and judgment | Revisions, commands/conditions, measurements and limitations support the conclusion | Unsupported performance claims, confused simulation/measurement, or hidden failures |

All four dimensions must be demonstrated; a strong demo does not compensate for unexplained behavior. Use a short diagnostic early to credit prior knowledge and target instruction.

## Assessment session

1. Name the milestone and exact criteria being assessed. Read earlier evidence first.
2. Student demonstrates the artifact/experiment and explains one path end to end.
3. Teacher introduces a small unseen variation or failure. Ask for a prediction before execution.
4. Record the result for each dimension, assistance used, links to evidence and the smallest remaining gap.
5. For `revise`, assign focused practice and reassess that gap with a fresh variation. Reuse already valid evidence; no arbitrary restart or penalty.

AI assistance is welcome during practice. During assessment, the teacher supplies the scenario and can clarify it; the student supplies the reasoning. If substantial hints or generated solutions are needed, record the support and use another variation before crediting independent transfer. Providing a requested worked explanation is teaching, not passing an assessment.

## Advanced work and capstone

Advanced milestones add a bounded research comparison or reproduction: state the claim, inspect its source, define a controlled test, report results and limits. Derive relevant quantities such as memory costs rather than copying them without assumptions. A failed reproduction can demonstrate understanding when the method and explanation are sound.

The capstone requires a design defense, evaluation workload and failure experiments. Record exact artifacts/revisions, deployment topology, model/runtime/hardware conditions, correctness and errors, latency/resource use, human interventions and unresolved limitations. Demonstrate cancellation, overload, worker/server loss and recovery. Use real multi-host execution for the distributed-agent claim; simulation can support an inference-parallelism analysis but must be labeled as such.

## Deliverable acceptance versus learner mastery

Apply [M11 engineering practice](modules/engineering-practice.md) to substantive course deliverables: identify the candidate revision, acceptance criteria, verification and review evidence, unresolved limits and recovery method before recording accept/revise. PR approval, merge permission and deployment permission are separate decisions. A result can meet its requirements while the learner still needs assessment of understanding; preserve both judgments distinctly.

## Systems evidence — September 30, 2026

Use the [R1/K1–K5, F0/O/N/S and D1–D3 criteria](modules/systems-foundations.md). M12 requires learner-authored compiler/VM behavior, semantics-preserving transformation evidence and an unseen extension or bug diagnosis; a copied interpreter is insufficient. M5 requires OS/network/security mechanism explanations with failure experiments, beyond command familiarity. M7 storage requires stated commit/recovery assumptions and transaction-history reasoning; process-kill tests do not prove power-loss safety. Reuse demonstrated evidence across modules and record only remaining gaps.

## Core-foundations evidence — September 30, 2026

[M13–M15](modules/core-foundations.md) use A1–A4, ALG1–ALG4 and DM1–DM4. Require a machine trace and controlled experiment, algorithm cost/correctness reasoning, and proofs/derivations with explicit assumptions. A mathematical artifact can be a proof plus counterexample/simulation rather than a software build. Each needs learner explanation and an unfamiliar variation. Diagnostics credit existing mastery; unsupported assumptions based on Python experience do not. F0 evidence is credited through M13 and reused in M5, never reassigned as a second requirement.

## Evidence record

In the owning Obsidian project, record: date, milestone/criterion, focused time, artifact/revision and output links, student explanation, unfamiliar scenario, assistance, dimension results and next step. Preserve historical completion when the curriculum changes; record additional requirements as new gaps linked to the approved change.

## M7 broker evidence — added September 28, 2026

The required [RabbitMQ/Kafka module](modules/message-brokers.md) uses the same artifact, explanation and unfamiliar-change rubric. Require both bounded lab results and a justified transport choice. Inspect the crash-after-effect/before-ack-or-commit case, duplicate handling, retry/overload limits and replay/ordering evidence. A single-node lab does not grant the separate multi-host failure criterion, and broker-level delivery guarantees do not establish exactly-once external effects. Preserve earlier queue evidence and assess only unmet criteria.

## University-source assessments — September 28, 2026

For the [selected MIT/Stanford route](../materials/university-course-integration.md), require a paper claim with assumptions and a counterexample/failure history, plus a short independent design defense. MIT selections add concurrent-history and protocol reasoning; Stanford selections add a simple baseline, development/held-out separation, scorer validation and error analysis. Reuse valid existing evidence and assess only gaps. Our adapted checkpoints are not university exams, grades or full-course completion. If using original assignments, inspect their current collaboration rules; retain learner authorship and keep MIT lab solutions private. No public recording, peer grading or university access is presumed.
