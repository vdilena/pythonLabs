# 📌 TIPOS DE DATOS EN PYTHON

# Números
variable_numerica = 1234  # Tipo int (número entero)
variable_decimal = 12.34  # Tipo float (número decimal)
variable_numero_complejo = 2 + 3j  # Tipo complex (número complejo)

# Variables especiales
variable_nula = None  # Tipo None (ausencia de valor)

# Cadenas de texto
variable_string = "Esta es una variable de tipo String"  # Tipo str (cadena de caracteres)

# Valores booleanos
variable_booleana = True  # Tipo bool (Verdadero o Falso)

# Estructuras de datos en Python
variable_lista_numeros = [2, 1, -2, 5, 17, 55]  # Tipo list (lista mutable)
variable_tupla_paises = ("Argentina", "Suiza", "Italia", "Brasil")  # Tipo tuple (tupla inmutable)
variable_diccionario_producto = {
    'nombre': 'Televisor',
    'precio': 120000,
    'stock': 50
}  # Tipo dict (diccionario clave-valor)
variable_set_numeros = {2, 5, 2, 9, 7}  # Tipo set (conjunto sin elementos duplicados)

# 📌 Imprimimos los valores y explicamos su uso
print("### 📝 EJEMPLOS DE TIPOS DE DATOS EN PYTHON ###\n")

print(f"1️⃣ Número Entero (int): {variable_numerica}")
print(f"2️⃣ Número Decimal (float): {variable_decimal}")
print(f"3️⃣ Número Complejo (complex): {variable_numero_complejo}\n")

print(f"4️⃣ Variable Nula (None): {variable_nula}\n")

print(f"5️⃣ Cadena de Texto (str): {variable_string}")
print(f"   Ejemplo: Longitud de la cadena → len(variable_string) = {len(variable_string)}\n")

print(f"6️⃣ Valor Booleano (bool): {variable_booleana}")
print(f"   Ejemplo: Negamos el valor → not variable_booleana = {not variable_booleana}\n")

print(f"7️⃣ Lista (list): {variable_lista_numeros}  ✅ Se pueden modificar")
print(f"   Ejemplo: Agregamos un número → variable_lista_numeros.append(100)")
variable_lista_numeros.append(100)
print(f"   Nueva lista: {variable_lista_numeros}\n")

print(f"8️⃣ Tupla (tuple): {variable_tupla_paises}  🚫 No se pueden modificar")
print(f"   Ejemplo: Intentar modificarla generará un error → variable_tupla_paises[0] = 'España' ❌\n")

print(f"9️⃣ Diccionario (dict): {variable_diccionario_producto}  🔑 Usa clave-valor")
print(f"   Ejemplo: Acceder al precio → variable_diccionario_producto['precio'] = {variable_diccionario_producto['precio']}")
print(f"   Modificar el stock → variable_diccionario_producto['stock'] = 45")
variable_diccionario_producto['stock'] = 45
print(f"   Diccionario actualizado: {variable_diccionario_producto}\n")

print(f"🔟 Conjunto (set): {variable_set_numeros}  🚀 No permite duplicados")
print(f"   Ejemplo: Agregamos un número → variable_set_numeros.add(10)")
variable_set_numeros.add(10)
print(f"   Nuevo conjunto: {variable_set_numeros}\n")