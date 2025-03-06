import modulos.variables
from modulos.funciones import mostrarNombrePaises as mp,sumar as sum
from datetime import datetime
from math import sqrt
from io import open

# Uso de funciones de otro modulo
mp()
print(f'La suma es {sum(2,5)}')
# Uso de modulo datetime
print(datetime.now())
# Uso de modulo math para obtener raiz cuadrada
print(sqrt(16))
# Uso de modulo io para leer archivos en modo lectura "r"
archivo = open("archivo.txt", "r")
contenido = archivo.read()
print(f'El contenido del archivo es {contenido}')
archivo.close()
archivo = open("archivo.txt", "w")
archivo.write("Este va a ser el texto del archivo ahora")
archivo.close()
