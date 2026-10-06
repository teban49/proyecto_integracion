def clasificar(data):
    if data['temperature'] > 40 or data['humidity'] > 90:
        return "ANOMALY"
    return "NORMAL"