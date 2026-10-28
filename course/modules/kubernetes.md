# M8 — Kubernetes: operate the understood service declaratively

Required milestone: **Operate services with Kubernetes** — workload lifecycle, scheduling/resources, service discovery, networking, configuration/secrets, persistent state, rollout and recovery, compared with the understood single-host deployment ([roadmap](../../ROADMAP.md#stages-and-milestones)). Checkpoints M8.1–M8.6 elaborate that row; they add no required outcome, depth or scope.

## Useful result

The Kubernetes half of the [project route](../../ROADMAP.md#project-route) row **"Deployment and interface comparisons"**: deploy the service the learner already operates under M5, then test its recovery. The [project catalog](../PROJECTS.md) names the smallest deliverable: one understood service deployment and a recovery demonstration. The same runner/worker service is moved from its single-host supervisor into declarative workloads. It is not replaced with a sample application.

**Observable acceptance:** from the learner's own manifests, the service is reachable by name from another Pod. Deleting its Pod or failing its readiness check produces the recovery or traffic change the learner predicted. A broken rollout is stopped and rolled back. For each event, the learner names which controller acted and compares the behavior with the M5 single-host deployment.

## Placement and prerequisites

- Entry gates: M5 containers, networks and services, including the [O1–O3/N1–N3/S1](systems-foundations.md) OS, socket/framing, packet/failure and access-boundary evidence required before orchestration, and M7 coordination and failure reasoning.
- Follow the resource-catalog rule: study Kubernetes only after the single-machine runtime works and measurements show why more infrastructure is needed ([catalog](../../materials/resource-catalog.md)).
- Reuse M5 Docker images, resource limits and logs, and M7 idempotency and duplicate-delivery evidence. Do not re-teach them.
- M10 needs M8 deployment evidence. The distribution node need not run Kubernetes: the subject is assessed even if it does not ship.
- Optional depth: custom operators and cluster internals, only for a relevant project question ([subject boundaries](../../ROADMAP.md#subject-boundaries)).

## Checkpoints

| ID | Mechanism | Observable evidence | Hours |
|---|---|---|---:|
| M8.1 | Workload lifecycle: Pods, Deployments/ReplicaSets, Jobs, desired state and controller reconciliation | Learner-written manifests; a deleted Pod replaced as predicted; ownership chain from Deployment to Pod explained | 4–6 |
| M8.2 | Scheduling and resources: requests/limits, node fit, QoS, eviction; relation to M5 cgroups | One unschedulable Pod diagnosed from events; one memory-limit kill explained with reference to the M5 limit lab | 3–5 |
| M8.3 | Service discovery and networking: Services, endpoints, cluster DNS, readiness, network policy | Name-based reachability from a client Pod; a failing readiness probe removes the endpoint; DNS, endpoint and application failures diagnosed separately | 4–7 |
| M8.4 | Configuration and secrets: ConfigMaps, Secrets, environment versus mounted files, change propagation | A missing or wrong config diagnosed from Pod status; fixture-only secret; the learner states what Secret storage does and does not protect in the chosen cluster | 2–4 |
| M8.5 | Persistent state: volumes, PersistentVolumeClaims, StatefulSet identity; relation to M7 D1–D3 | Job state survives Pod replacement on a claim but not on an ephemeral volume; storage assumptions of the local provisioner stated | 3–5 |
| M8.6 | Rollout and recovery: rolling update, probes, rollback, restart policy; comparison with single-host operation | A bad image or config rollout stopped and rolled back; a restarted job's duplicate effect handled by M7 idempotency; comparison table versus the M5 deployment | 4–8 |

Planning split of the 20–35h [workload](../WORKLOAD.md) row, including reading, attempts and assessment.

## Lab sequence

Each increment follows the [session workflow](../../teaching/README.md#prepare-and-teach). The learner writes the manifests and predicts outcomes; the teacher hints and points to the doc section. Each increment is at most one 6–9-hour project slice.

| Increment | Deliverable | Acceptance check | Learner's first action | Timebox |
|---|---|---|---|---|
| 1. Desired state | Deployment for the existing worker image | Deleting the Pod yields a new one; the learner names the replacing controller | Write down what should happen when the Pod is deleted, then apply | 1–2 sessions |
| 2. Fit and limits | Requests/limits matching measured M5 usage | An over-request stays Pending with an explained event; an over-limit process is killed as predicted | Pick requests and limits from M5 measurements and justify them | 1–2 sessions |
| 3. Reachable by name | Service plus a client Pod, with a readiness probe | Client reaches the service by DNS name; a failed probe removes it from endpoints | Predict the DNS name and which endpoints will exist | 2 sessions |
| 4. Config and state | ConfigMap/Secret wiring and a claim for job state | State survives Pod replacement; a deliberately missing key is diagnosed from status | Sketch which data must outlive a Pod and why | 2 sessions |
| 5. Rollout and compare | Rolling update, failed rollout and rollback, plus a comparison note | Rollback restores service; the comparison covers restart, logs, limits, reachability and state against M5 | Predict how a bad image tag will surface during rollout | 2–3 sessions |

## Failure experiments

- Crash-looping container from a bad command or config; read status, events and previous logs.
- Readiness versus liveness confusion: a slow start killed by liveness; explain the probe chosen.
- Wrong namespace or Service selector: DNS resolves but no endpoints exist. Separate this from an application error.
- Pod killed mid-job under a restart policy: show the re-executed effect, then the M7 idempotency check that prevents a duplicate external effect. Kubernetes restart is not exactly-once.
- Delete a Pod using an ephemeral volume, then one using a claim. Compare what survives.

## Hardware and environment notes

A laptop with the M5 container runtime can run a local single-node cluster; select the tool from the official [install tools](https://kubernetes.io/docs/tasks/tools/) page at lesson preparation and record its version. A multi-node local cluster on one machine simulates nodes that share one kernel and disk; label its node-failure results as simulated. Real node loss and cross-host networking need authorized remote nodes after M5 VPS readiness. No cluster, host, provider or budget is chosen here. Use only fixture secrets.

## Materials

| Source | Role | Checkpoint |
|---|---|---|
| [Kubernetes Concepts](https://kubernetes.io/docs/concepts/) (selected in the [systems reading map](../../materials/systems-reading-map.md)) | Primary reference, matched to the selected cluster version | All |
| [Workloads](https://kubernetes.io/docs/concepts/workloads/), [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/), [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) | Desired state, ownership and restart behavior | M8.1, M8.6 |
| [Resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/), [scheduling and eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/) | Requests/limits, placement and eviction | M8.2 |
| [Service](https://kubernetes.io/docs/concepts/services-networking/service/), [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/), [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) | Discovery, reachability and traffic restriction | M8.3 |
| [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/), [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) | Configuration injection and the Secret security model | M8.4 |
| [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) | Claims, provisioners and stable identity | M8.5 |
| [Kubernetes Tasks](https://kubernetes.io/docs/tasks/): [probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/), [debugging applications](https://kubernetes.io/docs/tasks/debug/debug-application/) | Step-by-step procedures for the active increment | M8.3, M8.6 |
| [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html), [cgroups(7)](https://man7.org/linux/man-pages/man7/cgroups.7.html), [Docker Get Started](https://docs.docker.com/get-started/) | M5 single-host baseline that the comparison refers to | M8.2, M8.6 |
| [MIT 6.5840](https://pdos.csail.mit.edu/6.824/) selected route ([integration map](../../materials/university-course-integration.md)) | Failure timelines reused to reason about reconciliation and restarts | M8.6 |

## Assessment

Use the [shared rubric](../ASSESSMENT.md). Require learner-written manifests, observed recovery and failure events, controller ownership explained for each event, and the single-host comparison. In an unseen variation, such as a changed selector, a tighter limit or a misconfigured probe, the learner predicts and then diagnoses the result. A tutorial deployment or a running cluster alone does not demonstrate M8. Reuse M5 and M7 evidence for the criteria it already supports.

**Estimated hours:** 20–35 directed hours ([workload forecast](../WORKLOAD.md)).
