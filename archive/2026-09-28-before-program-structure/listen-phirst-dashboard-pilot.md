# Listen Phirst dashboard: first autonomous pipeline pilot

Planning snapshot — September 24, 2026. Parent: [autonomous pipeline plan](autonomous-job-pipeline-plan.md). The user selected dashboard work in `phicil-itate/listen-phirst` as the first coding workload. No feature implementation or GitHub mutation has been performed.

## Verified starting point

- Private repository: [phicil-itate/listen-phirst](https://github.com/phicil-itate/listen-phirst).
- Integration branch inspected: `test`, commit `b52c6975f35e3005468180d5325999a0e5eb58f6` (September 18). Refresh before execution.
- The Analytics dashboard milestone consists of open issues [#23](https://github.com/phicil-itate/listen-phirst/issues/23), [#24](https://github.com/phicil-itate/listen-phirst/issues/24), [#25](https://github.com/phicil-itate/listen-phirst/issues/25), [#26](https://github.com/phicil-itate/listen-phirst/issues/26) and [#27](https://github.com/phicil-itate/listen-phirst/issues/27).
- Issue #23 has no comments in this snapshot. The inspected `test` docs tree has no dashboard/analytics/scope-named spec. No dashboard PR appears among the current open PRs; four dependency-update PRs are open. This does not establish that nobody has unpublished work; confirm task ownership before starting a writer.
- Issue instructions use `sean/<short-slug>` branches and PRs targeting `test`. Follow that repository-specific prefix rather than the generic `codex/` default.

## Dependency and decision structure

```text
#23 Dashboard scope and data/auth decision
    ├── #25 Patient endpoints → #27 Patient dashboard
    └── #24 Admin aggregates  → #26 Admin dashboard
                                  ↑
                      admin browser-auth decision
```

This is a milestone, not one bounded agent job. Each branch becomes smaller accepted jobs. **The user selected patient-first on September 24**, reusing the existing patient session as specified in #25/#27. That settles audience and sequence for the pilot; it does not settle the exact visible fields or waive ownership checks and the remaining #23 product/data decisions. The admin path stays later.

## Research job R1: prepare the dashboard decision

Question: **What is the smallest useful dashboard slice supported by the current data and authentication boundaries, and what decisions are required before implementation?** This is a proposed first research job tied to the selected coding workload; a separate general research topic is still open.

Inputs: issues #23–27; `AGENTS.md`; `CONTEXT.md`; ADR 0009; existing patient consent/session routes; response models and services; `frontend/src/services/api.ts`; current dashboard and navigation source; relevant tests. Read the required August audit before proposing auth/consent changes. Inspect source and synthetic fixtures, not live patient records.

Output: a short candidate `docs/` spec with an evidence ledger. For each proposed field/metric, identify the audience, user question, meaning, data source, date/time basis, access rule, response shape and empty/error behavior. For admin metrics, define numerator/denominator and grouping explicitly rather than infer them from labels. Distinguish verified code behavior from a proposal and from a product-owner decision.

The report must present concrete options for:

1. The exact first patient-visible fields; patient-first delivery is already selected, so do not reopen the audience choice.
2. Summary/aggregate data versus individual-record or transcript drill-down.
3. Record admin authentication as a later dependency rather than blocking the patient slice; browser API keys are excluded by repository convention.
4. Which mock page(s) are replaced and how navigation reaches the real page.

Source of the gate: issue #23 says **“Decide before any code.”** The pipeline may autonomously investigate, compare options and draft the spec. The human/product owner resolves these choices; the runner then records the accepted spec revision as input to implementation. The research job is successful when it provides an evidenced decision packet, not when it invents an approval.

## Coding jobs after scope is resolved

| Job | Bounded output | Required evidence |
|---|---|---|
| C1: one approved patient resource from #25 | Small session-cookie endpoint and corresponding backend tests; start with one resource chosen in the spec | Own-record success; unauthenticated handling consistent with the session contract; another patient's identifier returns 404; empty-data behavior; no excluded fields in payload/logs |
| C2: corresponding section of #27 | Replace the selected part of the mock patient dashboard using `services/api.ts` | Existing SMS-link → OTP session reaches it; synthetic data rendered; loading, empty, error and expired-session states; no API keys in bundle |
| C3: remaining approved scope | Repeat small slices, then test their combined behavior | Full accepted dashboard criteria met; no live mock values masquerading as user data; combined checks and visual evidence on the candidate revision |
| Alternative admin path: #24 → #26 | Approved SQL aggregates and matching admin UI | Admin-auth decision implemented as specified; aggregate correctness from fixtures; excluded transcript fields absent; no PHI in logs; frontend uses the shared API client |

For any chart work, issue #26 requires loading the `dataviz` skill first. Verify that skill is available before selecting a chart implementation job. A chart is unnecessary for a first plain summary/list slice unless the accepted spec requires one.

The 30-minute pilot deadline applies to an individual small job, not the whole dashboard milestone. Split an oversized slice or explicitly revise its budget. Do not count a partial dashboard as issue #27 complete.

## Verification adapted to this repository

Read and honor [AGENTS.md](https://github.com/phicil-itate/listen-phirst/blob/test/AGENTS.md), [ADR 0009](https://github.com/phicil-itate/listen-phirst/blob/test/docs/adr/0009-allow-identifiable-data-in-initial-production.md), [mise.toml](https://github.com/phicil-itate/listen-phirst/blob/test/mise.toml) and [CI](https://github.com/phicil-itate/listen-phirst/blob/test/.github/workflows/ci.yml).

- `mise run backend:test` uses SQLite with test-only configuration. Add relevant ownership and aggregate/response tests and run the existing suite; a mocked happy path alone is insufficient.
- `mise run check` covers backend lint/type/tests plus frontend type/lint/build. CI additionally includes backend compile, secret scan, conditional image build/vulnerability/runtime checks and conditional Terraform validation. A local green check does not mean all CI gates passed.
- The inspected frontend package has no browser/component test script. Before claiming a UI job complete, define a repeatable browser test using synthetic data, including session and cross-user access behavior. Tool/test setup is explicit work; do not claim that `tsc` proves the page works.
- A fresh review checks the exact candidate against the accepted spec and repository rules. Any candidate changes invalidate the affected evidence.
- Read remote check results for the actual PR head after authorized publication. Skipped or unavailable checks must be explained; the agent cannot label them passing.

Repository-specific execution boundary: synthetic fixtures/local test DB for the pilot; no production data, SMS, gift-card issuance, deploy or credential rotation. The worker does not need deployment credentials. Every endpoint declares its credential; patient endpoints enforce ownership. Schema changes, if the accepted slice actually needs them, require the repository's migration + model + test process. Policy/auth changes and individual transcript exposure remain explicit decisions.

These boundaries come from the selected task and repository instructions, not a generic request to add unrelated security work. Existing security backlog items should be classified as blocking, relevant follow-up or unrelated; do not fold the entire backlog into the dashboard pilot.

## What the human sees

Initially: one scope decision packet from R1. During implementation: only a scope/auth/data decision, exhausted budget, material blocker or failed recovery. At delivery: a concise packet containing the issue/slice, accepted spec revision, branch and candidate hash, behavior evidence, actual checks/CI, browser evidence, remaining findings and recommendation.

Draft-PR publication is a proposed delivery mode to authorize when execution begins. Merge to `test`, promotion to `main` and any deployment stay human decisions initially. `production` is a deployment pointer and is never a worker target.

The pilot passes when a selected slice reaches a review-ready result without the user supplying implementation instructions during execution. Final review and a legitimate product decision do not count as pipeline failure; silent scope expansion and unsupported success claims do.

## Next build session

1. Scope the selected patient path and confirm it is not already owned by another active writer.
2. Run the read-only research job R1 and produce the decision packet.
3. Record the chosen fields/data boundary and resulting acceptance examples.
4. Prepare C1's isolated workspace and baseline; select the execution budget and delivery authorization.
5. Run the first bounded coding job with observation, then evaluate the interventions needed before adding the automatic repair/recovery loop.

These steps use the extra 3–5 build hours/week. The generic runner milestone estimate excludes an unknown amount of dashboard product work; estimate the dashboard after R1 rather than promising the whole milestone in the runner's 16–24-hour budget.
