# 🎤 Lectura de datos desde el teclado en Python

# 🧍 1️⃣ Ingreso de texto (strings)

# Lectura de nombre y apellido ingresados por el usuario
nombre = input("🧑 ¿Cuál es tu nombre? ")
apellido = input("🧑 ¿Y tu apellido? ")
print(f"✅ Nombre: {nombre}, Apellido: {apellido}")

# 🔢 2️⃣ Ingreso de datos numéricos (y conversión a int)

# Se convierten los datos a enteros con int()
primer_numero = int(input("🔢 Ingrese el primer número: "))
segundo_numero = int(input("🔢 Ingrese el segundo número: "))
suma = primer_numero + segundo_numero
print(f"✅ La suma de {primer_numero} y {segundo_numero} es: {suma}")


# 🔗 3️⃣ Ingreso de varios valores en una sola línea con split()

# El usuario escribe 3 números separados por espacio, que se asignan a 3 variables
entrada = input("🔗 Ingrese tres números separados por espacio (ej: 2 4 6): ")
primero, segundo, tercero = entrada.split()

# Convertimos a entero para operar
resultado = int(primero) * int(segundo) * int(tercero)
print(f"✅ La multiplicación de {primero} * {segundo} * {tercero} es igual a {resultado}")


