---
layout: page
title: Facilities
permalink: /facilities/
---

This page provides an overview of the key facilities available within the M3 Learning research group at Drexel University.

## Development Workstations  
Agar's lab has a range of GPU resources for machine learning training, including:  
- **8× NVIDIA A6000**  
- **5× NVIDIA 3090**  
- **4× NVIDIA Titan RTX**  
These workstations support local testing before cluster-based model training. One system also features a **U200 FPGA** for real-time ML.

## FPGA Development Boards  

<div><img src="{{ site.baseurl }}/assets/img/facilities/DragonClusterDevSchematic.png" alt="Dragon Cluster Development Schematic" width="50%"><p>Schematic drawing of the Dragon Cluster under Development</p></div>


### RFSoC 4x2  
A high-performance board with **integrated ADCs, DACs, and a multi-core ARM processor**. It offers:  
- 5 GSPS ADCs, 9.85 GSPS DACs  
- **100 Gbps Ethernet, 8GB DDR4**  
- **PYNQ framework support** for Python/Jupyter-based development  

### Eclypse Z7  
Two **Eclypse Z7 boards** facilitate **high-speed signal processing**, featuring:  
- **Xilinx Zynq-7020 SoC** (Dual-Core Cortex-A9 + Artix-7 FPGA)  
- **SYZYGY standard** for rapid high-speed I/O integration  

### ZuBoard 1CG  
A **versatile development board** with:  
- **Zynq UltraScale+ architecture** (Dual-Core Cortex-A53 & Cortex-R5F)  
- **1GB LPDDR4, USB-C power, and expandable connectivity**  
- **Support for Vivado, PetaLinux, and Vitis AI accelerators**  

## Experimental Compute Facilities 
The lab hosts several **high-speed servers** for **data transfer and computation**, featuring:  
- **100 Gbps local networking**  
- **Edge node with 2× U280 FPGAs & 1× H100 GPU**  
- **4× 15TB NVMe RAID0 (20 GB/s read/write speed)**  
- **147 TB ZFS node (RAID6 for durability)**  
- **Automated snapshots to a secondary ZFS node at the university datacenter**  

## High-Performance Computing Clusters


<div><img src="{{ site.baseurl }}/assets/img/facilities/DragonDeepLearnCluster.png" alt="Dragon Cluster Development Schematic" width="50%"><p>Rack elevation for Dragon Deep Learning Cluster</p></div>


### Dragon Deep Learning Cluster
- Developed through an NSF MRI award.
- Designed for high-availability machine learning (ML) services.
- Kubernetes-based cluster for ML and web service deployment.
- Key specifications:
  - PB flash parallel file system with 80 GB/s read-write speeds.
  - 2x 8x H200 SMX GPU nodes (144 GB per GPU, 6 TB RAM, 256 CPU cores).
  - 1x 10X A100 80 GB node (1.5 TB RAM, supports multi-instance GPUs).
  - 2x GH200 SuperChips.
  - 15x single CPU 24-core/48-thread nodes.
  - Basepod reference architecture with 400 Gbps networking.

### Heterogeneous Computing Cluster for Scientific Machine Learning

<div><img src="{{ site.baseurl }}/assets/img/facilities/ComputingCluster.png" alt="Heterogenous computing cluster for scientific machine learning" width="60%"><p>Heterogenous computing cluster for scientific machine learning</p></div>
  

- Managed at Lehigh University.
- 200 Gbps network connectivity to scientific instruments.
- Key specifications:
  - Head node with 120 TB NVMe flash (40 GB/s read-write speed).
  - 2x 4x A100 nodes (one with 40 GB memory, another with 80 GB).
  - 1x heterogeneous compute node (2x U280 FPGAs, 80 GB A100 PCIe GPU).
  - Cluster set up as a DataFed Repository with backup at Lehigh data center.

### M3Kube Cluster

<div><img src="{{ site.baseurl }}/assets/img/facilities/M3KubeCluster.png" alt="Picture of m3Kube" width="50%"><p>Picture of M3Kube Cluster</p></div>


