# Monitoreo de Recursos del Sistema en Linux
Este es mi primer proyecto. En este script, desarrollé una herramienta para monitorear el uso de CPU, memoria y disco en un sistema Linux. Los datos recopilados se muestran en la consola y se guardan en un archivo CSV llamado `reporte_recursos.csv`. El objetivo de este proyecto fue aplicar los conocimientos adquiridos sobre scripting en Linux.

## Características

- Monitorea el uso de CPU, memoria y disco en tiempo real.
- Permite especificar un intervalo de tiempo para el monitoreo.
- Guarda un reporte en formato CSV con la fecha, hora, uso de CPU, uso de memoria y uso de disco.
- El monitoreo se detiene presionando `Ctrl + C`.

## Requisitos

Este script está diseñado para sistemas basados en Linux y requiere las siguientes herramientas:
- `vmstat` (para obtener el uso de CPU)
- `free` (para obtener el uso de memoria)
- `df` (para obtener el uso de disco)

## Uso

1. Clona el repositorio o descarga el archivo `monitor.sh` en tu sistema.
2. Abre una terminal y navega hasta el directorio donde se encuentra `monitor.sh`.
3. Asigna permisos de ejecución al archivo:

   ```bash
   chmod +x monitor.sh
   ```
4. Ejecuta el script:
  ```bash
./monitor.sh
  ```
Ingresa el intervalo de tiempo en segundos para el monitoreo cuando se te solicite (debe ser un número mayor o igual a 1).

## Ejemplo de Salida en la Consola
2024-11-07 15:30:01 | CPU: 23%, Memoria: 45%, Disco: 60%

## Archivos generados
`reporte_recursos.csv`: Archivo CSV que contiene las métricas registradas en cada intervalo especificado por el usuario. Incluye los siguientes campos:
* Timestamp: Fecha y hora del registro
* CPU (%): Porcentaje de uso de CPU
* Memoria (%): Porcentaje de uso de memoria
* Disco (%): Porcentaje de uso de disco

## Nota
El archivo reporte_recursos.csv se sobrescribe cada vez que se ejecuta el script.

## Autor
Desarrollado por Agustín Maretto.
