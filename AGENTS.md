# Course work

For teaching, course planning, new study ideas or course projects, read [the charter](course/CHARTER.md) and [the roadmap](ROADMAP.md). For a new idea, follow [idea intake](course/IDEAS.md); for assessment, use [the rubric](course/ASSESSMENT.md). Check the owning Obsidian note before assigning work or recording progress. [Project context](PROJECT-CONTEXT.md) identifies the live entry point.

Maintain the agreed 15-hour weekly budget and preserve demonstrated learning. Routine material selection and equivalent exercise substitutions are delegated to the teacher. Changes to required milestones, core outcomes or agreed milestone deadlines need student agreement under the charter's change process. Teach through learner attempts and feedback; planning does not authorize completing the student's exercises.

# Obsidian CLI connection

If `obsidian` reports `The CLI is unable to find Obsidian`, retry the same read-only command using the tool's approved `require_escalated` execution path before diagnosing app state, registration, or iCloud. Follow the execution tool's approval policy; a rejection is not permission to bypass it.

On 2026-09-09, `obsidian help` failed inside the sandbox and succeeded outside it. An approved `obsidian vault=obsidian-vault read path=Projects/Active/terminal-human-in-the-loop.md` also succeeded against the iCloud vault. This error can therefore indicate blocked app communication, even when Obsidian is running and registered.

After recovering the connection, verify the requested note through the CLI. If the approved retry also fails, investigate the running app and CLI registration before considering vault storage changes.
