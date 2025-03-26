# ⚖️ Estructuras Condicionales en Python

# 📌 Declaramos una variable con el número a evaluar
numero_a_evaluar = 16

print("### 🧪 Evaluación de condiciones con 'if' ###")

# ✅ Estructura básica con if
if numero_a_evaluar < 20:
    print("1️⃣ El número es menor a 20")
    print("   Además, debe ser mayor a 10")
    print("   Y también debe ser mayor a cero")

# ✅ Sentencia pass: se utiliza cuando aún no queremos escribir el código del bloque
if numero_a_evaluar > 20:
    pass  # Esto evita un error de indentación si dejamos el bloque vacío

# ✅ Estructura if/else para evaluar si el número es par o impar
if (numero_a_evaluar % 2) == 0:
    print("2️⃣ El número es par")
else:
    print("2️⃣ El número es impar")

# ✅ Estructura if/elif/else para evaluar si el número es positivo, negativo o cero
if numero_a_evaluar > 0:
    print("3️⃣ El número es positivo")
elif numero_a_evaluar < 0:
    print("3️⃣ El número es negativo")
else:
    print("3️⃣ El número es cero")

# 🧪 Ejemplo: Validación de edad

edad = 17

print("\n### 🧪 Ejemplo adicional: Validación de edad ###")
if edad >= 18:
    print("✅ Puede ingresar al sistema")
else:
    print("❌ Debe ser mayor de edad para ingresar")
