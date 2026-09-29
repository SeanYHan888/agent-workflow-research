# Oracle VPS status

## Latest verified capacity check

- Time: 2026-09-24 15:19:30 UTC (11:19 Boston time).
- Source: authenticated Oracle Cloud Shell, OCI Compute Capacity Report.
- Tenancy: cannotfand; home region: us-sanjose-1.
- Availability domain: EvdF:US-SANJOSE-1-AD-1.
- Shape checked: VM.Standard.A1.Flex at 2 OCPUs / 12 GB.
- Result: OUT_OF_HOST_CAPACITY; available-count was null (not a numeric zero). The earlier 2026-09-20 report also found smaller A1 configurations and AMD Micro out of capacity, but those were not rechecked today.
- No fault domain was specified, so the report covers all fault domains.
- No instance was launched by this check. The root-compartment instance list was empty.

## Repeat without launching a VM

Open Oracle Console > Developer tools > Cloud Shell in San Jose. The authenticated Cloud Shell has the OCI CLI and OCI_TENANCY environment variable. Run this as one line:

```bash
oci compute compute-capacity-report create --compartment-id "$OCI_TENANCY" --availability-domain "EvdF:US-SANJOSE-1-AD-1" --shape-availabilities '[{"instanceShape":"VM.Standard.A1.Flex","instanceShapeConfig":{"ocpus":2,"memoryInGBs":12}}]' --region us-sanjose-1 --max-retries 0
```

This creates a capacity report, not an instance or capacity reservation. Read the returned status and time; a shape listing or free-eligible label is not proof of available host capacity. Use the in-app browser for UI access. Paste a single command then press Return; multiline typeText was observed to concatenate lines. Wait for the terminal prompt to return before reading the result.

The daily automation `oracle-free-vps-capacity` checks at 09:00 America/New_York. It should use this verified method and notify only for availability or a new actionable blocker. Provisioning remains paused.

## Storage and transfer

Oracle's published free allowance is 200 GB combined boot/block storage in the home region and 10 TB outbound transfer per month. The capacity report above checks CPU and memory only; it does not reserve or guarantee storage. Root-compartment boot/block volume list queries returned no rows, but no complete cross-compartment storage or transfer-usage audit was performed.

## Resizing

Oracle's current documented A1 allowance is 2 OCPUs / 12 GB total (1,500 OCPU hours and 9,000 GB hours monthly). A smaller A1 Flex VM can be resized within that allowance if capacity is available; resizing a running VM causes a reboot and retains its volume attachments and IP addresses. E2.1.Micro cannot be resized, so moving from that AMD shape to A1 requires creating an ARM VM and migrating software/data, keeping aggregate storage within the free allowance.

## Local preparation

- Dedicated SSH key already created: /Users/seanmacbook/.ssh/oracle_vps_ed25519 (private; never upload or print).
- Public key: /Users/seanmacbook/.ssh/oracle_vps_ed25519.pub.
- Mac Herdr version previously verified: 0.9.0.
- No VPS-side Tailscale or Herdr installation is complete.
- Earlier launch request for 2 OCPUs / 12 GB failed due to capacity. A 1 OCPU / 6 GB retry was discussed but not submitted before the user paused.
- The optional Cloud Guard Workload Protection plugin was removed from that launch form after approval review flagged its unverified billing impact.

## Sources

- https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-capacity-report/create.html
- https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm
- https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm
