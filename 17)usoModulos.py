# 📦 Uso de Módulos y Archivos en Python

# Importación de un módulo propio
import modulos.variables

# Importación selectiva y con alias desde otro módulo propio
from modulos.funciones import mostrarNombrePaises as mp, sumar as sum

# Importación de módulos de la biblioteca estándar
from datetime import datetime      # Para obtener la fecha y hora actual
from math import sqrt              # Para operaciones matemáticas como raíz cuadrada
from io import open                # Para manipular archivos de texto
import random

# 🧪 Uso de funciones desde módulos propios

print("### 🔧 Funciones desde módulos propios ###\n")

mp()  # Llama a la función mostrarNombrePaises desde otro módulo
print(f'➡️ La suma es: {sum(2, 5)}')  # Llama a la función sumar desde otro módulo

# 🕒 Uso del módulo datetime

print("\n### 🕒 Fecha y hora actual con datetime ###")
print("Fecha y hora actual:", datetime.now())

# 📐 Uso del módulo math

print("\n### 📐 Raíz cuadrada con math.sqrt ###")
print("Raíz cuadrada de 16:", sqrt(16))

# 📄 Manejo de archivos con el módulo io

print("\n### 📄 Lectura y escritura de archivos ###")

# Abrimos un archivo en modo lectura ("r")
archivo = open("archivo.txt", "r")
contenido = archivo.read()
print("📖 Contenido actual del archivo:", contenido)
archivo.close()

# Sobrescribimos el contenido con modo escritura ("w")
archivo = open("archivo.txt", "w")
archivo.write("Este va a ser el texto del archivo ahora")
archivo.close()
print("✅ Archivo actualizado con nuevo contenido.")

# Uso del módulo random
print("\n### 🎲 Generación de números aleatorios con random ###")

# Generamos un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")

# Datos random de listas
paises = ["España", "México", "Argentina", "Colombia", "Chile"]

pais_aleatorio = random.choice(paises)
print(f"País aleatorio de la lista: {pais_aleatorio}") 

sample_paises = random.sample(paises, 3)
print(f"Selección aleatoria de 3 países: {sample_paises}")

