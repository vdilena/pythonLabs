# Conversión de tipos de datos en Python

# Definimos un número entero
numero = 1254  

# Convertimos el número a diferentes tipos de datos
numero_en_formato_float = float(numero)  # Convertimos el número a tipo float (decimal)
numero_en_formato_string = str(numero)   # Convertimos el número a tipo str (cadena de texto)
numero_en_formato_int = int(numero_en_formato_string)  # Convertimos la cadena nuevamente a entero

# Obtenemos el tipo de dato de la variable numero_en_formato_string
tipo_de_dato = type(numero_en_formato_string)

# Mostramos los resultados de las conversiones
print("### Conversión de Tipos de Datos en Python ###\n")

print(f"1️⃣ Número original (int): {numero}")
print(f"2️⃣ Convertido a float: {numero_en_formato_float}  🔹 Ahora tiene decimales")
print(f"3️⃣ Convertido a string: '{numero_en_formato_string}'  📝 Ahora es un texto")
print(f"4️⃣ Convertido de nuevo a int: {numero_en_formato_int}  🔄 Regresamos a un número entero")
print(f"5️⃣ Tipo de dato de 'numero_en_formato_string': {tipo_de_dato}  📌 Es un texto\n")
