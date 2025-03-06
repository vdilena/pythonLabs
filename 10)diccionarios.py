producto = {
    "nombre": "Samsung",
    "categoria": "Televisor",
    "stock": 100,
    "activo": True
}
print(producto)
empleado = dict([
    ("nombre", "Carolina"),
    ("apellido", "Gomez"),
    ("edad", 37),
    ("jefe", True)
])
print(empleado)
print(producto["categoria"]) # Accedo a key categoria
empleado["edad"] = 34 # Modifico el value de la key edad
print(empleado["edad"])
empleado["sueldo"] = 900000 # Agrego la key sueldo al diccionario
print(empleado)
print(producto.keys()) # Obtengo las keys del diccionario
print(empleado.values()) # Obtengo los values del diccionario
print(producto.get("categoria")) # Obtengo el value de la key categoria
del(empleado["jefe"]) # Elimino una key del diccionario
print(empleado)
print(len(producto)) # Obtengo la longitud del diccionario