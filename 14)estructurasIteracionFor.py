# 🔁 Iteraciones con for en Python

# 📋 1️⃣ Iteración de una Lista con continue y break

# Lista de países americanos (con Finlandia como excepción)
paises_de_america = ['Argentina', 'Brasil', 'Peru', 'Chile', 'Uruguay', 'Finlandia']

print("### Iteración de lista ###\n")

for pais in paises_de_america:
    if len(pais) < 6:
        continue  # Si el nombre del país tiene menos de 6 letras, se saltea
    if pais == 'Finlandia':
        break  # Si el país es Finlandia, termina el bucle
    print("🌎 País actual en el recorrido:", pais)

# 🔢 2️⃣ Iteración de una Tupla

numeros = (1, 6, 9, 4, 7, 5)

print("\n### Iteración de tupla ###\n")

for numero in numeros:
    print("🔸 Número actual:", numero)

# 🗂️ 3️⃣ Iteración de un Diccionario (key-value)

productos = {
    "nombre": "Samsung",
    "categoria": "Televisor",
    "stock": 100,
    "activo": True
}

print("\n### Iteración de diccionario ###\n")

for clave, valor in productos.items():
    print(f"🔑 Clave: {clave} → Valor: {valor}")

# 🔁 4️⃣ Iteración con range()

print("\n### Iteración con range() ###\n")

for numero in range(1, 10):  # Del 1 al 9 (el 10 no se incluye)
    print("🔢 Número actual:", numero)

# 🧪 Ejemplo: Enumeración con enumerate()

print("\n### Extra: Uso de enumerate() con lista ###")

for indice, pais in enumerate(paises_de_america):
    print(f"{indice + 1}. {pais}")
