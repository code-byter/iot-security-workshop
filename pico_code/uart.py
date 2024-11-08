import machine
import sys
import select

# Configure UART1 (TX=GPIO 16, RX=GPIO 17) for communication with the router
uart = machine.UART()

# UART-to-USB bridge loop
while True:

    # Check if data is available from UART (router)


    # Check if data is available from USB (PC)

