# Obsidian CLI connection

If `obsidian` reports `The CLI is unable to find Obsidian`, retry the same read-only command using the tool's approved `require_escalated` execution path before diagnosing app state, registration, or iCloud. Follow the execution tool's approval policy; a rejection is not permission to bypass it.

On 2026-09-09, `obsidian help` failed inside the sandbox and succeeded outside it. An approved `obsidian vault=obsidian-vault read path=Projects/Active/terminal-human-in-the-loop.md` also succeeded against the iCloud vault. This error can therefore indicate blocked app communication, even when Obsidian is running and registered.

After recovering the connection, verify the requested note through the CLI. If the approved retry also fails, investigate the running app and CLI registration before considering vault storage changes.
