# M16 — Programming paradigms and design

Required by the student's explicit agreement “同意加上编程范式与设计吧”, September 30, 2026. This closes the FP/OOD gaps recorded in v1.5. The [roadmap](../../ROADMAP.md) owns requirements; [workload](../WORKLOAD.md) counts overlap; Obsidian owns execution dates, tasks and evidence. Practical system design remains required through M3/M4/M7/M10/M11.

## Placement and scope

Begin after the relevant M2 functions, collections, classes/interfaces and error-handling checkpoints, using the M3 small program as the design subject. Python examples connect to existing experience; TypeScript is the default comparison language so language differences do not confound the FP/OOP comparison. P3's Rust transfer follows M12 R1; it does not delay initial FP/OOP lessons. Use M15 DM1 contracts/invariants when helpful without requiring the whole mathematics milestone first.

M16 adds assessed design reasoning, not a second language-syntax course. Credit existing M2/M3/R1 evidence for syntax and previously demonstrated design criteria. M3/M4 can begin before full M16 completion; introduce a relevant block before its design decision. M16 evidence is required by the final M10 defense. Keep one primary module and one active project.

## Required blocks — 24–36 directed hours

Hours include selected readings, explanation, learner attempts, implementation and assessment. Estimates are provisional additional effort beyond existing language lessons, not a claim to cover all programming-language theory.

| ID | Concepts and hours | Required evidence |
|---|---|---|
| P1 | Functional programming, 6–9h: pure functions, referential transparency, immutable updates and aliasing, higher-order functions/closures, composition, map/filter/fold, eager versus lazy iteration, explicit effects | Extract a deterministic state transition from an existing task/agent component; pass clock/randomness/I/O results explicitly. Test no input mutation and repeatable outputs; explain a captured mutable-state counterexample. Separate calculation from effect execution and explain the allocation/readability costs of the chosen approach. Closure syntax alone does not demonstrate purity. |
| P2 | Object-oriented design, 6–9h: encapsulation, invariants, responsibilities, identity/state, interface-based polymorphism, composition/delegation versus inheritance, behavioral substitutability, cohesion/coupling and dependency inversion | Implement the same bounded behavior with objects and two substitutable policy implementations. Verify the shared behavioral contract, explain an inheritance/substitution failure, and compare a composition alternative. Introduce a pattern only for an observed design pressure; naming patterns or drawing classes is insufficient. |
| P3 | Types and cross-language design, 4–6h: product/sum types, discriminated unions/enums, exhaustive matching, explicit errors, generics versus runtime polymorphism, Rust traits/trait objects and closure capture | Model valid task states and explain which invalid states are excluded by types and which still need runtime checks. Port only the small policy/state core to Rust after R1; compare enum dispatch with a trait-based design, including ownership and dispatch tradeoffs. Rust does not supply class inheritance; traits alone are not a complete OOD education. |
| P4 | Comparative design and change, 8–12h: functional core with effectful boundary, object boundaries, testability, extension costs and design judgment | Apply two teacher-selected changes to the FP and OOP variants using the same observable contract and fixtures. Report touched responsibilities, state ownership, tests and failure behavior; justify the final design, which may combine both styles. Explain one unfamiliar change independently. Reuse M11 review/ADR practice rather than repeating its introduction. |

## One shared experiment, bounded slices

Use a small **task lifecycle and retry-policy component** from the existing runner/agent. At activation freeze its inputs, outputs, state transitions, retry limits and error behavior. Its teaching fixture uses supplied timestamps and fake execution results; it needs no real worker, network service or broker. Retry policy here is a design example, not credit for M7's distributed guarantees.

The learner develops two small variants against one contract: a functional state-transition core and an object/policy-based model. A baseline procedural version can be the existing artifact; no third greenfield build is required. Candidate later changes include a new terminal state, an additional retry policy, or an audit-effect requirement. The teacher selects the actual unseen change during assessment rather than preparing its solution now.

Each practical slice must fit its allocated project time and finish within 21 days: first one variant with fixtures, then the other against the same fixtures, then the small Rust transfer/change defense as needed. Target at most 6–9 project hours per slice, splitting further when diagnosis warrants it. Their work is already inside P1–P4, not an extra lab surcharge. Theory uses core/lab hours; do not place all 24–36h into one three-hour/week project. Reuse the current project owner for a small integrated exercise; create a separate owner only when a bounded slice is activated.

## Assessment and limits

Use the shared [rubric](../ASSESSMENT.md): learner-authored working behavior, explanation and unfamiliar modification. Require evidence of state/effect boundaries, substitutability, the limitations of static types, and an explicit design tradeoff. Passing identical fixtures supports equivalence only for those cases, not a proof of all behavior. Measure performance only if claiming an advantage; count test or edit differences as observations, not universal design laws.

System design already assesses service/storage/coordination boundaries. M16 addresses design inside and between program components; M10 should connect those decisions to the system's operational requirements. A style is not inherently superior. Do not force every function into a class or every effect into a framework.

Effect adoption, Haskell/OCaml courses, category theory, advanced type-level programming, a full design-pattern catalog, full Grokking OOD completion and interview problem banks remain optional. Compiler theory belongs to M12. The teacher prepares prompts, source selections, hints and review; this planning change does not complete learner exercises.

## Selected primary sources

Official pages inspected September 30, 2026. Assign exact sections and verify the active language/toolchain at lesson preparation. Our shared experiment and hour estimates are course-authored adaptations, not completion claims for these sources.

| Source | Role | Boundary |
|---|---|---|
| [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html) | P1 familiar-language bridge: functional decomposition, iterators/generators and composition | Read selected concepts; a second Python course is not required. |
| [TypeScript Handbook: Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html) | P2 language semantics for state, visibility, interfaces and inheritance | Reuse prior syntax evidence; design principles and the comparison exercise require separate reasoning. |
| [Rust Book: Iterators and Closures](https://doc.rust-lang.org/book/ch13-00-functional-features.html) | P1/P3 closure capture and iterator-based composition | Rust's functional features do not make all Rust code pure. |
| [Rust Book: Object Oriented Programming Features](https://doc.rust-lang.org/book/ch18-00-oop.html) | P2/P3 selected encapsulation, polymorphism and state-design comparison | Use after R1; do not prescribe class inheritance in Rust. |

[Grokking OOD](../../materials/ood-assessment.md) remains a targeted optional reference even though the underlying P2 design outcomes are now required. No purchase, installation, deployment, new schedule or learner completion follows from this module's inclusion.
