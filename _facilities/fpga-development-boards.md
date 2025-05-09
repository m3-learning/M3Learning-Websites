---
title: FPGA Development Boards
category: Computing Facilities
layout: page
image: /assets/img/facilities/DragonClusterDevSchematic.png
description: FPGA development platforms for high-speed signal processing and ML.
permalink: /facilities/fpga-development-boards/
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <div class="text-center">
            {% include figure.liquid loading="eager" path="assets/img/facilities/RFSoC4x2.png" title="RFSoC 4x2 Board" class="img-fluid rounded z-depth-1" width="50%" %}
        </div>
    </div>
</div>


<div class="caption">
    RFSoC 4x2 Board
</div>


## RFSoC 4x2 Board

The RFSoC 4x2 is a flexible, high-speed system that combines:

- Fast ADCs and DACs  
- A multi-core ARM processor  
- A large FPGA

It’s built on AMD’s **ZYNQ Ultrascale+ RFSoC ZU48DR** chip and is designed for real-time signal processing.

**Key features include:**

- 4 ADC channels (5 GSPS, 6 GHz bandwidth)  
- 2 DAC channels (14-bit, up to 9.85 GSPS)  
- 8 GB DDR4 memory  
- 100 Gbps Ethernet (QSFP28)  
- Precise clocking for synchronized measurements

The board is *ready to use out of the box* and supports Python programming through the **PYNQ framework** and Jupyter notebooks. It also comes with tutorials and tools for quick setup and testing.

This platform is ideal for RF applications, data acquisition, and advanced digital signal processing.


## Eclypse Z7 Boards

We have 2× Eclypse Z7 boards designed for fast prototyping of embedded measurement and signal processing systems.

Each board features a **Xilinx Zynq-7020 SoC**, which combines:

- A 667 MHz dual-core Cortex-A9 processor  
- Programmable logic (Artix-7 FPGA equivalent)

This setup provides a powerful and flexible platform for developing high-speed instrumentation, control, and measurement systems, especially in edge computing, medical, and communications applications.

**Key features:**

- Zmod expansion (using the SYZYGY standard) for customizable high-speed I/O  
- Faster and more compact than the traditional Pmod standard  
- Cost-effective alternative to FMC modules

The Eclypse Z7 makes it easy for scientists and engineers to build and test application-specific systems quickly and efficiently.


## ZUBoard 1CG

The ZUBoard 1CG is an accessible development platform built on the **Xilinx Zynq UltraScale+™ architecture**.

It features:

- Dual-core Arm Cortex-A53 and Cortex-R5F processors  
- 81K programmable logic cells  
- 1 GB of LPDDR4 memory

The board supports **booting from QSPI Flash or microSD** and offers multiple connectivity options, including:

- Ethernet  
- USB 2.0 (via Microchip PHYs)  
- On-board JTAG/UART through microUSB

Power is provided via USB-C, and user interaction is supported with switches, buttons, LEDs, and environmental sensors (STMicroelectronics).

**Expansion options include:**

- Samtec connectors  
- A Click Board™ site for additional modules

With full support for Vivado and PetaLinux, the ZUBoard 1CG is ideal for developing bare-metal applications, Linux systems, or AI accelerators using Vitis.

