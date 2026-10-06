import serial, json, logging, time

logging.basicConfig(
    filename='system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def crear_conexion():
    try:
        # Conexión al puerto RFC2217 de Wokwi
        ser = serial.serial_for_url('rfc2217://localhost:4000', 
                                     baudrate=115200, timeout=3)
        logging.info("Conectado al simulador Wokwi")
        return ser
    except serial.SerialException as e:
        logging.error(f"Error de conexión: {e}")
        return None

def leer_y_validar(ser):
    """Valida estructura, tipo y rango"""
    try:
        linea = ser.readline().decode('utf-8').strip()
        if not linea:
            return None
        
        data = json.loads(linea)
        
        # Validación de campos
        if 'error' in data:
            logging.warning(f"Error del dispositivo: {data['error']}")
            return None
        
        assert 'device_id' in data
        assert 0 < data['temperature'] < 100
        assert 0 <= data['humidity'] <= 100
        
        return data
    except json.JSONDecodeError:
        logging.warning("JSON malformado, descartado")
        return None
    except (KeyError, AssertionError) as e:
        logging.warning(f"Dato inválido: {e}")
        return None