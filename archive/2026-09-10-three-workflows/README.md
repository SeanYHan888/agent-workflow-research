# Before integrating the three workflow projects

September 10, 2026 snapshot of the nine existing Obsidian project notes and three repository course documents. These contain the previous schedule; current dates are in ROADMAP.md and Projects/coding-agent-course.md in the vault.

The integration preserved all 53 original tasks exactly once, including completion states, wording and dates; it added nine GUI/team checkpoints. The new course overview has no checkboxes. See task-audit.json.

Verification after applying:

- All ten notes matched staged contents through filesystem and Obsidian CLI readback.
- Obsidian's metadata cache recognized start, deadline, status and order for all nine Active notes; every course-overview wikilink resolved.
- Installed and running Taskflow was 0.5.6. Its live panel showed the course projects in the planned order, with future start labels: GUI 01-18, worker 02-08, Linux 03-08, team 04-19. Active count was 2/3.
- No study checkpoint was marked complete. No plugin settings, templates, Calendar events or application installations were changed by this integration.

Taskflow's project reader uses start, not start_date. The course notes were migrated to the supported key. Dependency links are course guidance; the plugin does not enforce them.
