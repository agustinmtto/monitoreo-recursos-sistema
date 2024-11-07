import psutil
import csv
import time

# Mensaje de bienvenida
print("Bienvenido al sistema de monitoreo de recursos.")
print("Este programa monitorea el uso de CPU, memoria y disco.")
print("Para detener la ejecución, presiona Ctrl + C.")

# Solicitar al usuario que ingrese el intervalo de tiempo
tiempo = 0
while tiempo < 1:
    tiempo = int(input("Ingrese cada cuantos segundos desea monitorear el sistema (mayor o igual a 1 segundo): "))
    if tiempo < 1:
        print("El intervalo debe ser mayor o igual a 1 segundo. Intenta de nuevo.")

# Aquí comenzaría el monitoreo con el intervalo que el usuario ha seleccionado
print(f"Monitoreo comenzado. Intervalo: {tiempo} segundos.")



# Función para obtener las métricas del sistema
def obtener_datos():
    # Obtén el porcentaje de uso de CPU
    cpu = psutil.cpu_percent(interval=1)
    # Obtén el uso de memoria
    memoria = psutil.virtual_memory().percent
    # Obtén el uso de disco
    disco = psutil.disk_usage('/').percent
    
    return cpu, memoria, disco

# Función para guardar los datos en un archivo CSV
def guardar_en_csv(cpu, memoria, disco):
    with open('reporte_recursos.csv', mode='a') as archivo:
        escritor = csv.writer(archivo)
        # Escribe los datos de CPU, memoria y disco junto con la hora actual
        escritor.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), cpu, memoria, disco])

# Inicializa el archivo CSV con encabezados (solo la primera vez)
with open('reporte_recursos.csv', mode='w') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Timestamp", "CPU (%)", "Memoria (%)", "Disco (%)"])

# Bucle principal para monitorear el sistema
try:
    while True:
        cpu, memoria, disco = obtener_datos()
        # Obtener la hora actual para mostrar en consola
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S")
        # Imprimir en consola con la fecha y hora
        print(f"{fecha_hora} | CPU: {cpu}%, Memoria: {memoria}%, Disco: {disco}%")
        guardar_en_csv(cpu, memoria, disco)
        # Espera 10 segundos antes de obtener los datos nuevamente
        time.sleep(tiempo)
except KeyboardInterrupt:
    print("\nMonitoreo detenido por el usuario.")
