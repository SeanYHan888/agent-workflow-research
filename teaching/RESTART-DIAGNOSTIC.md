# JS/Node restart diagnostic

Teacher preparation, September 28, 2026. Use at the student's first study session after the break; there is no relocation/conference-break assignment (September 28–October 11); the confirmed restart is October 12. The [JS/Node project](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-02-javascript-node.md>) owns scheduling, attempts, artifacts and results. This sheet contains prompts, not a second task checklist or a completed assessment.

## First 45 minutes

**0–10 minutes — recover evidence.** Inspect the learner's last Boot.dev JS checkpoint and their latest script. Ask what they can explain without assistance and where they stopped. Retain M1 and previously credited Variables learning. Do not repeat the introductory tool-cycle exercise.

**10–20 minutes — language and asynchronous control.** Ask for a prediction before running this small example, then an explanation of how the resolved value reaches the callback. If promises are new, treat that as the next teaching target rather than a failed advanced test.

```js
async function readTask() {
  return { id: "demo", command: "echo" };
}
const pending = readTask();
console.log("created");
pending.then(task => console.log(task.id));
console.log("queued");
```

Ask the learner how they would handle a rejected task read and what a TypeScript type could or could not guarantee about JSON read from disk. The latter is a readiness probe, not a requirement to know TS before studying it.

**20–35 minutes — files and processes.** In an existing practice checkout, have the learner show or attempt a minimal CLI that reads a local fixture and launches a harmless child process. Choose one unfamiliar case based on their current level: malformed input, missing executable, nonzero exit, or output split across chunks. Ask what they expect before running it. Do not write the implementation for them.

**35–45 minutes — route and record.** Ask who should terminate the child when the caller cancels, and how they would establish that it stopped. Inspect `git status` and a small diff together; if Git inspection is unfamiliar, introduce M11 E1 before edits. Record actual time, help given, evidence and the next unmet checkpoint in the owning project.

## Route after the attempt

| Evidence | Next teaching focus |
|---|---|
| Functions, objects, modules or errors still uncertain | Continue from the actual Boot.dev checkpoint; defer child-process implementation until the needed concepts are explained. |
| Language ready; file/async behavior uncertain | Official Node selected reading, then a task-file CLI and one failure case. |
| CLI and basic child process explained | Stream framing, bounded output, timeout/cancellation and meaningful failure checks. |
| Runner criteria demonstrated | Record the assessment and inspect remaining explicit course-completion work before activating TS; do not repeat the runner. |

Ask one question at a time during teaching. A plan or passing generated script does not satisfy the [assessment rubric](../course/ASSESSMENT.md). If the remaining scope exceeds the proposed three-week execution window, prepare separate finishable projects before activating them.
