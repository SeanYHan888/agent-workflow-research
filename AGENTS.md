# Course work

For teaching, course planning, new study ideas or course projects, read [the charter](course/CHARTER.md) and [the roadmap](ROADMAP.md). For a new idea, follow [idea intake](course/IDEAS.md); for assessment, use [the rubric](course/ASSESSMENT.md). Before assigning work or recording progress, find the owning Obsidian note through [progress owners](my-progress/OWNERS.md) and read it. [Project context](my-progress/PROJECT-CONTEXT.md) identifies the live entry point.

Maintain the agreed 15-hour weekly budget and preserve demonstrated learning. Routine material selection and equivalent exercise substitutions are delegated to the teacher. Changes to required milestones, core outcomes or agreed milestone deadlines need student agreement under the charter's change process. Teach through learner attempts and feedback; planning does not authorize completing the student's exercises.

## Repository layout

- The course is shareable: `ROADMAP.md`, `course/`, `materials/` and `teaching/` are written for any learner. Put this learner's schedule, dates, Obsidian links, owner status, ideas, personal projects, VPS operations and practice work in `my-progress/`; course pages state the general rule instead.
- Each milestone's guide is in [course/modules/](course/modules/README.md); add milestone material there and in `materials/`.
- Third-party sources are pinned Git submodules under `materials/sources/`. Read them in place; change a pin only as a recorded material change in [materials/versions.md](materials/versions.md).
- Git history is the snapshot record. Before a curriculum change, commit the current state and cite that commit in [the decision record](course/DECISIONS.md); [HISTORY.md](HISTORY.md) locates earlier snapshots.
- Link repository files with relative paths.

## Project-first teaching

- Start from a useful behavior in the evolving agent-first Linux project. Select one small build, debugging task or experiment from the [project route](ROADMAP.md#project-route); use an isolated foundation lab when it makes the mechanism easier to learn.
- Before teaching, name the deliverable, one observable acceptance check, the learner's next action and the timebox. Follow the [session workflow](teaching/README.md#prepare-and-teach); finish with observed output, the learner's explanation and one next step.
- Have the learner predict, implement or investigate first. Give the smallest useful hint, then introduce the concept or source passage needed to continue. Use worked examples when requested; keep assessment evidence tied to the learner's own reasoning.
- Make building, debugging and experiments the majority of normal session time. Reading supports the current question; retain explicit resource-completion goals and required assessments. A whole subject is an entry gate only where the roadmap requires it.
- Reuse the runner, agent, worker and service across modules. Scope each execution project to a useful result within 21 days at its allocated capacity; count shared work once. Keep tasks and evidence in their existing Obsidian owner.
- Expand only the next ready slice. Course planning produces briefs and teaching prompts; it does not complete the learner's implementation, activate infrastructure or establish mastery.

# Obsidian CLI connection

If `obsidian` reports `The CLI is unable to find Obsidian`, retry the same read-only command using the tool's approved `require_escalated` execution path before diagnosing app state, registration, or iCloud. Follow the execution tool's approval policy; a rejection is not permission to bypass it.

On 2026-09-09, `obsidian help` failed inside the sandbox and succeeded outside it. An approved `obsidian vault=obsidian-vault read path=Projects/Active/terminal-human-in-the-loop.md` also succeeded against the iCloud vault. This error can therefore indicate blocked app communication, even when Obsidian is running and registered.

After recovering the connection, verify the requested note through the CLI. If the approved retry also fails, investigate the running app and CLI registration before considering vault storage changes.
