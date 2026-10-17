# M18 — Agent Skills: design, evaluate and maintain

Added October 16, 2026 at the student's request after reviewing five skill collections. This is a required, bounded course within Distributed AI Agent Systems, connected to M3/M4/M11 and the agent-first Linux project. It teaches reusable agent workflows through one learner-authored skill, not completion of every repository in the review.

## Useful result

Give the existing agent a repeatable way to inspect a failed local runner job and produce an evidence-backed diagnosis. The learner chooses a narrower workflow if that better matches their current artifact. Use local fixtures initially; reuse later service logs only after the Linux prerequisites. The deliverable is one versioned skill package, a small evaluation set and an evidence report explaining when the skill helps, fails or should not activate.

**Observable acceptance:** on a held-out failed-job fixture, the agent identifies the relevant evidence or explicitly reports insufficient evidence, follows the agreed output contract, and makes no unrequested changes. A passing example alone does not establish improvement; compare with the same task without the skill.

## Placement and prerequisites

- AS1 can be sampled after M1 tool-cycle orientation and basic repository reading. It does not block the current JS/Node restart.
- AS2 needs relevant M2 files/process/error knowledge and M11 inspect/recover practice. Use an existing harness; implementing a skill loader is optional later M3/M4 work.
- AS3 follows AS2 and basic fixture/test reasoning. AS4 uses relevant M4 harness boundaries; live service integration additionally needs M5 readiness.
- M18 is a graduation requirement. Full M18 completion is not an entry gate to M3, M4 or early Linux work. The final distribution reuses the evidence; it need not ship a general skill marketplace.

## Course sequence

| Block | Learner build or investigation | Evidence | Hours |
|---|---|---|---:|
| AS1 — Select and dissect | Compare two real skills for one runner task; trace metadata, instructions, references and tool assumptions. Explain skill vs repository instruction vs tool/MCP connector vs plugin packaging. | Annotated selection and one relevant/non-relevant trigger pair; predict what the host loads. | 2–3 |
| AS2 — Author one bounded skill | Write a focused `SKILL.md`, explicit inputs/output and failure behavior; separate supporting references. Add a helper script only if deterministic work warrants it. | Learner-authored package, valid metadata/paths, one normal case and one missing-input case. | 4–6 |
| AS3 — Evaluate and revise | Compare no skill, initial skill and one revision on the same frozen task set. Inspect false activation, missed activation and wrong/confident answers. | Per-case traces and scoring; repeated trials on ambiguous cases; an explanation of improvement or lack of it. | 4–6 |
| AS4 — Maintain and transfer | Pin provenance, inspect an upstream change, adapt one host-specific assumption, then demonstrate disable/rollback. | Compatibility note, version/change record and one unseen diagnosis or trigger change defended by the learner. | 2–3 |
| **Total** | Includes reading, attempts, feedback and assessment. | No duplicated M11 engineering or M4 harness instruction. | **12–18** |

The [source review](../../research/agent-skills-review-2026-10-16.md) supplies case studies. Start with Matt Pocock for a compact engineering workflow, then compare HumanLayer or Addy Osmani for context and orchestration choices. pstack supplies verification-generation and orchestration examples; Emil Kowalski supplies a focused domain-expertise example. These are teaching selections, not five mandatory installations.

## Evaluation contract

Before revising the skill, the learner proposes a small set of 6–8 cases covering intended use, a paraphrase, an unrelated request, missing evidence, an unavailable tool and misleading instructions inside fixture data. Reserve at least two cases for assessment; do not tune the skill against those cases. Agree the expected observable behavior and failure criteria before running.

Keep model, harness settings, tools, fixtures and task wording fixed when comparing skill variants. Record revisions, conditions, correctness, unsupported claims, tool actions, intervention and elapsed time; record tokens/cost only when the host exposes them. Separate trigger selection from execution quality. Repeat uncertain cases within the timebox and report variation. A small sample gives local evidence, not a universal benchmark or proof of safety.

Skills supply instructions; enforcement comes from the harness and operating environment. A stated tool list is not proof that a host enforces it. Test only within an isolated workspace with synthetic inputs. Inspect bundled scripts and dependencies before use. A compatibility analysis can satisfy the initial transfer study; actual cross-host success requires an observed run.

## First session brief — ready after owner review

- **Deliverable:** a one-page selection and anatomy comparison for two skills applied to the same failed-runner question.
- **Acceptance check:** the learner identifies the trigger, evidence source, output and host assumptions, and explains one request where each skill should remain inactive.
- **Learner's next action:** choose a familiar task and predict which instructions would change the agent's behavior before reading the complete skill.
- **Timebox:** 60–90 minutes within AS1; most time goes to annotation, prediction and a small fixture trial. Teacher supplies hints and asks for explanation; no completed skill or assessment solution is supplied during planning.
- **Close:** observed output or source trace, the learner's explanation and one next revision question. Record help used.

## Capacity, ownership and activation

This adds **12–18 directed hours**, using future course capacity under the 15h/week charter cap. It does not add weekly hours or move existing deadlines. The live overview read October 16 records a temporary 10h/week course allocation for October 16–29; use that lower available capacity during activation review, and do not assume the full charter allocation is available.

The existing owner is 智能体指令与技能试验, read through Obsidian on October 16: `later`, no dates, a three-hour minimal instruction/skill experiment, with unchecked tasks. Preserve that experiment as a possible first slice; it does not contain the full new course. At activation, map any genuine overlap once and assign the next bounded slice to an appropriate owner. Do not infer mastery from installed skills.

Use at most 6–9 project hours per execution slice and a useful result within 21 days at the actual allocation; reduce scope if the temporary capacity is smaller. Any remaining instruction comes from the primary module's core/lab allocation. Identify displaced work at activation rather than running a second module concurrently. No new project, date, installation, remote deployment or completion is created by this course brief.

## Assessment

Use the [shared rubric](../ASSESSMENT.md): artifact and reproducible results, learner explanation, unfamiliar change and evidence-based judgment. Require all AS1–AS4 criteria; accept a well-supported conclusion that the tested skill did not improve outcomes. Reuse M1 tool-cycle, M4 source trace and M11 review evidence for their existing criteria, and assess only the new selection/authoring/evaluation/maintenance gaps. Keep product acceptance and learner mastery separate.

## Primary references

- [Agent Skills overview](https://agentskills.io/home): format and progressive loading.
- [Agent Skills specification](https://agentskills.io/specification): metadata, structure and optional resources; reviewed October 16, 2026. Host behavior must be verified separately.
- [Five-repository review and per-skill catalog](../../research/agent-skills-review-2026-10-16.md): source revisions, purposes, dependencies and recommended selections.
