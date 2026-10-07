# Instrucciones

1. Instala las extensiones **Python** y **Wokwi Simulator** en Visual Studio Code.
2. Desde la carpeta `integracion` (la carpeta principal que abriste en VS Code), instala las dependencias: `python -m pip install -r requirements.txt`.
3. Abre en VS Code la carpeta `integracion` que contiene `proyecto_integracion`.
4. Abre `proyecto_integracion/wokwi.toml` y ejecuta **F1 → Wokwi: Select Config File** para seleccionarlo.
5. Confirma que exista `proyecto_integracion/.wokwi/ESP32_GENERIC-20251209-v1.27.0.bin`.
6. Ejecuta **F1 → Wokwi: Start Simulator**. Wokwi inicia automáticamente `proyecto_integracion/main.py`, que ejecuta el firmware de `firmware/main.py`.
7. Desde `proyecto_integracion`, ejecuta `python -m app.main`. La terminal mostrará cada lectura como JSON con `status` igual a `NORMAL` o `ANOMALY`.
8. No ejecutes al mismo tiempo la tarea **Ver telemetria Wokwi** ni otro monitor serial: solo un proceso debe leer el puerto.
9. Para generar el reporte después de recibir datos, ejecuta `python -m app.report` desde `proyecto_integracion`.
