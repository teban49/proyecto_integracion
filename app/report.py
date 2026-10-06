import csv, json
from collections import Counter

def generar_reporte():
    with open('telemetry.csv') as f:
        filas = list(csv.DictReader(f))
    
    contador = Counter(r['classification'] for r in filas)
    total = len(filas)
    
    reporte = {
        'total_registros': total,
        'normales': contador.get('NORMAL', 0),
        'anomalias': contador.get('ANOMALY', 0),
        'tasa_anomalias': f"{contador.get('ANOMALY',0)/total*100:.2f}%" if total else "0%"
    }
    
    with open('report.json', 'w') as f:
        json.dump(reporte, f, indent=2)