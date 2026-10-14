import csv
import os


def persistir(data, clasificacion, texto_telemetria):
    ruta = "telemetry.csv"
    existe = os.path.isfile(ruta) and os.path.getsize(ruta) > 0
    with open(ruta, "a", newline="", encoding="utf-8") as f:
        campos = (
            "timestamp",
            "device_id",
            "temperature",
            "humidity",
            "classification",
            "telemetry_text",
        )
        writer = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        if not existe:
            writer.writeheader()
        writer.writerow({
            **data,
            "classification": clasificacion,
            "telemetry_text": texto_telemetria,
        })
