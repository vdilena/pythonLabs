# 🔐 Tuplas en Python (inmutables)

# 📌 Definimos una tupla de números
tupla_numeros = (1, 9, 4, 7, 9)  # Las tuplas permiten valores repetidos

# 📌 Creamos una lista de países y luego la convertimos en tupla
lista_paises = ["Italia", "Suiza", "Irlanda", "Noruega"]
tupla_paises = tuple(lista_paises)

print("### 📦 TUPLAS EN PYTHON ###\n")

# ✅ Mostrar tuplas completas
print("1️⃣ Tupla de números:", tupla_numeros)
print("2️⃣ Tupla de países:", tupla_paises)

# ✅ Acceder a un elemento por índice
print("3️⃣ Tercer país en la tupla:", tupla_paises[2])  # Irlanda

# ✅ Longitud de una tupla
print("4️⃣ Cantidad de países en la tupla:", len(tupla_paises))  # 4

# ✅ Desempaquetar (unpack) una tupla
(primero, segundo, tercero, cuarto) = tupla_paises
print("5️⃣ Desempaquetado:")
print(f"   ➤ Primer país: {primero}")
print(f"   ➤ Segundo país: {segundo}")
print(f"   ➤ Tercer país: {tercero}")
print(f"   ➤ Cuarto país: {cuarto}")

# ❌ Intento de modificar una tupla (error)

print("\n### 🚫 Intento de modificación de tupla ###")
try:
    tupla_numeros[1] = 10  # Esto genera un error
except TypeError as e:
    print("Error:", e)
    print("⚠️ No se puede modificar una tupla porque es inmutable.")
