---
type: project
status: later
area:
start:
deadline:
outcome: Turn on noUncheckedIndexedAccess and exactOptionalPropertyTypes in Daily Task Panel, fix every error they report myself, and explain each fix.
created: 2026-09-28
tags:
  - project-file
related:
  - "[[terminal-agent-03-typescript-agent]]"
roadmap: "[[Notes/Coding Agent Course/00 Start Here]]"
sequence: 12
order: 19
---
# TypeScript plugin lab 01 — Strict compiler flags

[[Notes/Coding Agent Course/00 Start Here|Course overview]] · Entry gate: [[terminal-agent-03-typescript-agent|Section 3, Boot.dev TypeScript]] · Classroom design: `/Users/seanmacbook/Projects/agent-workflow-research/typescript-plugin-lab.md` · Plugin repo: `~/Projects/obsidian-taskflow`

> [!note] Scope: at most three weeks
> Choose one deliverable finishable within 21 calendar days at available capacity. Set start and target finish when activating; split larger work into separate projects. See [[Indexes/System/Project Workflow#Project size: maximum three weeks]].

## Project goal:

Apply Section 3's TypeScript to real code I maintain. Two stricter compiler flags point at every place in the plugin where a value might be missing, and I fix each one myself.

## Planned window:

Two to three weeks; about 12–15 focused hours (an estimate). Optional follow-on inside the shared 10 hours/week study budget: set calendar dates when activated, and take the hours from other planned course work rather than adding them on top. Do not compress the dated foundation sections to make room.

**Entry gate:** Boot.dev TypeScript through unions and narrowing. I can explain what `string | null` means and how an `if` narrows it. Recommended start: after the Section 3 checkpoint, or at its pace review if Boot.dev TS finishes early.

## Done when:

- Both flags are on in `tsconfig.json` on the `pipeline` branch, with `npm test`, `npm run build` and `npm run lint` passing, and no `any` or `as` cast added just to silence an error.
- The panel still works in the dev vault after the change.
- Without notes, I can explain what TS2532, TS18048, TS2345 and TS2322 mean, and when a guard, a `??` default or a `!` assertion is the right fix. The explanation is in the progress log.

## Start here:

Attempt first, then ask. Claude gives the smallest useful hint and reviews my explanation; it does not write the fixes. Record each session below: date, focused minutes, what changed, my explanation, commit link and one open question. A passing build is not the checkpoint; my explanation is.

Work only on a branch in the plugin repo and test only in `taskflow-demo-vault`. Never run `deploy:prod` or `release:*` during the lab.

Error counts measured 2026-09-28 at plugin commit `7b95718`; remeasure when starting.

## Tasks:

### Step 0 — Set up

- [ ] Create branch `learn/01-strict-flags` from `pipeline` in `~/Projects/obsidian-taskflow`; run `npm test`, `npm run build` and `npm run lint` and confirm all three pass before changing anything

### Step 1 — Read the plugin's types with what Boot.dev taught (no code changes)

- [ ] Read `src/core/types.ts` and explain in my own words what `Task`, `string | null` and `Subject` mean
- [ ] Find three places in `src/core/` where an `if`, `?.` or `??` narrows a value that might be `null` or `undefined`, and explain each
- [ ] Read `tsconfig.json` and the TSConfig entries for `strict`, `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes`; explain what `strict` already checks and what each new flag adds

### Step 2 — `noUncheckedIndexedAccess` (63 errors)

- [ ] Turn the flag on, run `npx tsc --noEmit`, and group the errors by code (TS2532, TS18048, TS2345, TS2322); write one sentence on what each code means
- [ ] Fix `src/core/hierarchy.ts` (5 errors); for each one, choose between a guard, a `??` default and a `!` assertion, and write down why
- [ ] Fix `src/core/order.ts` (5 errors)
- [ ] Fix `src/core/move.ts` (11 errors)
- [ ] Fix `src/core/actions.ts` and `src/core/note-edit.ts` (7 errors)
- [ ] Fix the tests (35 errors, mostly `tests/pacing.test.ts` and `tests/classify.test.ts`); settle on one shared pattern for "this element must exist" in tests
- [ ] Run test, build and lint; commit the flag together with its fixes

### Step 3 — `exactOptionalPropertyTypes` (8 errors)

- [ ] Explain the difference between `x?: T` and `x: T | undefined`, using an example from `src/settings.ts`
- [ ] Fix the 8 errors (`src/settings.ts` 3, `src/ui/prompts.ts` 2, `src/core/actions.ts` 1, `src/adapters/tasks-plugin.ts` 1, `tests/hierarchy.test.ts` 1); run the checks and commit

### Step 4 — Wrap up

- [ ] Reload the plugin in the dev vault (`taskflow-demo-vault`, never the live vault) and check that check-off, reschedule and move-to-project still work
- [ ] Ask Claude to review the branch, fix what it finds, and merge into `pipeline`
- [ ] Write the checkpoint explanation in the progress log: the four error codes, when `!` is acceptable, and one real bug or edge case the flags exposed (or why none did)

## Decisions and blockers:

- 2026-09-28: Placed on the Coding Agent Course roadmap as an optional follow-on (sequence 12), the same way as the Magpie, harness-instruction and Rust trials. Not a prerequisite for any foundation section. Later stages (domain types, decoders, declaration files, async errors, optional framework-free UI and tooling) are designed in the classroom file; each gets its own project note only after this one closes, and only if still wanted.
- Boot.dev TypeScript stays owned by [[terminal-agent-03-typescript-agent]]. This lab applies it and does not replace or complete that task.
- Activation date, and which planned course hours it replaces, are not yet decided. `now` currently holds 4 projects against a limit of 3.

## Progress log:

- 2026-09-28: Re-scoped into the Coding Agent Course at the user's request. The separate roadmap note created earlier the same day was moved to the Obsidian trash; the Handbook basics reading was dropped because Boot.dev TS covers it. No study or code changes yet.
- 2026-09-28: Project created. No study or code changes yet.

## Resources:

- Classroom design and route: `/Users/seanmacbook/Projects/agent-workflow-research/typescript-plugin-lab.md`
- [Boot.dev TypeScript](https://www.boot.dev/courses/learn-typescript), the language instruction (owned by Section 3)
- [TSConfig: noUncheckedIndexedAccess](https://www.typescriptlang.org/tsconfig/#noUncheckedIndexedAccess)
- [TSConfig: exactOptionalPropertyTypes](https://www.typescriptlang.org/tsconfig/#exactOptionalPropertyTypes)
- [TSConfig: strict](https://www.typescriptlang.org/tsconfig/#strict)
- [Handbook: Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), as a reference when a fix is unclear
- Plugin rules: `~/Projects/obsidian-taskflow/AGENTS.md` (dev loop, two vaults)
