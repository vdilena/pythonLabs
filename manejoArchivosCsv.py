import csv

# Creamos una matriz para almacenar las filas y columnas
matrizUsuarios = []

# Leemos archivo csv
with open('usuarios.csv') as archivo: # Abrimos el archivo en modo lectura
    """ csv_reader = csv.reader(archivo, delimiter=';') # Determinamos el delimitador usado en el archivo

    # Comenzamos a leer cada linea
    for row in csv_reader:
        print(row) """

    # Guardamos los elementos en una matriz
    matrizUsuarios = list(csv.reader(archivo, delimiter=';'))

# Recorremos la matriz
print("Matriz de usuario almacenada")
print(matrizUsuarios)