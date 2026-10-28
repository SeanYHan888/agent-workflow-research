# M10 — Publish and defend an agent-first Linux distribution

M10 is the Stage IV capstone. It integrates the components proven across the course into a small agent-first Linux distribution for remote VPS nodes, publishes it, and defends it. This page is a guide to the module. It arranges existing requirements into checkpoints and slices. It does not restate or change them. The [release brief](../projects/agentic-linux-distribution.md) owns the version 0.1 boundary, the acceptance-evidence table and the sequence of bounded work. The [project folder](../projects/agentic-linux-distribution/README.md) owns the six goals (Rust, easy remote SSH, distributed system, agentic first, safety, lightweight) and the M1–M19 contribution map. The [roadmap](../../ROADMAP.md#stages-and-milestones) owns milestone requirements and graduation dependencies.

## Useful result

Release version 0.1 as the brief defines it. A user downloads a versioned image and boots it through the supported VPS path. Over SSH they configure their own provider access, then run a bounded task, inspect and interrupt it, review its changes, and recover from a documented failure. The release keeps M10's distributed-system claims: durable jobs, isolated workers and a model-serving boundary, demonstrated on at least two real remote VPS nodes.

**Observable acceptance:** the release passes the brief's acceptance table. The image builds from a clean environment, installs on a fresh test target, matches its published checksums, and completes the documented workflow and recovery. Separately, the learner defends the design and diagnoses an unfamiliar failure. Publication readiness and learner mastery are recorded as separate facts.

## Open decisions

These choices stay open: the Linux base and distribution name; the image or install format; the init and service manager; the control interface; the network topology; the Rust component boundary; the VPS provider, profile and architecture; numerical resource limits and the workload; whether an MCP surface ships, and over which transport; and where coordination, storage and model serving run. Study and experiments make these choices. This page does not. The [October 4 build-first options](../projects/agentic-linux-distribution/BUILD-FIRST-OPTIONS.md) (routes A–C, early VPS work, reduced graduation scope) are proposals that have not been selected. A desktop ISO is not assumed.

## Graduation gates and slice entry

- **Final M10 assessment** needs, per the [roadmap dependencies](../../ROADMAP.md#dependencies-and-flexibility): the M19 MCP boundary decision, M18 skill evaluation and maintenance, M17 design and comparison, M7 durable work, M8 deployment, M9 serving and evaluation, M11 review/acceptance/recovery, M12 compiler work, M13–M15 foundations and M16 comparative design. The compiler and the M13–M16 teaching artifacts remain graduation requirements but need not ship in the image.
- **Slices can start before the final assessment.** Packaging begins incrementally. The design brief reuses M17 C1 and M5/M6 resource evidence. The first target experiment and C1 test the effort estimate before build work begins.
- **Uploading a release** needs separate, task-specific authorization under the [charter](../CHARTER.md). Planning and passing checks do not authorize publication, spending or provisioning.

## How earlier work feeds in

Reuse the artifacts that already work and count shared evidence once. The [contribution map](../projects/agentic-linux-distribution/README.md#how-the-whole-course-contributes) gives every milestone's role. The table below shows only which M10 checkpoint consumes each piece of evidence.

| Earlier evidence | Consumed by |
|---|---|
| M17 C1 comparison; M5/M6 resource measurements; M8 orchestration-cost comparison; M19 MC4 boundary decision | M10.1 |
| M5 service, SSH, permissions and isolation; M13 machine-limit reasoning | M10.2, M10.3 |
| M2/M3 runner and typed agent; [M4](agent-harnesses.md) adapter and session ownership; M12 R1 Rust component; M18 skill where justified; M19 server | M10.3 |
| M11 acceptance and recovery practice | M10.4, M10.6 |
| M7 durable jobs, broker and failure histories; M6/M9 serving measurements; CS329Z S4 evaluation fixtures; M14/M15 queue and invariant reasoning | M10.5 |
| M12, M13–M16 defenses and all retained evidence | M10.7 |

## Checkpoints

These checkpoints spell out the release brief and the roadmap row in more detail. They add no required outcome, depth or scope.

| ID | Brief step | Observable evidence |
|---|---|---|
| M10.1 | 1. Design brief and upstream comparison | Intended user, one workflow and one improvement compared against a plain upstream setup. Base, Rust component and VPS profile chosen. Numerical limits and a workload set before measurement. |
| M10.2 | 2. Bootable VPS baseline | Minimal image on the supported path. First SSH connection with host identity verified. Base OS idle cost recorded separately. |
| M10.3 | 3. Agent integration | Task entry, visible state, review, cancellation and resume, with owners named. Rust component errors, cancellation, concurrency and resource use tested. Safety-boundary tests passed. |
| M10.4 | 4. Update and recovery | One update and one failed update recovered. A statement of what rollback restores and what needs backup. |
| M10.5 | 5. Distributed evaluation | A fixed workload compared against a baseline on at least two real remote VPS nodes. Correctness, latency, resource use, failures and human intervention reported. |
| M10.6 | 6. Release preparation | A clean-environment build and a fresh install. Checksums and build logs, notices, guides, limits, release notes and an issue route. A fresh-download check once publication is authorized. |
| M10.7 | Learner defense | A design defense and an unfamiliar failure handled under the rubric. |

## Incremental packaging route

Each slice is one useful increment of at most 6–9 project hours, finished within 21 days. The brief allows a setup script as an intermediate artifact before an image exists. Use the [session workflow](../../teaching/README.md#prepare-and-teach). The learner builds and decides; the teacher reviews and prepares fault injections.

| Slice | Deliverable | Acceptance check | Learner's first action |
|---|---|---|---|
| S1 → M10.1 | Design brief | Limits and workload are written down before any measurement; a reviewer can say what result would refute the claimed improvement | Run the chosen workflow on plain upstream; record steps and human minutes |
| S2 → M10.2 | Repeatable setup recipe, then a minimal image | A fresh instance boots; SSH works with the host key checked; idle cost is recorded | Read the target's supported deployment path; predict what first boot must provide |
| S3 → M10.3 (split as needed) | Agent service integrated on the node | Bounded task with cancel, resume and review; a denied action under ordinary user permissions | Draw who owns each process, session, checkout and result |
| S4 → M10.4 | Update plus recovery drill | An induced bad update is recovered by the documented path | Predict what rollback will and will not restore |
| S5 → M10.5 (split as needed) | Evaluation run | Baseline and candidate run under fixed conditions; failure injections recorded | Write the workload, held-out cases and scoring before running |
| S6 → M10.6 | Release packet | A clean build reproduces the artifacts; checksums match; a fresh target installs from the packet alone | List each claim the packet makes and the evidence behind it |

## Failure experiments

Run these from the brief and the [capstone rubric](../ASSESSMENT.md#advanced-work-and-capstone). Write down the expected behavior before each injection.

- **Distributed work and limits:** duplicate delivery, link failure, worker and server loss, cancellation and overload, plus memory/disk pressure with bounded logs and queues. Do not claim exactly-once external effects; label simulated parallelism as simulation.
- **Access and updates:** access revocation, recovery from a bad configuration over SSH, and a failed update.
- **Safety:** a denied action, a cross-workspace attempt, untrusted task text asking for more authority, and the explicit elevation path. Check that no personal credentials appear in the image or logs.

## Defense

Follow the [rubric's capstone section](../ASSESSMENT.md#advanced-work-and-capstone). Record exact artifacts and revisions, the deployment topology, model/runtime/hardware conditions, correctness and errors, latency and resource use, human interventions and unresolved limitations.

Apply the CS329Z-inspired criteria: a simple baseline, development cases kept separate from held-out cases, a validated scorer, and error analysis. Reason about guarantees MIT-style. The teacher introduces an unseen failure and asks for a prediction before anything runs.

Artifacts generated by an agent, a booting image or public availability do not establish mastery. Apply the [M11 acceptance practice](engineering-practice.md) to the release candidate itself.

## Materials

| Source | Role | Checkpoint |
|---|---|---|
| [Release brief](../projects/agentic-linux-distribution.md), [project folder](../projects/agentic-linux-distribution/README.md) | Acceptance criteria, goals and contribution map | All |
| [M17 module](agentic-linux.md), [source map](../../materials/agentic-linux.md), [Omarchy checkout](../../materials/sources/linux/omarchy/README.md), [T3 Code background service](../../materials/sources/agents/t3code/docs/user/background-service.md) | Case studies for C1. Studying them does not require forking either product. | M10.1, M10.3 |
| [Build-first options](../projects/agentic-linux-distribution/BUILD-FIRST-OPTIONS.md) | Unselected routes and their packaging-gap analysis | M10.1, M10.2 |
| [M19 distribution connection](mcp.md#connection-to-the-distribution) | Whether an MCP surface ships, and its transport | M10.1, M10.3 |
| [Shared capstone plan](../../materials/advanced-study.md#shared-capstone-one-agent-one-model-server-visible-evidence) | A timeline from agent to model server, with measured, inferred and unavailable timings labeled | M10.5 |
| [CS329Z S4](../../materials/university-course-integration.md#required-stanford-selections--m3m4m7m10), [fit review](../../research/stanford-cs329z-course-fit.md), [MIT fit review](../../research/mit-65840-course-fit.md) | Evaluation discipline and reasoning about guarantees | M10.5, M10.7 |
| [Cua course fit](../../research/cua-course-fit.md) | Optional: independent final-state evaluation of an unfamiliar task | M10.5 (optional) |

## Assessment and hours

Use the [shared rubric](../ASSESSMENT.md) and its agentic Linux section. M10.1–M10.7 need artifacts, explanation and unfamiliar-failure evidence.

The [workload forecast](../WORKLOAD.md) estimates **53–85 directed hours**. That is 35–55h of integration, evaluation and failure defense, plus 18–30h for a narrow image, update/recovery and the release packet. M17 time is counted separately, and C1 is performed once. The estimate has not been validated against a real target. Reforecast it after the base and target decision instead of compressing scope. The 15h weekly cap applies.
