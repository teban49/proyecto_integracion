import time, logging
import serial

if __package__ in (None, ""):
    from acquisition import crear_conexion, leer_y_validar
    from classifier import clasificar
    from persistence import persistir
    from system_monitor import estado_sistema
else:
    from .acquisition import crear_conexion, leer_y_validar
    from .classifier import clasificar
    from .persistence import persistir
    from .system_monitor import estado_sistema


def ejecutar():
    while True:  # RF09: no se detiene ante fallos
        ser = crear_conexion()
        if ser is None:
            logging.error("Reintentando en 5s...")
            time.sleep(5)
            continue

        try:
            for i in range(30):  # ~60 segundos de operación
                data = leer_y_validar(ser)
                if data is None:
                    continue

                clasificacion = clasificar(data)
                persistir(data, clasificacion)
                logging.info(f"{data['device_id']} → {clasificacion}")

                # Consultar SO cada 10 mensajes
                if i % 10 == 0:
                    estado = estado_sistema()
                    logging.info(f"CPU: {estado['cpu_percent']}% | "
                                 f"RAM: {estado['memoria_percent']}%")
        except serial.SerialException:
            logging.error("Conexión perdida, reconectando...")
        finally:
            ser.close()
            time.sleep(5)


if __name__ == "__main__":
    ejecutar()