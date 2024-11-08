import asyncio
from bleak import (
    BleakScanner,
    BLEDevice,
)


devices = {}
MAX_DEVICES = 10

async def main():
    stop_event = asyncio.Event()
    def callback(device:BLEDevice, advertisement_data):
        devices[device.address] = {"name": device.name, "advertisement_data": advertisement_data}
        print(device.name," - ",device.details['props'].get("ManufacturerData", {}))
        if(len(devices) >= MAX_DEVICES): stop_event.set()

    async with BleakScanner(callback) as scanner: 
        print("Scanning...")
        await stop_event.wait()

if __name__ == '__main__':
    asyncio.run(main())

