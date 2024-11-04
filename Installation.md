# Hardware Hacking Workshop Tool Installation Guide

This guide provides instructions for setting up a Linux environment with all the necessary tools for the Hardware Hacking Workshop. Follow the steps below to install each tool and set up configurations as needed.

## 1. Install Visual Studio Code (VSCode)

1. Download the Debian package for VSCode from the [official website](https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64).

    ```bash
    sudo dpkg -i code_1.95.1-1730355339_amd64.deb
    ```

2. After installation, open VSCode and install the MicroPico extension:

    - **Extension Name**: MicroPico
    - **ID**: paulober.pico-w-go
    - **Description**: Provides auto-completion, remote workspace, and REPL console integration for Raspberry Pi Pico boards running MicroPython firmware.
    - **Version**: 4.0.6
    - **Publisher**: paulober
    - [VS Marketplace Link](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go)

## 2. Udev Rules for Raspberry Pi Pico

To ensure the Pico board can be accessed without `sudo` and to create a persistent symlink, configure udev rules:

1. Create a new file in `/etc/udev/rules.d/99-pico.rules`:

    ```bash
    sudo nano /etc/udev/rules.d/99-pico.rules
    ```

2. Add the following rules:

    ```udev
    # Make an RP2040 in BOOTSEL mode writable by all users, so you can `picotool` without `sudo`.
    SUBSYSTEM=="usb", ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="0003", MODE="0666"

    # Symlink an RP2040 running MicroPython from /dev/pico.
    SUBSYSTEM=="tty", ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="0005", SYMLINK+="pico"
    ```

3. Reload the udev rules:

    ```bash
    sudo udevadm control --reload-rules
    ```

## 3. Install PulseView

PulseView is an open-source tool for analyzing signals from digital and analog devices.

```bash
sudo apt install pulseview
```

## 4. Install Binwalk

Binwalk is a tool for analyzing binary files. To install it, first install Rust and Cargo, then compile Binwalk:

1. Install additional dependencies:

    ```bash
    sudo apt install build-essential pkg-config libfontconfig1-dev
    ```

2. Install Rust and Cargo:

    ```bash
    curl https://sh.rustup.rs -sSf | sh
    ```

3. Install Binwalk:

    ```bash
    cargo install binwalk
    ```


## 5. Install GDB and GEF

GDB and the GEF plugin enhance debugging capabilities.

1. Install GDB:

    ```bash
    sudo apt install gdb gdb-multiarch
    ```

2. Install GEF:

    ```bash
    bash -c "$(curl -fsSL https://gef.blah.cat/sh)"
    ```

## 6. Install Burp Suite Community Edition

Burp Suite is an essential tool for web application security testing.

1. Download the Community Edition installer from the [official website](https://portswigger.net/burp/documentation/desktop/getting-started/download-and-install).
2. Run the installer:

    ```bash
    bash ./burpsuite_community_linux_v2024_9_4.sh
    ```

## 7. Install Ghidra

Ghidra is a software reverse engineering tool developed by the NSA.

1. Install Java (required for Ghidra):

    ```bash
    sudo apt install openjdk-21-jdk unzip wget
    ```

2. Download Ghidra from the [official GitHub release page](https://github.com/NationalSecurityAgency/ghidra/releases).

    ```bash
    wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.2_build/ghidra_11.2_PUBLIC_20240926.zip
    ```

3. Unzip the downloaded file:

    ```bash
    unzip ghidra_11.2_PUBLIC_20240926.zip
    ```

## 8. Install Python3 Packages

A few Python packages are essential for the workshop exercises.

```bash
pip3 install requests scapy
```


---
Make sure to verify each installation step and test the setup. If you encounter issues, refer to the official documentation for each tool.