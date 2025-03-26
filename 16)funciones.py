# 🔧 Funciones en Python

# 🟢 1️⃣ Procedimiento: función sin retorno
paises_de_america = ['Argentina', 'Brasil', 'Peru', 'Chile', 'Uruguay']

def mostrar_nombre_paises():
    print("🌎 Paises de América:")
    for pais in paises_de_america:
        print(" -", pais)

# mostrar_nombre_paises()

# 🔢 2️⃣ Función con retorno y parámetro por defecto

def sumar(a, b=2):
    return a + b

# print("Resultado suma:", sumar(5, 8))
# print("Resultado suma con valor por defecto:", sumar(5))

# ➕ 3️⃣ Función con *args (cantidad variable de argumentos)

def suma_numeros(a, *numeros):
    resultado = a
    for numero in numeros:
        resultado += numero
    return resultado

# print("Resultado suma múltiple:", suma_numeros(5, 6, 7, 3, -1, 7, 12))

# 🧾 4️⃣ Función con **kwargs (argumentos con clave y valor)

def mostrar_datos_empleado(nombre, **datos_adicionales):
    print(f"👤 Nombre: {nombre}")
    for clave, valor in datos_adicionales.items():
        print(f"   ➤ {clave}: {valor}")

# mostrar_datos_empleado("Juan", apellido="Perez", puesto="Contador", edad=39, sueldo=900000)

# 🎀 5️⃣ Decoradores: funciones que modifican el comportamiento de otras

def decorador_operaciones(funcion_operacion):
    def funcion_ejecutora(a, b):
        print(f"Ejecutando operación entre {a} y {b}")
        return funcion_operacion(a, b)
    return funcion_ejecutora

@decorador_operaciones
def sumar_numeros(a, b):
    return a + b

@decorador_operaciones
def restar_numeros(a, b):
    return a - b

@decorador_operaciones
def multiplicar_numeros(a, b):
    return a * b

@decorador_operaciones
def dividir_numeros(a, b):
    return a / b

# print("Suma:", sumar_numeros(6, 3))
# print("Resta:", restar_numeros(6, 3))
# print("Multiplicación:", multiplicar_numeros(6, 3))
# print("División:", dividir_numeros(6, 3))

# ⚡ 6️⃣ Función lambda (función anónima)

potencia = lambda a, b: a ** b
# print("Potenciación (2^3):", potencia(2, 3))


# 🔁 7️⃣ Uso de map() para transformar listas

numeros = [4, 1, 4, 2, 9]
lista_con_suma_cinco = map(lambda x: x + 5, numeros)
# print("Lista con +5 a cada número:", list(lista_con_suma_cinco))

# 🚦 8️⃣ Uso de filter() para filtrar listas

paises_de_europa = ['Italia', 'Suiza', 'Portugal', 'Suecia']
tiene_mas_de_cinco_caracteres = lambda pais: len(pais) > 5

paises_filtrados = filter(tiene_mas_de_cinco_caracteres, paises_de_europa)
print("Paises con más de 5 caracteres:", list(paises_filtrados))


