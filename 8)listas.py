# 📌 Definición de listas
paises_de_america = list(('Argentina', 'Brasil', 'Peru', 'Chile', 'Uruguay'))  # También se puede usar list() con una tupla
paises_de_europa = ['Italia', 'Suiza', 'Portugal', 'Suecia']  # Lista creada directamente con corchetes

print("### 🗂️ OPERACIONES CON LISTAS ###\n")

# ✅ Acceder a un elemento por índice
print(f"1️⃣ Primer país de América: {paises_de_america[0]}")  # Argentina

# ✅ Modificar un elemento de la lista
paises_de_europa[1] = 'Alemania'
print(f"2️⃣ Lista de Europa con cambio en el segundo país: {paises_de_europa}")

# ✅ Agregar un nuevo elemento con append()
paises_de_europa.append('Francia')
print(f"3️⃣ Lista de Europa con nuevo país agregado: {paises_de_europa}")

# ✅ Obtener un subconjunto (slice) de una lista
print(f"4️⃣ Subconjunto de los 3 primeros países de América: {paises_de_america[0:3]}")

# ✅ Eliminar un elemento específico por su valor
paises_de_america.remove('Brasil')
print(f"5️⃣ Lista de América luego de eliminar 'Brasil': {paises_de_america}")

# ✅ Ordenar las listas (ascendente por defecto)
paises_de_america.sort()
print(f"6️⃣ Lista de América ordenada (ascendente): {paises_de_america}")

paises_de_europa.sort(reverse=True)
print(f"7️⃣ Lista de Europa ordenada (descendente): {paises_de_europa}")

# ✅ Unir dos listas
paises_americo_europeos = paises_de_america + paises_de_europa
print(f"8️⃣ Unión de América y Europa: {paises_americo_europeos}")

# ✅ Obtener la cantidad total de elementos
print(f"9️⃣ Cantidad total de países en la lista combinada: {len(paises_americo_europeos)}")

# 📌 Explicaciones clave:
print("\n 📌 Acceso por índice: Comienza en 0. lista[0] es el primer elemento.\n")
print("📌 Modificación: Se pueden cambiar los elementos por posición.\n")
print("📌 Método append(): Agrega un elemento al final de la lista.\n")
print("📌 Slice ([0:3]): Permite tomar un subconjunto de la lista.\n")
print("📌 Método remove(): Elimina un elemento por su valor (si existe).\n")
print("📌 Método sort(): Ordena la lista (modifica la lista original).\n")
print("📌 Concatenación (+): Une dos listas en una nueva.\n")
print("📌 len(): Devuelve la cantidad de elementos de una lista.\n")

print("🔄 Observación importante:\n")
print("Las funciones sort() y append() modifican la lista en el lugar (in-place) y no devuelven un valor, por eso al hacer:\n")
print(paises_de_america.sort())
print("Se imprime None. Lo correcto es:\n")
paises_de_america.sort()
print(paises_de_america)



