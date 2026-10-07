import dht
import json
import time
from machine import Pin

sensor = dht.DHT22(Pin(4))
device_id = "ESP32_WOKWI_01"

while True:
    try:
        sensor.measure()
        temperatura = round(sensor.temperature(), 1)
        humedad = round(sensor.humidity(), 1)
        status = "ANOMALY" if temperatura > 40 or humedad > 90 else "NORMAL"
        print(json.dumps({
            "device_id": device_id,
            "timestamp": time.time(),
            "temperature": temperatura,
            "humidity": humedad,
            "status": status
        }))
    except OSError as e:
        print(json.dumps({"device_id": device_id, "error": str(e)}))
    time.sleep(2)