- Constructed from surplus nodes of the Proteus cluster at Drexel.
- 60-node Kubernetes cluster.
- Key specifications:
  - 24-core CPUs per node, RAM ranging from 64 to 256 GB.
  - 150 TB ZFS storage node for persistent data storage.
  - 40 Gbps InfiniBand networking.
  - Public internet connectivity bypassing university firewall, managed via pfSense.
  - Suited for FPGA model compilation and web service hosting.

### Big Mac Cluster

<div><img src="{{ site.baseurl }}/assets/img/facilities/BigMacKubernetesCluster.png" alt="Picture of BigMac Kubernetes cluster" width="50%"><p>Picture of BigMac Kubernetes cluster</p></div>


- 15-node Kubernetes cluster built from surplus iMac workstations.
- 40 TB NAS for persistent data storage.
- Public internet connectivity, secured by a firewall.
- Primarily used for:
  - Development, education, and testing.
  - Hands-on training with bare-metal Kubernetes.
  - Deployment, troubleshooting, and rebuilding exercises.
  - Rapid configuration via Ansible playbooks.

## Pulsed Laser Deposition (PLD) Facilities – Agar Lab
<div class="facility-carousel">
  <div class="carousel">
    <div><img src="{{ site.baseurl }}/assets/img/facilities/PLDfacility.png" alt="Computer automated pulsed-laser deposition facility" width="50%"><p>Computer automated pulsed-laser deposition facility</p></div>
    <div><img src="{{ site.baseurl }}/assets/img/facilities/PLDMotionStage.png" alt="Motion Stage for computer-controlled optics" width="50%"><p>Motion Stage for computer-controlled optics</p></div>
    <div><img src="{{ site.baseurl }}/assets/img/facilities/PLDAttenuator.jpg" alt="Motion Stage for computer-controlled optics" width="50%"><p>Motion Stage for computer-controlled optics</p></div>
    </div>
  <div class="dots"></div>
</div>

- Custom-designed PLD facility with precise temperature and humidity control.
- Fully computer-controlled PLD system featuring:
  - Excimer LPX 305 laser (248 nm).
  - Motion stage for optics.
  - Ultrafast Shimadzu Hypervision X2 camera (10 million fps, 256-frame bursts).
  - Computer-controlled attenuator.
  - Two PLD chambers (one RHEED-ready, recently ordered second chamber).
  - Computer-controlled mass flow controllers, 6-carousel target rotators, heater stage, and throttle valve.
  - Centralized LabVIEW control system.
  - 10 Gbps Ethernet data transfer to 80 TB network-attached flash storage.

## Surface Analysis Capabilities
### Atomic Force Microscopy (AFM) – Oxford Instruments Cypher S

<div><img src="{{ site.baseurl }}/assets/img/facilities/AFMSchematic.png" alt="Technical schematic showing custom control systems and computational pipeline" width="50%"><p>Technical schematic showing custom control systems and computational pipeline</p></div>

- High-resolution interferometric AFM.
- Equipped with:
  - Piezoresponse force microscopy.
  - Conductive AFM with a high-voltage source.
  - Fast force mapping and blueDrive photothermal excitation.
  - Interferometric detection for precise cantilever displacement measurement.
- Custom control system for multimodal spectroscopic measurements:
  - PXI system with arbitrary waveform generator and oscilloscope.
  - Software for band-excitation piezoresponse force microscopy.
  - KU60 Xilinx FPGA for real-time data processing and machine learning deployment.

## Electrical Testing Facility

<div><img src="{{ site.baseurl }}/assets/img/facilities/ElectricalProbe.jpg" alt="Electrical Probe with a temperature Check" width="50%"><p>Electrical Probe with a temperature Check</p></div>

- Electrical probe station with:
  - Resistive heater up to 500°C.
  - Radiant multiferroic II ferroelectric tester with high-voltage capabilities.
  - Deep-level transient spectroscopy imaging add-ons.
- National Instruments system for various electrical measurements.
- Collaboration with Spanier Lab:
  - Access to additional electrical testing equipment.
  - Shared PLD chambers with 248 nm KrF and 1064 nm Nd:YAG pulsed lasers.
  - RHEED-equipped PLD chamber for plume dynamics imaging.
  - Empyrian X-ray diffractometer with a 2D detector for high-resolution XRD and reciprocal space mapping.



