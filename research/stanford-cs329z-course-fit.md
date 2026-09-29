# Stanford CS329Z — course fit

Researched September 28, 2026. This is a source review and teaching recommendation for our [roadmap](../ROADMAP.md), not enrollment, course completion or a tested implementation. The parent integration decision determines required selections; this report does not activate assignments or change deadlines.

## What the course is and what is available

Stanford **CS329Z: Engineering AI Agents**, Fall 2026, studies building compound AI applications. Its advertised sequence includes tool use, retrieval, memory, frameworks, multi-agent design, optimization, data, evaluation, safety and coding agents. The published calendar is tentative. It lists HW1 release on October 5 and HW2 release on October 26, both future as of this review. The website currently links introductory and September 28 slides; later lectures have topic descriptions and readings but no linked slides in the inspected schedule. [Official homepage and schedule](https://cs329z.stanford.edu/).

The logistics page requires NLP background equivalent to courses such as CS224N/CS336. It describes HW1 as implementing an internal-assistant harness without an agent framework, and HW2 as evaluating a supplied agent. Grades combine project 40%, homework 15%, homework quizzes 15%, paper presentation 10%, and peer review 20%. Formal auditing is restricted to Stanford students. Published site materials are public; lecture recordings require Canvas login. AI is permitted for learning, debugging and critique, but substantial AI completion or copied solutions violates the course policy; quizzes are individual and closed-book. These are Stanford's rules, not an assertion of our enrollment. [Official logistics](https://cs329z.stanford.edu/logistics.html).

The [introductory slides, pages 9 and 12](https://cs329z.stanford.edu/static/slides/lecture01.pdf) add useful evidence: students are expected already to understand basic LLM training/evaluation terminology, and the quiz is described there as a 15-minute oral check-in. Logistics instead says 10 minutes. Treat the exact official quiz format as unresolved until updated. Slides mention student compute support; this does not establish access for a public self-learner. The second linked slide deck could not be retrieved with the research tool; its contents were not inspected.

## Recommendation and boundaries

Use CS329Z as a selected **agent design and evaluation source**, distributed across our existing milestones. Do not import another full quarter or a second capstone into the 15-hour week. Its most useful contribution to this student's destination is the discipline of deciding what an agent should do, comparing it against a simpler baseline, and checking whether the resulting evidence supports the claim.

The following mappings are our curricular judgment based on the official syllabus, rather than Stanford's requirements:

| Our milestone | Recommended use | Boundary and evidence |
|---|---|---|
| M1: tool cycle | Diagnostic reference to the introductory material | Credit existing tool-cycle evidence. Ask one comparison question only if it reveals a real gap; do not restart the completed section. |
| M3: typed agent | Required selected builder/tool material when released and appropriate; use it to critique the student's existing small agent | Keep the existing JS/TS artifact. Examine an input contract, tool result, stop condition and error path. Do not require a parallel Python rebuild just to mirror a course resource. |
| M4: harness boundaries | Required selected design/framework and coding-agent material | Compare the studied harness with the student's implementation. Preserve mini-swe-agent → Pi → Codex source reading; lecture descriptions do not substitute for tracing source. |
| M7: durable coordination | Selected multi-agent discussion as an application comparison | Agent delegation does not demonstrate durable queues, consensus, broker guarantees or partition recovery. Keep the RabbitMQ/Kafka and distributed-state requirements. |
| M10: capstone | Required selected evaluation, data-quality and safety material, checked again when publicly released | Apply an explicit workload, repeat trials, human-reviewed scoring and failure analysis to the same capstone; do not add a separate Stanford-length project. |
| M11: engineering practice | Reuse design defense, critique and reproducible evidence | Connect results to the PR/acceptance record. A teacher critique is useful but is not represented as Stanford peer review or independent human review. |
| M6/M9: inference | Supplementary vocabulary and application tradeoffs only | Keep tensor/attention, cache, serving, kernels, batching and hardware measurements in their existing inference sources. App-level model selection does not establish inference-engine understanding. |

For the required selection, start with the released foundations/builder material, then select tool design, harness design, evaluation and safety readings at the relevant milestone. Recheck publication and assignment terms before using any later material. Treat RAG implementation, DSPy optimization, fine-tuning, full multi-agent framework comparisons, proactive agents and a paper video as **optional depth** unless a current project specifically needs them. This selection protects room for Linux, networking, brokers, Kubernetes and inference.

## Readiness and effort

The prerequisite is a reason to provide a diagnostic and targeted bridge, not to insist on completing an entire additional NLP course. Before a substantive CS329Z-derived lab, verify that the learner can write/debug a small asynchronous program, inspect an API response, distinguish development from held-out evaluation data, explain tokens/context, and separate model behavior from harness behavior. Introduce missing concepts as needed. This readiness checklist is ours; it is not a rewritten official admission requirement.

Provisional budget for our selected package: **20–28 focused hours spread over M3/M4/M7/M10**, comprising 6–12 hours selected reading and guided discussion, two six-hour lab slices, and 2–4 hours explanation, transfer assessment and focused revision. This estimates our bounded adaptation, not Stanford's workload. Count overlap with existing agent-building and capstone evaluation time once. The exact net addition remains unknown until existing learner evidence and the next eligible milestone are inspected. Any prerequisite bridge is estimated separately at that point. Full official homework could exceed these bounds; it is not silently included.

Each six-hour slice can fit two weeks of the existing three-hour project allocation and has its own finishable result. Alternatively, a slice can occupy the active core/lab allocation with equivalent work displaced. They are sequential options, not concurrent projects. No dates are assigned here and no existing deadline changes are implied.

## Two bounded adaptations for our course

These are original teaching designs, **not released Stanford assignments or their solutions**.

**Slice A — explain one agent decision, six hours.** Reuse the learner's existing M3 runner against a small synthetic/local document fixture. The learner chooses one task that might need tool selection and predicts whether a fixed workflow is sufficient. Compare that workflow with the bounded agent using the same inputs and access. Record tool sequence, final result, termination reason and resource/call counts. Reserve time to exercise a malformed tool response and one denied action. Finish with a runnable revision, short trace and explanation of the tradeoff. If framework setup would dominate, use the existing implementation.

**Slice B — make the acceptance claim testable, six hours.** Extend the same artifact with a small, fixed evaluation set separated from cases used during development. Include ordinary success, missing information, tool error and an instruction embedded in untrusted task data. Define allowed behavior and scoring before running the comparison. Record repeated trials under fixed model/configuration conditions, inspect disagreements manually, and distinguish empirical reliability on this fixture from broader correctness. A model judge is an optional extension after a human-audited criterion exists; it is not required merely to reproduce an advertised homework ingredient. Paid calls require a separately authorized budget; mock runs establish harness behavior only.

Each slice includes our own 10-minute closed-resource design defense; this is an explicit adaptation, not a claim to reproduce the unresolved Stanford quiz format. Allow additional time for feedback and revision. For each slice, use our [assessment rubric](../course/ASSESSMENT.md): an observed artifact, student explanation, and unfamiliar variation. A suitable unseen change is a tool timeout after an uncertain external effect, or a deceptively high evaluation score caused by an inadequate scorer. Ask for the student's prediction and diagnosis; do not supply the exercise solution. The later M10 acceptance package can reuse this evidence while adding distributed failures, deployment and serving measurements.

## Research limits and next check

This review inspected the official homepage, logistics and introductory PDF, plus our charter, roadmap, idea policy and assessment rubric. It did not obtain authenticated Canvas recordings, homework handouts, tests or a detailed final-project specification. Public assignment summaries are available, but future release dates are not proof that a full specification is already obtainable. No framework was installed, model called or exercise solved.

Recheck the public course site when the relevant milestone is ready, especially after the advertised homework releases. Preserve our own task boundaries rather than chasing the university calendar. Any full-course completion ambition would need a separate workload proposal; the selected-source integration above does not promise Stanford credit or completion.
