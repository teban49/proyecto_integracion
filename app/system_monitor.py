import psutil, platform, os

def estado_sistema():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memoria_percent": psutil.virtual_memory().percent,
        "disco_percent": psutil.disk_usage('/').percent,
        "so": platform.system(),
        "cwd": os.getcwd()
    }