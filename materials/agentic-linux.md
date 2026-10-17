# T3 Code and Omarchy Quattro — source map

Checked October 4, 2026. These are sources for [M17](../course/modules/agentic-linux.md) and the [distribution capstone](../course/projects/agentic-linux-distribution.md). They are not completion records. Record a commit or release and exact files before assigning a source trace; the moving `main` links below are entry points, not pinned lesson versions.

| Primary source | Verified scope and teaching use |
|---|---|
| [T3 Code repository](https://github.com/pingdotgg/t3code) | Describes an interface for controlling agent harnesses, with desktop, web and mobile clients. Use it to locate current providers and packages. |
| [T3 Code internals](https://github.com/pingdotgg/t3code/blob/main/docs/internals/overview.md) | Entry point for T1's request/state ownership trace. Verify the selected implementation against the documented architecture. |
| [Linux background service](https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md) | Primary entry for T2 service lifecycle study. Read the current commands and service scope before the lab. |
| [Omarchy Quattro v4.0.0 release](https://github.com/omacom/omarchy/releases/tag/v4.0.0) | Documents the Quickshell-based desktop, plugin structure and move of internals to system packages. Use this release as a historical architecture reference. |
| [Current Omarchy manual](https://omarchy.org/manual/) | User documentation for the supported release. Select installation, configuration and recovery sections after choosing the test target. |
| [Omarchy source](https://github.com/omacom/omarchy) | Locate code for Q1/Q2 and record the inspected revision. The old `basecamp/omarchy` release URL redirects to this organization. |

The old [Omarchy 3 manual](https://learn.omacom.io/2/the-omarchy-manual) identifies itself as legacy and links to the Quattro manual. Do not use v3 configuration instructions as proof of v4 behavior.

## T3OS status

The student clarified on October 4: “they havent publish it yet they are just teasing it”. Keep T3OS as a future comparison. This review did not verify an official release, specification or release date. Do not infer architecture or compatibility from the name. Recheck at M17 entry or when the student supplies an announcement; there is no background monitoring task.

## Assigning a lesson

Start with one learner question and one source path. Retain the existing GUI project's T3 Code trace and its narrow framework-reading bridge. For Quattro, learn only the shell language and APIs needed for the selected action. The final comparison should identify what the student's distribution adds, which upstream parts it reuses, and how its behavior can be tested.
