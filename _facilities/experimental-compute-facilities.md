---
title: Experimental Compute Facilities
category: Computing Facilities
layout: page
image: /assets/img/facilities/ComputingCluster.png
description: High-speed servers and storage systems for edge computing and data analysis.
permalink: /facilities/experimental-compute-facilities/
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <div class="text-center">
            {% include figure.liquid loading="eager" path="assets/img/facilities/ComputingCluster.png" title="Dragon Cluster" class="img-fluid rounded z-depth-1" width="50%" %}
        </div>
    </div>
</div>

<div class="caption">
    Schematic drawing of the Dragon Cluster under Development by Agar
</div>

## High-Speed Data Transfer and Storage Infrastructure

The lab hosts several high-performance servers designed for **high-velocity file transfers** over a local 100 Gbps network.

Key components include:

- An edge node with:

  - 2× U280 FPGAs
  - 1× NVIDIA H100 GPU
  - 4× 15 TB NVMe drives (RAID0, up to 20 GB/s read/write speed)

- A **ZFS storage node** with 147 TB capacity (RAID6), balancing performance and durability

The system is managed with **DataFed**, enabling rapid data offloading from local flash storage to disk. Snapshots are automatically replicated to a second ZFS node located in the University Research Computing Facility datacenter, ensuring data security and redundancy.

This infrastructure supports fast, reliable storage and processing for data-intensive experiments.
