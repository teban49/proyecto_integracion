import json
import logging
import time

import serial

from .acquisition import crear_conexion, leer_y_validar
from .classifier import clasificar
from .persistence import persistir
from .system_monitor import estado_sistema


def ejecutar():
    print("App iniciada. Esperando la simulacion de Wokwi...", flush=True)

    while True:
        ser = crear_conexion()
        if ser is None:
            print("Wokwi no esta conectado en localhost:4000; reintentando.", flush=True)
            time.sleep(5)
            continue

        print("Conectado a Wokwi; esperando telemetria...", flush=True)
        ultimo_aviso = time.monotonic()
        mensajes = 0
        try:
            while True:
                data = leer_y_validar(ser)
                if data is None:
                    if time.monotonic() - ultimo_aviso >= 10:
                        print(
                            "Sin telemetria. Mantenga visible la simulacion Wokwi "
                            "y cierre otros monitores seriales conectados al puerto.",
                            flush=True,
                        )
                        ultimo_aviso = time.monotonic()
                    continue

                clasificacion = clasificar(data)
                persistir(data, clasificacion)
                print(
                    json.dumps({**data, "status": clasificacion}, ensure_ascii=False),
                    flush=True,
                )
                logging.info(f"{data['device_id']} → {clasificacion}")
                ultimo_aviso = time.monotonic()
                mensajes += 1

                if mensajes % 10 == 0:
                    estado = estado_sistema()
                    logging.info(f"CPU: {estado['cpu_percent']}% | "
                                 f"RAM: {estado['memoria_percent']}%")
        except serial.SerialException as error:
            logging.error(f"Conexión perdida: {error}")
            print(f"Conexion serial perdida: {error}", flush=True)
        finally:
            ser.close()

        time.sleep(5)

if __name__ == "__main__":
    ejecutar()