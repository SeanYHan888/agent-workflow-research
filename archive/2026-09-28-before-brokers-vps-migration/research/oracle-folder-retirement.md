# Oracle project folder — retirement assessment

Inspected September 28, 2026 in response to “can I delete the Oracle project folder now?” This is a dependency assessment and preservation step, not authorization to delete files or alter an automation.

## Findings

| Item | Observed evidence | Consequence |
|---|---|---|
| Directory contents | `/Users/seanmacbook/Peronsal/oracle-vps` contains only STATUS.md in the current listing; no Git repository was present | No implementation tree needs migration, but the status record needed preservation |
| Preserved source | [STATUS.md](../archive/2026-09-28-oracle-project-source/STATUS.md) copied byte-for-byte, with [hash manifest](../archive/2026-09-28-oracle-project-source/manifest.json) | Course knowledge no longer depends on the sole original copy |
| Registered project | Codex lists `oracle-vps` at the original path, project ID `93f89e09-a6a0-4f98-9360-ee6193074dfa` | Deleting a folder does not remove its app registration |
| Existing chat | **Plan Oracle Cloud Free VPS setup**, `01a0c09c-e6df-7391-9bad-1fd159c7d752`, has the original path as cwd; status was `notLoaded` | Resuming it after deleting the cwd can fail; notLoaded is not an OS process inventory |
| Capacity monitor | Local `oracle-free-vps-capacity` configuration is `PAUSED` and targets that chat | It is not presently scheduled to run, but resuming it would retain the old workspace association |
| External credentials/cloud state | Not inspected or changed; STATUS.md references a key outside the folder | Deleting this folder is neither key cleanup nor Oracle account/resource deletion |

The automation view tool was also invoked; its result rendered a card rather than returning structured state. The PAUSED finding comes from the current local automation.toml, not the older STATUS.md description of daily checks.

## Recommendation

Keep the folder until the old chat/monitor is deliberately retired or its execution context is migrated. The data preservation step is complete, but the app dependency is not. Moving the directory to Trash would preserve file recoverability while still breaking a future resume at that path.

To retire it cleanly, decide whether the monitor is still wanted. If wanted, establish its new supported chat/workspace target and update it while preserving its paused state, scope and notification policy, then verify the association. If unwanted, explicitly retire the monitor and the old project/chat as appropriate. Remove the stale project entry and only then remove the folder. Do not infer authorization to delete the Oracle account, keys or cloud resources from a local-folder cleanup request.

No monitor update, project removal, chat archival, folder deletion or cloud action was performed by this assessment. The [course VPS roadmap](../course/projects/vps-lab-roadmap.md) and preserved record remain usable here.
