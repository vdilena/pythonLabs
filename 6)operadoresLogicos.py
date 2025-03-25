# 📌 OPERADORES LÓGICOS EN PYTHON
# Los operadores lógicos se usan para combinar condiciones.

print("### Operadores Lógicos en Python ###\n")

# OR (o): Devuelve True si al menos una de las condiciones es verdadera
print("1️⃣ OR: (3 == 2) or (5 == 5) →", (3 == 2) or (5 == 5))  # True, porque 5 == 5 es True

# AND (y): Devuelve True solo si TODAS las condiciones son verdaderas
print("2️⃣ AND: ('hola' == 'hola') and (True == True) and (2.3 == 2.3) →", 
      ('hola' == 'hola') and (True == True) and (2.3 == 2.3))  # True

# NOT (no): Invierte el valor lógico (True → False, False → True)
esta_activo = True
print("3️⃣ NOT: not esta_activo (donde esta_activo = True) →", not esta_activo)  # False

# 💡 Ejemplo práctico con lógica de usuario

print("\n### Ejemplo práctico: Ingreso a un sistema ###")

usuario_valido = True
clave_correcta = False

print("¿Puede acceder al sistema?", usuario_valido and clave_correcta)  # False

print("\n### Otro ejemplo: Descuento en tienda ###")

es_estudiante = True
tiene_cupon = False

print("¿Tiene descuento?", es_estudiante or tiene_cupon)  # True
