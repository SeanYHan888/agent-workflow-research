# VPS recommendation source excerpts

Preserved September 28, 2026 from the Codex chat **Plan Oracle Cloud Free VPS setup** (`01a0c09c-e6df-7391-9bad-1fd159c7d752`). These are September 24 historical messages, not current purchase advice. The later approximately $5/month request supersedes the earlier unbudgeted recommendation. Full chat remains in Codex history; the shared web link was inaccessible.

## Turn 01a0d42b-d51f-7143-ac75-a46f48a482ec

User:

if oracle is not available what other provider do you recommand

Assistant (historical):

For **Tailscale and Herdr with multiple coding agents**, I’d choose **OVHcloud VPS-3** if you’re willing to pay. It advertises 6 vCores, 12 GB RAM, and 100 GB storage starting at **$12.32/month**. The cheaper VPS-2 has 8 GB RAM starting at **$8.50/month** and is a reasonable place to start; OVH says you can upgrade it later. Those are advertised starting prices, so check the **US location, month-to-month price, and total due at checkout** before ordering. [OVHcloud VPS plans](https://us.ovhcloud.com/vps/), [OVHcloud billing terms](https://support.us.ovhcloud.com/hc/en-us/articles/360002306224-Overview-of-Billing-with-OVHcloud-US)

If **$0 is essential**, I’d keep the Oracle capacity monitor running. Google Cloud’s Always Free VM has only **1 GB RAM**, 30 GB of disk, and 1 GB of outbound transfer per month—too constrained for the agent setup you described. While waiting, you could run Herdr on your Mac and reach it through Tailscale, as long as the Mac stays awake. [Google Cloud Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features), [Herdr remote workflow](https://herdr.dev/docs/how-to-work/)

My recommendation: **OVH VPS-2 if you want to start cheaply; VPS-3 if you expect several agents running at once.** Keep Oracle as the free option to revisit when capacity opens.



## Turn 01a0d42f-6851-7c52-87a0-423bd074ce98

User:

my budge is around 5 dollars a month, what are some options

Assistant (historical):

At **around $5/month**, my pick for running **Tailscale and Herdr on the VPS** is **OVHcloud VPS-1**: 2 vCores, 4 GB RAM, and 40 GB storage, advertised from **$4.54/month**. That’s the most useful amount of RAM I found near your budget. The catch is that the advertised price links to a **12-month upfront** option—about **$54.48 before tax**. Check the final price and renewal terms before ordering; I haven’t verified a $5 month-to-month price. [OVHcloud plans](https://us.ovhcloud.com/vps/), [billing terms](https://support.us.ovhcloud.com/hc/en-us/articles/360002306224-Overview-of-Billing-with-OVHcloud-US)

If you need to **pay month by month**, the alternatives are much smaller:

| Option | Price | RAM | Fit for your setup |
|---|---:|---:|---|
| [BuyVM KVM Slice](https://www.buyvm.net/) | $3.50/month | 1 GB | Cheap, but check stock; limited room for agents |
| [Akamai Nanode](https://www.akamai.com/cloud/pricing) | $5/month | 1 GB | Predictable monthly option; best for light use |
| [DigitalOcean Basic](https://www.digitalocean.com/pricing/droplets) | $4/month | 512 MB | Too small for the Herdr setup I’d recommend |

**I’d choose OVH if paying for a year is comfortable.** If it isn’t, I’d keep the Oracle monitor running and use a $5 VPS only for light tasks; 1 GB won’t give you the multiple-agent machine you originally wanted.

