# Git, GitHub and engineering-practice readings

For [M11](../course/modules/engineering-practice.md). Sources inspected September 28, 2026. Selections and exercises are the course's design; exact commands and repository rules are checked at the lesson. Read a narrow selection, perform the related exercise, then explain it.

| Material | Assigned use |
|---|---|
| [Pro Git: Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) and its linked basics/branching chapters | E1/E2: index versus working tree, focused changes and deliberate undo; avoid treating all recovery operations as interchangeable |
| [Git revert](https://git-scm.com/docs/git-revert) | E2: reverse a recorded change through a new commit; distinguish correction from rewriting history |
| [Git reflog](https://git-scm.com/docs/git-reflog.html) | E2: inspect local reference history and its limits in recovering a saved commit |
| [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) | E5: branch, focused commits, PR, review and merge as distinct steps |
| [GitHub pull request reviews](https://docs.github.com/en/pull-requests/reference/pull-request-reviews) | E5/E6: comment, approve and request changes; review state and applicable repository rules |
| [Google: what to look for in code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | E5: inspect design, behavior, complexity, tests and clarity; connect findings to concrete consequences |
| [Michael Nygard: Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | E4: retain decision context and consequences so future changes can be reasoned about |
| [Martin Fowler: Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) | E3: understand the small feedback cycle and distinguish it from writing tests after implementation |
| [Matt Pocock's engineering skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/README.md) | Map the workflow to its concepts; compare installed instructions with upstream rather than assuming they are identical |

## Installed examples inspected

The follow-up [Matt Pocock workflow survey](../research/matt-pocock-skills-course-fit.md) inspects eleven upstream skill bodies at a pinned revision and confirms that all eleven installed copies match. It maps the workflow to M11 and explains a composition hazard: review before committing can miss the implementation when the review only compares committed `...HEAD` changes. Use this as an E5 exercise in checking the exact review scope.

- [Local TDD skill](</Users/seanmacbook/.agents/skills/tdd/SKILL.md>): behavioral tests through agreed public boundaries; small red/green slices; refactoring assigned to review in this installed version.
- [Local code-review skill](</Users/seanmacbook/.agents/skills/code-review/SKILL.md>): specification and standards as distinct review axes, using a named comparison base.
- [Local domain-modeling skill](</Users/seanmacbook/.agents/skills/domain-modeling/SKILL.md>): precise vocabulary and sparing use of ADRs for meaningful tradeoffs.

These are reading references for this curricular update, not invocations of their implementation/review procedures. During a real exercise, honor the applicable repository instructions and the selected skill's actual scope. Running a skill does not establish that its prerequisites were met or its output was accepted.
