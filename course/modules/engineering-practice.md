# M11 — engineering practice with Git, GitHub and agents

Required topic added at the student's explicit request on September 28, 2026. M11 is a stable ID added to the existing roadmap, not the eleventh item in chronological order. Introduce its fundamentals alongside M2, demonstrate its full delivery cycle with M3/M4, and reuse it through M10.

## Purpose and boundary

Be able to define a small change, give it to an agent or implement it, inspect the exact result, test its behavior, request corrections, recover a mistake and accept the deliverable with evidence. Reviews reduce risk and reveal mistakes; they do not guarantee defect-free software.

The central workflow is **brief → small change → verification → review → acceptance → authorized integration → recovery when needed**. The lesson is the reasoning behind the workflow, not memorizing skill names or imposing every ceremony on every edit. Use small changes, explicit contracts, separation of responsibilities, readable code and proportionate tests/review. An ADR belongs to a meaningful architectural tradeoff; a typo does not require one.

## Concepts we will make concrete

| Concept | What the student should be able to explain |
|---|---|
| Git versus GitHub | Local version history versus hosted collaboration; repository, working tree, staging area, commit, branch, HEAD and remote |
| Issue/spec/acceptance criteria | The problem, boundaries and observable examples that decide whether a result meets the request |
| Pull request (PR) | A proposed branch change relative to a base, carrying discussion, checks and review; opening it is not merging or deploying |
| Code review | Assess both the requested behavior and the repository's design/quality standards, using the actual changed code and evidence |
| CI | Automated checks on a particular revision; a green result only establishes what those checks cover |
| ADR | A short record of an architectural decision, its context, alternatives/tradeoff and consequences; supersede a decision without erasing its history |
| TDD | Develop observable behavior using a failing test, a minimal passing implementation and deliberate refactoring while preserving behavior |
| Refactoring | Change structure while preserving intended behavior; separate it from feature changes so the diff remains reviewable |
| Recovery | Choose a response based on what changed, what was saved, whether history was shared and whether external effects occurred |
| Deliverable acceptance | A decision that the requested result meets its criteria at an identified revision; distinct from PR approval, merge, deployment and learner mastery |

## Learning sequence and tests

| Unit | Placement | Learn and practice | Evidence required |
|---|---|---|---|
| E1. Inspect and preserve work | Begin alongside M2, before substantial agent edits | Read status/diffs/history; distinguish staged, unstaged and untracked files; make a focused commit on a branch; identify base/head and unrelated work | Predict what a commit includes and demonstrate that unrelated work is preserved |
| E2. Recover mistakes | After E1, still early | Unstage without discarding; restore a deliberately saved fixture; recover a reachable lost commit using reflog; revert a shared change; resolve a small conflict by intent | Choose and explain a recovery method for three different scenarios, then verify the restored behavior |
| E3. Specify and test behavior | With the M2 runner or M3 agent | State in/out scope and acceptance examples; choose a public test boundary; observe a failing test, make it pass, then review a behavior-preserving refactor | Show a meaningful red result, green result and an unseen variation; explain why a test can pass while the requirement fails |
| E4. Record design decisions | When M3/M4 presents a real choice | Trace responsibilities, compare alternatives, write one compact ADR when justified; distinguish a decision from a task plan | Defend the choice, consequences and a condition that would justify superseding it |
| E5. PR, review and CI | Before accepting agent-generated project changes | Write a focused PR description; choose the review base/head; inspect committed and uncommitted scope; review spec and standards; classify blocking findings versus suggestions | Find a seeded defect, cite its trigger and consequence, request a concrete correction and recheck the changed revision |
| E6. Accept, integrate and recover | By the M3/M4 delivery exercise; repeat through capstone | Assemble an acceptance packet; distinguish accept/revise from merge/deploy authority; verify integration and a recovery plan | Accept or reject the candidate against evidence, explain residual limits, then complete a controlled rollback/recovery drill |

Initial estimate: **12–18 focused hours**, distributed across core study/labs and existing project review time; reassess after E1/E2. This is additional curricular scope within the same 15-hour weekly capacity, not a claim that the old dates can absorb it. Select a short engineering lesson in the current core allocation when it helps the active work, displacing an equal amount of planned study. Keep one primary module and one project. Existing deadlines await the shared reforecast rather than moving silently.

## Mistake-recovery cases

Before taking action, inspect status, identify what must be preserved and make a recoverable checkpoint for the intended scope. Practice in a disposable teaching repository; do not use this dirty classroom or a live product as a destructive-command sandbox.

| Situation | Reasoning to demonstrate |
|---|---|
| Wrong file staged | Change the index while retaining working-file contents |
| Unwanted uncommitted edit | Inspect and preserve needed work before restoring a known version; untracked/never-saved content is not guaranteed recoverable by Git |
| Local commit on wrong branch or lost branch reference | Locate the commit and recover a branch/reference before rewriting anything; explain that reflog is local and time-limited, not a universal backup |
| Faulty change already shared | Use a history-preserving corrective/revert change when appropriate; rewriting shared history affects collaborators |
| Merge/rebase conflict | Explain both sides' intent and verify the result rather than blindly choosing one side |
| Bad deployed behavior or changed data | Code reversal alone may not undo data migrations or external actions; define restore/compensation and acceptance separately |

Reset/restore/revert/rebase are not synonyms. Explain which state each affects before using it. Commands that discard work or rewrite shared history need a deliberate scoped choice, not an automatic “fix everything” recipe. Detailed commands are taught against the disposable lab's observed state.

## Review and acceptance packet

Each substantive delivery identifies the request/spec, exact base and candidate revision, changed paths, scope exclusions, acceptance examples and their observed results, checks with commands/environment, review findings and resolution, residual risks/limits, and recovery method. The human disposition is **accept** or **revise**, with a reason. An approved PR or green CI badge alone does not replace this packet.

Review two questions separately: does the result meet the requested behavior, and does its implementation meet the repository's standards? Add concrete failure cases and inspect whether tests exercise them. Agent self-reports and repeated model agreement are evidence to examine, not independent proof.

If changes occur after review, identify the new revision and recheck affected evidence before acceptance. Passing learner assessment additionally requires the student's own explanation and unfamiliar modification under the [course rubric](../ASSESSMENT.md).

## Using Matt Pocock's skills consciously

Use the [engineering reading map](../../materials/engineering-practice.md) to connect the installed skills to their underlying concepts. Read each applicable skill before use and understand what input, authority and evidence it assumes.

The inspected local TDD skill uses red → green slices and places refactoring in review; conventional descriptions often use red → green → refactor. Teach that distinction explicitly. Its test boundaries must be agreed before writing tests when that skill is invoked.

The inspected local code-review skill uses `git diff <fixed-point>...HEAD`: that comparison omits unstaged, staged-but-uncommitted and untracked work. An exercise must make the reviewed scope explicit and account for those states separately. A skill reporting no findings on the wrong diff is not acceptance.

This module studies skills as workflow examples; it does not install/reconfigure them, run a code review, commit the classroom or create a GitHub PR. The later learner lab can use a designated exercise repository and separately authorized remote actions.

## First lesson

Bring one small agent-produced change or a teacher-provided fixture. Before accepting it, identify the requested behavior, the files/revision being reviewed, the evidence that would convince you, and how to recover a mistake. Start with read-only Git inspection and a prediction; prepare the hands-on fixture only when the lesson begins.
