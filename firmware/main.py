# firmware/main.py - MicroPython para ESP32 en Wokwi
import dht, machine, time, json

# Configuración del sensor DHT22 (pin 4) y botón integrado (pin 0)
sensor = dht.DHT22(machine.Pin(4))
boton = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

device_id = "ESP32_WOKWI_01"

while True:
    try:
        sensor.measure()
        temperatura = round(sensor.temperature(), 1)
        humedad = round(sensor.humidity(), 1)
        estado_boton = "PRESIONADO" if boton.value() == 0 else "LIBRE"

        # Condición anómala: temperatura > 40 o humedad > 90
        estado = "ANOMALY" if (temperatura > 40 or humedad > 90) else "NORMAL"

        mensaje = {
            "device_id": device_id,
            "timestamp": time.time(),
            "temperature": temperatura,
            "humidity": humedad,
            "button": estado_boton,
            "status": estado
        }
        print(json.dumps(mensaje))
    except OSError as e:
        print(json.dumps({"device_id": device_id, "error": str(e)}))
    time.sleep(2)  # DHT22 requiere 2s entre lecturas