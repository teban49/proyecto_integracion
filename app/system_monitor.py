import psutil


def estado_sistema():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memoria_percent": psutil.virtual_memory().percent,
    }