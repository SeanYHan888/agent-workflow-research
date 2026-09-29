# Oracle folder migration and retirement

Completed September 28, 2026 following the student's request to move needed Oracle/VPS material into this workspace and delete the old folder. This supersedes the earlier keep-folder recommendation, preserved in the [pre-migration snapshot](../archive/2026-09-28-before-brokers-vps-migration/research/oracle-folder-retirement.md).

## Preserved and migrated

| Item | Verified result |
|---|---|
| Original file inventory | Exactly STATUS.md; no code, hidden files, symlinks or Git repository in the original folder |
| Source preservation | [Original STATUS.md](../archive/2026-09-28-oracle-project-source/STATUS.md) matches byte-for-byte; SHA-256 `d4158bc919e47e8950ea046cf95aa0b87dccd111650fbe2b11e3f09002dc08a8` |
| VPS recommendations | [Original September 24 recommendation messages](../archive/2026-09-28-oracle-project-source/vps-recommendation-excerpts.md) preserved with source turn IDs; [current comparison](../operations/vps/provider-options.md) separates historical offers from the September 28 OVH/Akamai public-page refresh |
| New operational owner | [VPS operations home](../operations/vps/README.md), with current STATUS.md; course execution tasks still belong to the existing Obsidian Linux note |
| Capacity monitor | Existing `oracle-free-vps-capacity` retargeted to this course chat, `01a0ea2f-b212-7d43-8e27-c936b83dad7a`; PAUSED and daily 09:00 rule retained; read-only scope retained and new evidence paths added. Target and status verified in saved configuration after the tool update. |
| Old chat | **Plan Oracle Cloud Free VPS setup**, `01a0c09c-e6df-7391-9bad-1fd159c7d752`, archived through the app tool. History remains recoverable; future work belongs here. |
| Original folder | Moved to `/Users/seanmacbook/.Trash/oracle-vps-retired-2026-09-28` after inventory/hash checks. Verified `/Users/seanmacbook/Peronsal/oracle-vps` no longer exists and the Trash copy still matches the archive. Trash was not emptied. |
| Saved project entry | The old `oracle-vps` registration (project ID `93f89e09-a6a0-4f98-9360-ee6193074dfa`) has no exposed removal API. Native computer-use access to Codex was blocked by the tool. The stale sidebar project entry may therefore remain; remove it manually in the app. It is not the monitor's target or a required operational dependency. |

No cloud account/resource action, provisioning, broker installation or SSH-key change occurred. The key referenced by the original record lives outside the removed folder and was not read or copied. The shared web-chat link previously returned “Shared chat not found”; the source messages above came from the accessible local chat, without claiming the two are identical.

## Continue here

Use [operational status](../operations/vps/STATUS.md), [provider options](../operations/vps/provider-options.md) and the [learning roadmap](../course/projects/vps-lab-roadmap.md). Current cloud capacity and checkout costs remain unverified. Resuming the old archived chat would require restoring its cwd; restoring that chat is unnecessary for continuing the migrated project here.
