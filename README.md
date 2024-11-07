# Monitoreo de Recursos del Sistema en Linux

Este script permite monitorear el uso de CPU, memoria y disco en el sistema y guarda los datos en un archivo CSV con marcas de tiempo.

## Requisitos

- Python 3.x
- `psutil`: para instalarlo, ejecuta `pip install psutil`

## Uso

Ejecuta el script en la terminal:

```bash
python monitor.py


# Instalación
Sigue estos pasos para clonar el repositorio y configurar el entorno:

1- Clona el repositorio: 
git clone https://github.com/agustinmtto/monitoreo-recursos-sistema.git

2- Navega al directorio del proyecto:
cd monitoreo-recursos-sistema

3- Instala las dependencias necesarias:
pip install psutil

# Uso
Para ejecutar el script: python monitor.py


# Ejemplo de Salida
2024-11-07 15:30:01 | CPU: 23%, Memoria: 45%, Disco: 60%
2024-11-07 15:30:11 | CPU: 25%, Memoria: 50%, Disco: 63%

Los datos también se guardan en reporte_recursos.csv.

# Detener la Ejecución
Para detener el script, presiona Ctrl + C en la terminal.


# Autor
Desarrollado por Agustín Maretto.
