# TypeScript plugin lab — Daily Task Panel

Added September 28, 2026 at the user's request. This lab applies the course's TypeScript to a second, real codebase: the user's own Obsidian plugin, Daily Task Panel (`/Users/seanmacbook/Projects/obsidian-taskflow`, repo `SeanYHan888/obsidian-daily-task-panel`). It is course design, not a completion record. Obsidian owns tasks, status, dates, actual hours and evidence.

## Why this lab exists

Section 3 teaches TypeScript through Boot.dev and one small evolving agent. This lab adds what a small new program cannot: reading and safely changing about 5,000 lines of strict TypeScript that someone actually uses, with 19 test files and a pure core (`src/core/`) that has no framework or Obsidian imports. It departs from the "one evolving TypeScript build" rule on purpose: the plugin is maintained work the user already owns, so the practice is not a throwaway exercise.

## Placement, time and entry gate

- **Optional follow-on** on the Coding Agent Course roadmap, like the Magpie, harness-instruction and Rust trials. Roadmap sequence 12. It is not a prerequisite for any foundation section or workflow project.
- **Time:** inside the shared 10 focused hours/week. When activated, its hours replace other planned course hours; they are not added on top, and they must not silently compress the dated foundation sections. Set calendar dates only when activating; each stage is its own project of at most three weeks.
- **Entry gate:** Boot.dev TypeScript through unions and narrowing (Section 3). The learner can explain `T | null` and narrow it in their own words. Starting earlier means learning the TypeScript basics twice: once from the plugin's compiler errors and again from Boot.dev.
- **Recommended timing:** after the Section 3 checkpoint, or at the Section 3 pace review if Boot.dev TS finishes early. Decided by the user at a review, not inferred.

## Route

Only stage 01 has a project note. Create each later stage's note when the previous one closes, and only if the user still wants it. Sequence is intent, not an enforced dependency.

| Stage | Question it answers | Mechanism | Change in the plugin | Checkpoint |
| --- | --- | --- | --- | --- |
| 01 Strict flags | What can be `undefined` here, and who handles it? | Narrowing, `null`/`undefined`, optional properties, reading compiler errors | Enable `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes`; fix all reported errors | Explain TS2532, TS18048, TS2345, TS2322, and when a guard, `??` or `!` fits |
| 02 Domain types | Can the types rule out a wrong value before it runs? | Literal and discriminated unions, `never` exhaustiveness, branded and template literal types, `satisfies` | Branded ISO dates, typed location keys, `assertNever` in action/effect switches, `expectTypeOf` tests | Add a union member and show every switch the compiler forces you to update |
| 03 Decoders | How does data of unknown shape become a trusted type? | Generics, constraints, `keyof`, mapped and conditional types, `infer` | A small `Decoder<T>` library replacing the adapter casts and frontmatter checks | Explain the difference between the static type and the runtime check, using one invalid frontmatter value |
| 04 Boundaries | Where does `unknown` stop in a program that calls another plugin? | `unknown` vs `any`, type guards, `.d.ts` files, module augmentation | A declaration file for the Tasks plugin API slice and its workspace event | Show what breaks, and where, if that API changes shape |
| 05 Async and errors | What happens when a write fails halfway? | Promises, floating promises, result types vs exceptions | Make the line editor's and adapters' failure cases explicit in types | Trace one stale-line failure from the click to the notice |
| 06–07 Framework-free UI (optional) | What does a UI framework do for you? | DOM types, typed events, keyed lists, UI state ownership | Decide by ADR first; rewrite `TaskRow`, then `Section` and `Panel`, in plain TypeScript | Compare bundle size and behavior with the Svelte version and justify keep-or-switch |
| 08 Tooling and performance (optional) | What do `tsc` and esbuild each actually do? | `isolatedModules`, `moduleResolution`, type stripping, profiling | A TypeScript stress-test generator for the dev vault; profile one refresh | Explain one measured cost and one compiler option's effect |

Stages 04 and 05 reinforce Section 3's typed provider boundary and Section 5's worker failure handling. Stages 06–07 overlap with the GUI project's client-state questions, but they do not replace its T3/Paseo work.

## Teaching method

Same as the course: one concrete question, a small example, the learner's prediction or attempt, the smallest useful hint, then the learner's own explanation. The learner writes the fixes; Claude explains and reviews but does not write the solution. Record date, focused minutes, what changed, the explanation, a commit link and one open question in the Obsidian project's progress log. A passing build is not a checkpoint.

## Plugin rules the lab must keep

Work on a branch from `pipeline` in the plugin checkout. Test only in the dev vault (`~/Projects/taskflow-demo-vault`), never the live vault. Never run `deploy:prod` or `release:*` as part of an exercise. The plugin's `AGENTS.md`, `CONTEXT.md` and `docs/adr/` define its vocabulary and design rules.

## Stage 01 preparation

Measured September 28 at plugin commit `7b95718`: `noUncheckedIndexedAccess` reports 63 errors (28 in `src/`: `move.ts` 11, `actions.ts` 5, `order.ts` 5, `hierarchy.ts` 5, `note-edit.ts` 2; 35 in `tests/`, mostly `pacing.test.ts` and `classify.test.ts`). `exactOptionalPropertyTypes` reports 8 (`settings.ts` 3, `ui/prompts.ts` 2, `core/actions.ts` 1, `adapters/tasks-plugin.ts` 1, `tests/hierarchy.test.ts` 1). Remeasure at entry; the counts change with the code.

Start with `src/core/hierarchy.ts`, the smallest file. Ask the learner to predict what `items[i]` can be before revealing the error. If they reach for `!` everywhere, ask them to show why the value cannot be missing at that line.

## Open decisions

- Activation date, and which planned course hours it replaces.
- Whether stages 02–08 happen at all, decided after stage 01's evidence.
- Stages 06–07 need an ADR in the plugin repo that supersedes ADR-0002 (Svelte 5 stack) before any rewrite.
