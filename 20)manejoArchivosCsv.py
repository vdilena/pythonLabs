# 📄 Lectura de archivos CSV en Python

import csv

# 📌 Creamos una matriz para almacenar las filas y columnas
matriz_usuarios = []

# 📥 Leemos archivo CSV
with open('usuarios.csv', mode='r') as archivo:
    lector_csv = csv.reader(archivo, delimiter=';')  # Usamos punto y coma como separador
    matriz_usuarios = list(lector_csv)  # Convertimos el objeto en una lista de listas

# ✅ Mostramos el contenido almacenado
print("### 👥 Matriz de usuarios almacenada desde el archivo CSV ###\n")

for fila in matriz_usuarios:
    print(" ➤", fila)

# Explicaciones

#  csv.reader()	Permite leer un archivo CSV línea por línea.
# delimiter=';'	Especifica el separador de columnas (usualmente ; o ,).
# list(reader)	Convierte el lector en una lista de listas (filas y columnas).
# with open(...) Abre el archivo y se asegura de que se cierre correctamente.