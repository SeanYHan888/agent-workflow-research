# Grokking OOD: targeted optional reference

**September 30 scope update:** [M16 programming paradigms and design](../course/modules/programming-paradigms.md) now requires OOD outcomes and an FP/OOP comparison. This particular Grokking resource remains optional. The September 11 scope/time statements below are historical; the current [roadmap](../ROADMAP.md) and [workload](../course/WORKLOAD.md) supersede the old 160-hour boundary.

Assessed September 11, 2026. Local checkout: `/Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview`, initially commit `3d35276091bcc84027c91935912b1f9e29d987c0`, refreshed to `ba7927f641f26a189ddfc4679aba527b170cd0b8`. Recommendation based on the index, UML notes, and representative library/OOP examples; this is not an exhaustive review.

**Include it on the material shelf as targeted optional reading in Sections 3 and 5.** Its useful contribution is practice identifying responsibilities, interfaces, relationships, and message order. Completing its interview case studies would add a separate goal to our existing agent-building course. Keep the [160-hour roadmap](../ROADMAP.md) and [settled course sequence](../teaching/DECISIONS.md); use these readings only within an existing design-reading allocation when they resolve a concrete gap.

## Refresh correction — September 11

The pull brought 25 commits, including newer Java/Python implementations, a library demo and tests. Our selected OOAD, class-diagram and sequence-diagram readings are unchanged. The root README still carries a broad non-executable warning, while the new library README describes an executable implementation; neither that claim nor its tests were validated by this pull. Use a mix-of-sketches-and-implementations description going forward. Optional reading placement and existing hours remain unchanged. See [the refresh report](versions.md) for revisions and the unrelated Java README filename collision.

## Initial assessment before the refresh

The [local readme](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/readme.md>) lists OOP/UML introductions and 16 interview-style case studies. It describes itself as an extension of another course with Python examples, and explicitly says examples outside OOP basics are not executable. The [current upstream readme](https://github.com/tssovi/grokking-the-object-oriented-design-interview) retains that limitation. Treat the repository as third-party teaching notes and sketches, not the original commercial course or production implementations. The local readme attributes Educative; current upstream links Design Gurus. This assessment does not equate their content or access.

The checkout also has a `docs/` presentation of the material. Use the root reading paths below consistently so duplicate pages do not become separate assignments. Upstream now lists additions absent from this checkout, including a tests directory; that is not evidence that the local examples work or were tested.

## Selected readings and course application

| Timing | Exact reading | Bounded application |
|---|---|---|
| Section 3, after basic TS interfaces | [Object Oriented Analysis and Design](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-and-uml/object-oriented-analysis-and-design.md>) and selected parts of [Class Diagram](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-and-uml/class-diagram.md>) | Optional 20–30 minutes. Name who owns tool registration, input validation, execution, and stored messages. Draw only those relationships; explain which component can change which state. |
| Section 5, before worker-adapter implementation | [Sequence Diagram](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-and-uml/sequence-diagram.md>) | Optional 20–30 minutes. Draw coordinator → adapter → child process → event consumer, including failed startup and cancellation. Identify who reports completion and who verifies the result. |
| Only if responsibilities remain unclear | [Library Management System](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/object-oriented-design-case-studies/design-a-library-management-system.md>), requirements and class responsibilities only | Optional analogy: distinguish a description from an individual instance, then distinguish a tool definition from a tool call and a task from a worker run. Stop before implementing the library. |

These are instructor-selected timeboxes, not measured completion estimates. Skip them when the learner can already explain the corresponding design. No whole-repository reading, separate Python OOP project, or new course phase is needed.

## Bridge into our TypeScript build

Use [official TypeScript Object Types](https://www.typescriptlang.org/docs/handbook/2/objects.html) for interfaces and object-shaped contracts, and [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions) for distinct result/event variants. Our exercise should express a tool's input/output contract and a worker's running/succeeded/failed/cancelled outcomes, then demonstrate one actual failure path. This is a proposed application of those language features, not an implementation supplied by the OOD repository. Introduce a class only when it helps manage behavior and state; the diagrams do not require an inheritance hierarchy.

## Teaching limitations observed before the refresh

At the initial revision, the [library models](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/example-codes/library-management-system/models.py>) contain `None` method bodies and references to methods not defined there. The [catalog search](</Users/seanmacbook/Self-learn/grokking-the-object-oriented-design-interview/example-codes/library-management-system/search.py>) describes substring matching in a comment but implements an exact dictionary lookup. These are useful critique exercises only after the learner understands the intended behavior; they are unsuitable as working solutions to copy.

The introductory UML prose contains broad simplifications. Use the diagrams as communication aids and consult the [OMG UML specification](https://www.omg.org/spec/UML/2.5.1/About-UML) if exact notation semantics matter. Do not make UML standard memorization a checkpoint.

## Progress ownership

This file records a resource recommendation. Existing Obsidian project notes remain the source of truth for current progress, next phases, tasks, and completion evidence. Adding this reference does not complete or activate a phase. If a selected reading is assigned, record its actual explanation/diagram evidence in the existing Section 3 or Section 5 project note; the Obsidian reading room should link to the material, not create a second progress tracker.
