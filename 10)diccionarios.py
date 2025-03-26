# 📘 Diccionarios en Python (dict)

# 📌 Definición de un diccionario usando llaves {}
producto = {
    "nombre": "Samsung",
    "categoria": "Televisor",
    "stock": 100,
    "activo": True
}

# 📌 Otra forma de crear un diccionario: usando dict()
empleado = dict([
    ("nombre", "Carolina"),
    ("apellido", "Gomez"),
    ("edad", 37),
    ("jefe", True)
])

print("### 📂 DICCIONARIOS EN PYTHON ###\n")

# ✅ Mostrar ambos diccionarios completos
print("1️⃣ Diccionario 'producto':", producto)
print("2️⃣ Diccionario 'empleado':", empleado)

# ✅ Acceder a un valor usando la clave (key)
print("\n3️⃣ Categoría del producto:", producto["categoria"])

# ✅ Modificar el valor de una clave existente
empleado["edad"] = 34
print("4️⃣ Edad modificada de empleado:", empleado["edad"])

# ✅ Agregar una nueva clave con su valor
empleado["sueldo"] = 900000
print("5️⃣ Diccionario 'empleado' con nuevo campo 'sueldo':", empleado)

# ✅ Obtener todas las claves y todos los valores
print("\n6️⃣ Claves del diccionario 'producto':", list(producto.keys()))
print("7️⃣ Valores del diccionario 'empleado':", list(empleado.values()))

# ✅ Usar el método get() para acceder a un valor (más seguro que usar [])
print("8️⃣ Categoría del producto (usando get):", producto.get("categoria"))

# ✅ Eliminar una clave con del
del empleado["jefe"]
print("9️⃣ Diccionario 'empleado' sin la clave 'jefe':", empleado)

# ✅ Obtener la cantidad de elementos (pares clave-valor)
print("🔟 Longitud del diccionario 'producto':", len(producto))

print("\n### 🧪 Ejemplo: Consultar clave inexistente con get() ###")
precio = producto.get("precio", "No especificado")
print("Precio del producto:", precio)  # Devuelve valor por defecto
