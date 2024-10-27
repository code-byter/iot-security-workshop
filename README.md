# IoT Device Security Workshop

**Disclaimer:** This repository will be fully updated and finalized one week before the workshop. Please check back at that time for the complete materials and resources.

## Workshop Focus

This workshop is centered around the security of IoT devices, with a specific focus on:
- **Hardware security** of a WiFi router
- **Firmware analysis** and reverse engineering

## Materials

- A pre-configured Virtual Machine (VM) with all necessary tools will be available here one week before the workshop.
- Alternatively, a list of required tools and installation instructions will be provided.

## Agenda

1. **0x01: IoT Device Attack Vectors**
   - Overview of common attack vectors for IoT devices
2. **0x02: Device Recon**
   - Techniques for reconnaissance on IoT devices
3. **0x03: Analyzing UART**
   - Understanding UART interfaces and how to analyze them
4. **0x04: Firmware Extraction from Flash Memory**
   - Methods for extracting firmware from flash memory chips
5. **0x05: Firmware Reverse Engineering**
   - Using Ghidra for reversing firmware and exploiting vulnerabilities
6. **0x06: Introduction to BLE Security**
   - Basic principles and vulnerabilities in Bluetooth Low Energy (BLE) security

## Prerequisites

- Basic knowledge of programming, networking, and memory management
- Familiarity with Linux command line
- A computer with virtualization support

## Tools and Software

- The VM will include all required tools, such as:
  - **Ghidra** for reverse engineering
  - **Binwalk** for firmware analysis
  - **BurpSuite** for Web Request Analysis
  - **GDB** for  debugging
- If you prefer to set up your environment manually, a detailed list will be provided.


## Getting Started

To get started, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/iot-security-workshop.git
   ```

2. Download and set up the VM or follow the instructions in the tools.md file (to be uploaded a week before the workshop).