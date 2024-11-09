import machine
import sys
import select

# Configure UART1 (TX=GPIO 16, RX=GPIO 17) for communication with the router
uart = machine.UART(0, baudrate=115200, tx=machine.Pin(16), rx=machine.Pin(17))

# UART-to-USB bridge loop
while True:

    # Check if data is available from UART (router)
    if uart.any():
        data = uart.read()
        if data:
            sys.stdout.write(data.decode())

    # Check if data is available from USB (PC)
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        user_input = sys.stdin.read(1) 
        uart.write(user_input)
