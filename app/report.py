import csv
import json


def generar_reporte():
    total = normales = anomalias = 0
    with open("telemetry.csv", encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            total += 1
            if fila["classification"] == "NORMAL":
                normales += 1
            elif fila["classification"] == "ANOMALY":
                anomalias += 1

    reporte = {
        "total_registros": total,
        "normales": normales,
        "anomalias": anomalias,
        "tasa_anomalias": (
            f"{anomalias / total * 100:.2f}%" if total else "0%"
        ),
    }

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=2)


if __name__ == "__main__":
    generar_reporte()