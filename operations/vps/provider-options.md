# VPS options — imported recommendation and refresh

Migrated September 28, 2026 from **Plan Oracle Cloud Free VPS setup**. The [September 24 source excerpts](../../archive/2026-09-28-oracle-project-source/vps-recommendation-excerpts.md) are preserved locally. The later approximately **$5/month** preference takes precedence over the earlier unbudgeted suggestion of larger OVH plans. No provider was selected or purchased.

## Shortlist and evidence

| Option | Earlier recommendation | September 28 evidence / remaining check |
|---|---|---|
| Oracle A1 | Free option for remote agent work if capacity becomes available | Last authenticated result was unavailable; later checks blocked. No fresh capacity or allowance claim. [Operational status](STATUS.md). |
| OVHcloud VPS-1 | Best RAM near the stated budget among the inspected candidates: advertised $4.54/month, 2 vCores, 4 GB RAM, 40 GB NVMe; earlier link used 12-month upfront billing | The public page still lists those starting-price/spec figures. True month-to-month cost, region stock, term, renewal, tax and checkout total were not verified. [Official plans](https://us.ovhcloud.com/vps/). |
| Akamai Nanode | $5/month, 1 GB RAM for a light service | Public pricing still lists $5/month, 1 vCPU, 1 GB, 25 GB disk and 1 TB transfer. Region and extras still need checking. [Official pricing](https://www.akamai.com/cloud/pricing). |
| BuyVM | Historical $3.50/month / 1 GB candidate with stock caveat | Imported as history only; current offer/stock not rechecked. [Provider](https://www.buyvm.net/). |
| DigitalOcean Basic | Historical $4/month / 512 MB option, too constrained for the intended multi-agent use | Imported as history only; current offer not rechecked. [Official pricing](https://www.digitalocean.com/pricing/droplets). |

The earlier broader comparison also suggested OVH VPS-2/3 for more agents. The public page currently advertises starting prices of $8.50 for 8 GB and $12.32 for 12 GB; these exceed the recorded budget and are not the default recommendation. [OVH plans](https://us.ovhcloud.com/vps/).

## Recommendation retained for the course

Investigate OVH VPS-1 first if annual prepayment is acceptable, but do not equate the advertised monthly equivalent with monthly billing. If monthly payment and $5 are firm constraints, Nanode is a candidate for one light remote service. Measure the actual workload before adding agents. Four GB is a planning starting point for more headroom, not a benchmark-backed guarantee; 1 GB is not an assumed fit for brokers, several agents and inference together.

Keep Oracle as the free candidate while its monitor stays paused. An awake local Mac with an appropriately configured remote-access path was the earlier interim alternative; no new access configuration is performed here. Model-serving, Kafka/RabbitMQ and Cua environments need separate resource/architecture checks rather than being silently added to the cheapest host.

Before a purchase decision, verify total recurring cost, prepayment/commitment, renewal, tax, IPv4, backups, transfer charges, region/stock and cancellation terms. The two public-page refreshes above are not a checkout verification. [OVH billing reference](https://support.us.ovhcloud.com/hc/en-us/articles/360002306224-Overview-of-Billing-with-OVHcloud-US).
