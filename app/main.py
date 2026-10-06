import logging
import time

import serial

from .acquisition import crear_conexion, leer_y_validar
from .classifier import clasificar
from .persistence import persistir
from .system_monitor import estado_sistema


def ejecutar():
    while True:
        ser = crear_conexion()
        if ser is None:
            time.sleep(5)
            continue

        mensajes = 0
        try:
            while True:
                data = leer_y_validar(ser)
                if data is None:
                    continue

                clasificacion = clasificar(data)
                persistir(data, clasificacion)
                logging.info(f"{data['device_id']} → {clasificacion}")
                mensajes += 1

                if mensajes % 10 == 0:
                    estado = estado_sistema()
                    logging.info(f"CPU: {estado['cpu_percent']}% | "
                                 f"RAM: {estado['memoria_percent']}%")
        except serial.SerialException as error:
            logging.error(f"Conexión perdida: {error}")
        finally:
            ser.close()

        time.sleep(5)

if __name__ == "__main__":
    ejecutar()