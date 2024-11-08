from datetime import datetime

data = [0x00, 0x00, 0x00, 0x00, 0x00]
temperature_bytes = data[:2]
humidity_bytes = data[2]
temperature = int.from_bytes(temperature_bytes, byteorder="little") / 100.0
humidity = humidity_bytes

print("Tempterature: {}°C".format(temperature))
print("Humidity: {}°C".format(humidity))