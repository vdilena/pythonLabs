# 🖨️ Impresión por pantalla con f-strings

# 🔤 1️⃣ F-string con variables sueltas

# Definición de variables individuales
nombre = 'Carolina'
apellido = 'Gomez'
edad = 29

# Impresión usando f-string (forma moderna y clara)
print("### Datos personales con variables sueltas ###")
print(f"👤 Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")

# 📋 2️⃣ F-string con datos desde un diccionario

# Definición de un diccionario con datos de un empleado
empleado = {
    "nombre": "Carolina",
    "apellido": "Gomez",
    "edad": 37,
    "jefe": True
}

# Impresión de cada clave y valor usando f-string
print("\n### Datos del diccionario 'empleado' ###")
for clave, valor in empleado.items():
    print(f"🔹 {clave.capitalize()}: {valor}")

# Metodos de string #

# capitalize() se utiliza para poner la primera letra en mayúscula y el resto en minúscula, mejorando la presentación de las claves del diccionario al imprimirlas.
s = "lenguajes de programacion"
print(s.capitalize())

# swapcase() se utiliza para invertir el caso de cada letra en la cadena, cambiando mayúsculas a minúsculas y viceversa.
s = "LenGUaJEs DE progrAMACion"
print(s.swapcase())

# upper() se utiliza para convertir toda la cadena a mayúsculas, lo que puede ser útil para resaltar información importante.
s = "lenguajes de programacion"
print(s.upper())

# count() se utiliza para contar cuántas veces aparece una subcadena específica dentro de la cadena principal, lo que es útil para análisis de texto.
s = "lenguajes de programacion "
print(s.count("o"))

# isalnum() se utiliza para verificar si todos los caracteres de la cadena son alfanuméricos (letras y números), lo que puede ser útil para validar entradas de usuario.
s = "jperez@email.com"
print(s.isalnum())

# isalpha() se utiliza para verificar si todos los caracteres de la cadena son letras, lo que puede ser útil para validar nombres o palabras.
s = "abcdefg"
print(s.isalpha())

# strip() se utiliza para eliminar los espacios en blanco al principio y al final de la cadena, lo que es útil para limpiar entradas de usuario.
s = "  abc  "
print(s.strip())

# zfill() se utiliza para rellenar la cadena con ceros a la izquierda hasta alcanzar una longitud específica, lo que puede ser útil para formatear números.
s = "123"
print(s.zfill(5))

# join() se utiliza para unir una lista de cadenas en una sola cadena, utilizando un separador específico, lo que es útil para crear cadenas a partir de listas.
s = " y ".join(["1", "2", "3"])
print(s)

# split() se utiliza para dividir una cadena en una lista de subcadenas, utilizando un separador específico, lo que es útil para analizar cadenas.
s = "Python,Java,C"
print(s.split(","))
