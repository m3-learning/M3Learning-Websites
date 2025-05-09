---
title: High-Performance Computing Cluster
category: Computing Facilities
layout: page
image: /assets/img/facilities/DragonDeepLearnCluster.png
description: Kubernetes-based deep learning clusters with cutting-edge GPU nodes.
permalink: /facilities/high-performance-computing-cluster/
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <div class="text-center">
        {% include figure.liquid loading="eager" path="assets/img/facilities/DragonDeepLearnCluster.png"  title="PODWYRM Deep Learning Development Schematic" class="img-fluid rounded z-depth-1" width="50%"%}
        </div>
    </div>
</div>


<div class="caption">
    Rack Elevation for PODWYRM Deep Learning Cluster
</div>

## PODWYRM Deep Learning Cluster

Agar has been awarded funding through the **NSF MRI program** to develop the PODWYRM deep learning cluster, designed to provide **high-availability machine learning services** for scientific research.

The cluster is deployed as a **Kubernetes-based system**, enabling flexible and scalable AI workflows. Agar serves as the **primary system administrator**, managing policies and software.

**Key components include:**

- **1 PB flash parallel file system**  
   - 80 GB/s read-write speeds  
   - Optimized for high-speed AI training workflows

- **2× GPU nodes (8× H200 SMX GPUs each)**  
   - 144 GB memory per GPU  
   - 6 TB RAM per node  
   - 256 CPU cores  
   - Supports SMX interconnects for multi-GPU training  
   - GPUs can be combined or sliced into 56 microGPUs for flexible workloads

- **1× GPU node (10× A100 80 GB GPUs)**  
   - 1.5 TB RAM  
   - Designed for AI model testing, education, and outreach  
   - Supports Multi-Instance GPU (MIG) mode, providing up to 70 GPU instances

-  **2× GH200 SuperChips**

- **15× CPU nodes**  
   - Each with a single CPU (24 cores / 48 threads)

The cluster is built on a **Basepod reference architecture** and features **400 Gbps networking** for high-speed data transfers and distributed training.

This cutting-edge infrastructure enables advanced AI research and supports educational initiatives.

