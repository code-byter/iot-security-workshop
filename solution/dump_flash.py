from machine import Pin, SPI
import time

# SPI Commands
READ_DATA = 0x03

# SPI Pins
SPI_SCK = 2   # Clock
SPI_MOSI = 3  # TX
SPI_MISO = 0  # RX
CS_PIN = 1    # Chip Select
POWER_PIN = 4 # Power for Flash chip

cs = Pin(CS_PIN, Pin.OUT)
pw = Pin(POWER_PIN, Pin.OUT)

spi = SPI(0, baudrate=1000, polarity=0, phase=1, sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))


# Function to select the flash chip (low active)
def select_chip():
    cs.value(0)
    time.sleep_us(10)

# Function to deselect the flash chip
def deselect_chip():
    time.sleep_us(10)
    cs.value(1)

def read_data(address, length):
    select_chip()
    rxdata = bytearray(length)
    spi.write_readinto(bytes([READ_DATA]) + address.to_bytes(3, 'big') + bytes(length-4), rxdata)
    deselect_chip()
    return rxdata[4:]

#
# Main Run
#

deselect_chip()
pw.value(1)
time.sleep(1) 

address = 0x00d120
data = read_data(address, 64)
print("Dumped data:", [hex(x) for x in data])
