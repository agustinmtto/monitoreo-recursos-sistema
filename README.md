# Monitoreo de Recursos del Sistema en Linux

Este es mi primer proyecto. En este script, he creado una herramienta para monitorear el uso de CPU, memoria y disco en el sistema. Los datos recolectados se guardan en un archivo CSV con marcas de tiempo, lo que permite hacer un seguimiento continuo del rendimiento del sistema. Este proyecto tiene como objetivo aprender y practicar la interacción con el sistema operativo Linux mediante Python, además de trabajar con archivos CSV y realizar monitoreo de recursos.

## Requisitos

- Python 3.x
- `psutil`: para instalarlo, ejecuta `pip install psutil`

## Uso

Ejecuta el script en la terminal:

```bash
python monitor.py
```

# Instalación
Sigue estos pasos para clonar el repositorio y configurar el entorno:

1- Clona el repositorio: 
```bash
git clone https://github.com/agustinmtto/monitoreo-recursos-sistema.git
```

2- Navega al directorio del proyecto:
```bash
cd monitoreo-recursos-sistema
```

3- Instala las dependencias necesarias:
```bash
pip install psutil
```

# Uso
Para ejecutar el script: python monitor.py


# Ejemplo de Salida
2024-11-07 15:30:01 | CPU: 23%, Memoria: 45%, Disco: 60%

Los datos también se guardan en reporte_recursos.csv.

# Detener la Ejecución
Para detener el script, presiona Ctrl + C en la terminal.


# Autor
Desarrollado por Agustín Maretto.
