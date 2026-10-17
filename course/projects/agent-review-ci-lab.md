# Agent review and CI — M11 delivery experiment

Accepted October 1, 2026 after the student asked to add an experiment testing when a robust review/testing process can justify less manual code inspection. This is the concrete delivery exercise for M11 E3/E5/E6, practiced with an existing M3/M4 artifact. It replaces the generic delivery slice, retains its recovery assessment, and is not a new milestone or active assignment.

## Question and deliverable

**Which defects do tests, a separate review agent and human inspection catch, and what evidence would justify reducing manual inspection for this kind of change?**

Deliver one small, reproducible review-and-repair pipeline and an evidence report. Reuse a runner/agent component with a clear public contract, such as timeout/cancellation handling. The learner defines acceptance examples and explains the implementation; the teacher prepares the exercise fixture when the lesson begins, without completing the learner's solution.

## Entry, time and ownership

- Entry: M11 E1/E2 Git inspection/recovery, E3 behavioral-test readiness, and enough M3/M4 understanding to explain the selected component. Use a disposable exercise repository and synthetic inputs.
- Allocate **up to six focused hours**, including setup, selected reading, trials and defense: approximately 1h for contract/fixture, 2h for CI/reviewer wiring, 2h for trials/repair and 1h for acceptance/recovery. This replaces the existing six-hour M11 delivery slice within its 12–18h estimate. At three project hours/week it spans two weeks inside the same 15h weekly budget.
- Reuse existing tests and agent tooling; no new orchestration framework, product feature or multi-provider benchmark. If setup threatens the timebox, narrow the component/case set or reforecast the remaining work; do not mark unexecuted CI complete.
- Check the live TS agent owner or the later worker owner at activation. Reuse one owner or assign a single bounded successor then. No execution checklist, new date or progress credit is created here.

## Pipeline to build and inspect

```text
Behavior contract + identified candidate revision
  → deterministic checks (types/lint + relevant behavior tests)
  → separate agent review of the actual diff, spec and test evidence
  → bounded repair of actionable findings
  → rerun checks and review the changed candidate
  → human accept/revise with residual risks and recovery evidence
```

Start with a read-only reviewer in a fresh context, separate from the author conversation. Give it the actual candidate, contract and repository standards; do not treat its agreement as statistically independent confirmation. Findings need a location, concrete trigger, consequence and proposed correction. Human triage distinguishes demonstrated defects, unsupported findings and suggestions.

Run deterministic checks as required CI checks. The review agent is an additional source of findings, not a replacement for test assertions. Record the exact commit for every check and review; an earlier green run cannot approve a later repair. Explicitly account for staged, unstaged and untracked files when reviewing locally.

Bound the repair loop to **two attempts**, with a runtime/usage limit chosen before execution. If checks still fail, the reviewer cannot run, or a requirement is unresolved, report `revise` or `needs decision`; do not turn missing evidence into a pass. Do not let repair remove required checks or weaken the acceptance contract to make the run green. Keep test/contract changes visible for review.

Use minimum repository permissions, avoid giving the read-only reviewer write credentials, and keep untrusted fixture code away from privileged secrets. Configure and verify required checks and human integration control in the exercise repository. Hosted workflow setup and model usage need the actual repository/account authorization at the lesson; adding this curriculum does not enable an integration, buy usage or authorize publishing. A local rehearsal can establish pipeline behavior, but must be labeled local; hosted CI evidence remains outstanding until actually run.

## Defect experiment

Use one clean control and three small teacher-prepared faulty variants of the same component. Include a missing edge case, a failure/cancellation defect, and a misleading test or review-scope defect. Keep the answer key and at least one acceptance variation out of the author/reviewer context until scoring. Fixture code and solutions are prepared only at lesson time.

For each initial candidate, freeze its revision and collect, in order: deterministic-check results, a fresh reviewer result before any repairs, and human inspection. Reveal the held-out check afterward to score misses; then attempt repairs and verify the final candidate. Reset each trial so previous repair context does not leak the answer into the next reviewer run. The clean control helps reveal false alarms.

Record:

| Evidence | Measurement |
|---|---|
| Detection | Which seeded defects each stage caught before repair; misses against the held-out oracle |
| Review quality | Actionable true findings, false alarms and unresolved findings |
| Human effort | Inspection/triage minutes and number of interventions |
| Execution | Candidate hashes, commands, CI run/result, reviewer/model configuration, elapsed time, usage/cost when available |
| Repair and recovery | Attempts, final behavior, regressions, and one observed revert/recovery drill |

This small sequential trial characterizes these fixtures; it does not establish a production escape rate or a causal productivity improvement. Human review benefits from earlier evidence, and crafted defects are not a representative random sample. Claims about time saved require a separate comparable baseline; otherwise report only observed minutes. Different models or extra reviewer agents do not establish independent correctness.

## Acceptance and learner defense

Reuse the [M11 acceptance packet](../modules/engineering-practice.md#review-and-acceptance-packet). The learner must explain one initially green-but-wrong candidate, trace a defect to its consequence, judge reviewer findings, recheck the repaired revision, and demonstrate recovery. The teacher supplies an unfamiliar variation for the learner's own reasoning under the [assessment rubric](../ASSESSMENT.md).

Conclude with a bounded manual-review policy: which low-impact changes might justify less inspection, which assumptions support that choice, and which triggers require deeper inspection (for example changed access control, persistent data, concurrency or weak test coverage). “Tests passed and an agent approved” alone is not a sufficient conclusion. Finding that manual inspection remains necessary is a successful experimental result.

## Readings

Use the [M11 reading map](../../materials/engineering-practice.md#agent-review-and-ci-experiment) for selected review guidance, GitHub Actions documentation and the existing workflow research. Refresh exact provider actions, permissions and repository rules when preparing the lesson.
