from machine import Pin, SPI
import time

# SPI Commands
READ_DATA = 

# SPI Pins
SPI_SCK =
SPI_MOSI =
SPI_MISO =
CS_PIN =
POWER_PIN =

spi = SPI()


# Function to select the flash chip (low active)
def select_chip():


# Function to deselect the flash chip
def deselect_chip():

def read_data(address, length):

#
# Main Run
#
data = read_data(address, 64)
print("Dumped data:", [hex(x) for x in data])
