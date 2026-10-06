import csv, os

def persistir(data, clasificacion):
    ruta = 'telemetry.csv'
    existe = os.path.isfile(ruta)
    with open(ruta, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'timestamp', 'device_id', 'temperature', 
            'humidity', 'button', 'classification'])
        if not existe:
            writer.writeheader()
        writer.writerow({
            'timestamp': data['timestamp'],
            'device_id': data['device_id'],
            'temperature': data['temperature'],
            'humidity': data['humidity'],
            'button': data['button'],
            'classification': clasificacion
        })
