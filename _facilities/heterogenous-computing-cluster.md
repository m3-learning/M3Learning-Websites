---
title: High-Performance Computing Cluster
category: Computing Facilities
layout: page
image: /assets/img/facilities/ComputingCluster.png
description: Kubernetes-based deep learning clusters with cutting-edge GPU nodes.
permalink: /facilities/heterogenous-computing-cluster/
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/facilities/ComputingCluster.png"  title="Heterogenous computing cluster for scientific machine learning" class="img-fluid rounded z-depth-1" width="50%"%}
    </div>
</div>

<div class="caption">
    Heterogenous computing cluster for scientific machine learning
</div>

## Heterogeneous Computing Cluster for Scientific Machine Learning

Agar manages a **Kubernetes-based machine learning cluster** at Lehigh University, designed to connect directly to scientific instruments via **200 Gbps networking**.

**Key components include:**

- **Head node:**

  - 120 TB of NVMe flash storage
  - > 40 GB/s read/write speeds

- **2× GPU nodes (4× A100 GPUs each):**

  - One node with 40 GB memory per GPU
  - One node with 80 GB memory per GPU
  - SMB interconnects for multi-GPU workloads

- **1× heterogeneous compute node:**

  - 2× U280 FPGAs
  - 1× A100 PCIe GPU (80 GB memory)

- **1.4 PB StorJ cluster:**
  - Set up as a DataFed repository
  - Fully backed up on a second 1.4 PB StorJ cluster in Lehigh’s datacenter

This cluster provides **high-speed AI processing** and **seamless integration with scientific instruments**, supporting advanced research workflows.
