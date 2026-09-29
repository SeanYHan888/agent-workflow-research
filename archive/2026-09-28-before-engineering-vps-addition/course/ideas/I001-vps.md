# I001 — rent a VPS as a course lab

Captured September 28, 2026: “I recently want to rent a VPS.” Accepted as an exploration candidate under the existing curriculum. No host has been selected or rented, and no price, purchase or deployment is assumed.

Existing execution owner: [Linux coordination](</Users/seanmacbook/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-vault/Projects/Active/terminal-agent-06-linux-coordination.md>) already contains three unfinished VPS tasks from September 24: evaluation (including OVHcloud as a candidate), obtain/configure/verify SSH, and deploy the runtime with recovery evidence. This brief gives that interest an early exploration slot; it does not create another task list or select that vendor.

## Why this belongs

Use the VPS idea to make M5's Linux, remote access, networking and service operations concrete. Early preparation can reinforce M2's processes, files and shell skills while JS/Node remains the primary module. Later, the same environment may host an understood worker/controller. Its suitability for model inference is a separate workload/hardware question; do not bundle a GPU-serving requirement into the first remote Linux exercise.

## First exploration — up to two hours

This uses one week's existing exploration allowance, not a new required milestone or a second active project. The output is a one-page requirements and decision brief.

| Block | Work | Evidence/output |
|---|---|---|
| 20 minutes | State the first workload: Linux practice, one long-running worker, a small API, or model serving. Separate immediate need from later ambitions. | One first use and a definition of success |
| 30 minutes | Draw laptop → SSH → Linux host → process/service; identify DNS, ports, credentials, logs and state ownership. Compare with a local lab and any existing authorized remote access. | Simple topology and which remote behavior the lab needs |
| 40 minutes | Translate the workload into constraints: CPU architecture, memory/storage needs, region/latency, traffic, persistence, recovery access and budget. Once the spending ceiling is known, inspect current official offers and terms. | Requirements plus at most two suitable candidates, or an explicit reason to defer comparison |
| 30 minutes | Explain tradeoffs and choose a next step: local practice, a proposed rental, or defer. | Recommendation with total recurring cost, billing/deletion conditions and remaining unknowns when a paid option is proposed |

Unresolved student inputs are the monthly all-in ceiling and intended first workload. Until they are supplied, prepare the topology and workload criteria without inventing a spending limit or choosing a paid plan. Verify current provider specifications/prices when comparing; no recommendation has been researched yet.

## Candidate follow-on project

After choosing a workload, meeting entry prerequisites and authorizing any rental, a possible bounded project is **operate one remote Linux service and recover it after interruption**. An initial planning allowance is six project hours across two weeks, subject to a prerequisite check. It would occupy the existing three-hour project slot and displace whichever optional project would otherwise use it.

Prerequisites: explain shell paths, basic permissions, a process and its logs; understand the SSH authentication path and the proposed service's access boundary. A gap becomes a small lesson before exposure or setup.

Demonstration: connect deliberately, identify the running service and its state/logs, show a controlled restart and recovery, explain the permitted network path, and document how to stop the service and terminate the rental without losing required evidence. Use a harmless fixture workload. Kubernetes and distributed inference retain their later prerequisites.

When activated, reuse the Linux project's ownership or split out an independently finishable project with dates within 21 days during the reviewed reforecast. Transfer/link the existing VPS tasks and retain their history; each action keeps one owner. Rental authorization and actual completion are separate from admitting this idea to the course.
