import json
import logging

import serial

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def crear_conexion():
    try:
        ser = serial.serial_for_url(
            "rfc2217://localhost:4000",
            baudrate=115200,
            timeout=3,
        )
        logging.info("Conectado al simulador Wokwi")
        return ser
    except serial.SerialException as e:
        logging.error(f"Error de conexión: {e}")
        return None


def leer_y_validar(ser):
    try:
        linea = ser.readline().decode("utf-8").strip()
        if not linea:
            return None

        data = json.loads(linea)
        if not isinstance(data, dict):
            logging.warning("Dato inválido: se esperaba un objeto JSON")
            return None
        if "error" in data:
            logging.warning(f"Error del dispositivo: {data['error']}")
            return None

        temperatura = data["temperature"]
        humedad = data["humidity"]
        if (
            "device_id" not in data
            or "timestamp" not in data
            or not isinstance(temperatura, (int, float))
            or not isinstance(humedad, (int, float))
            or not 0 < temperatura < 100
            or not 0 <= humedad <= 100
        ):
            logging.warning("Dato inválido: campos faltantes o fuera de rango")
            return None

        return data
    except (KeyError, TypeError, ValueError) as e:
        logging.warning(f"Dato inválido: {e}")
        return None