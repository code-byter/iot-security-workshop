I recorded some data between my BLE enabled temperature sensor and phone. You can find the wireshark captures in `wireshark_captures/smart_power_socket.pcapng` 

## Challenge 0x01: Advertisements

The MAC address of the sensor is `a4:c1:38:65:12:fc`. What's the device name?

## Challenge 0x02: Services and Characteristics

Which characteristic contains the temperature and humidity data


What's the temperature and humidity in my room?

<details>
  <summary>Hint</summary>
  
  The temperature value consists of the first two bytes. To decode it, you can use the `wireshark_captures/decode.py` python script
</details>