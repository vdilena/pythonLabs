# 🔷 Sets (Conjuntos) en Python
# 📌 Un set es una colección desordenada, sin elementos duplicados.

# ✅ Crear un set directamente con llaves {}
set_de_numeros = {1, 9, -4, 8, 7, 4, 1, 9, -7}
print("1️⃣ Set de números (se eliminan duplicados automáticamente):", set_de_numeros)

# ✅ Crear un set a partir de una lista con set()
set_paises = set(["Italia", "Alemania", "Suiza", "Eslovenia", "Croacia"])
print("2️⃣ Set de países creado desde una lista:", set_paises)

# ✅ Obtener la cantidad de elementos únicos
print("3️⃣ Cantidad de elementos únicos en el set de números:", len(set_de_numeros))

# ✅ Usar sorted() para ver los elementos en orden (sin modificar el set)
set_duplicado = {"Italia", "Alemania", "Suiza", "Eslovenia", "Croacia", "Alemania", "Eslovenia"}
set_ordenado = sorted(set_duplicado)
print("4️⃣ Set ordenado (sorted):", set_ordenado)

# 🧪 Ejemplo práctico de uso

print("\n### 🧪 Eliminar duplicados de una lista con set() ###")
lista_con_duplicados = [1, 1, 2, 3, 2, 4, 5, 5, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print("Lista original:", lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)
