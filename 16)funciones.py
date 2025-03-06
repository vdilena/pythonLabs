# Funcion que muestra los paises de America (Procedimiento)
paisesDeAmerica = list(('Argentina', 'Brasil', 'Peru', 'Chile','Uruguay'))

def mostrarNombrePaises():
    for pais in paisesDeAmerica:
        print(pais)

# mostrarNombrePaises()

# Funcion que devuelve el resultado de sumar dos numeros. Tiene un valor por default
def sumar(a, b = 2):
    return a + b

# print(sumar(5,8))

# Funcion con args
def sumaNumeros(a, *numeros):

    resultado = a
    for numero in numeros:
        resultado +=  numero
    
    return resultado
    
# print("Resultado: " + str(sumaNumeros(5, 6, 7, 3, -1, 7, 12)))

# Funcion con kwargs
def mostrarDatosEmpleado(nombre, **datosAdicionales):

    print("Nombre: " + nombre)
    for dato in datosAdicionales:
        print(dato + ":" + str(datosAdicionales[dato]))

datosEmpleados = {
    "apellido": "Perez",
    "puesto": "Contador",
    "edad": 39,
    "sueldo": 900000
}
# mostrarDatosEmpleado("Juan",  apellido = "Perez", puesto = "Contador", edad = 39, sueldo = 900000)

# Decoradores
def decoradorOperaciones(funcionRetornaOperacion):
    def funcionEjecutoraOperacion(primerNumero, segundoNumero):
        return funcionRetornaOperacion(primerNumero, segundoNumero)
    return funcionEjecutoraOperacion

@decoradorOperaciones
def sumarNumeros(a,b):
    return a+b

@decoradorOperaciones
def restarNumeros(a,b):
    return a-b

@decoradorOperaciones
def multiplicarNumeros(a,b):
    return a*b

@decoradorOperaciones
def dividirNumeros(a,b):
    return a/b

""" print("Suma: " + str(sumarNumeros(6, 3)))
print("Resta: " + str(restarNumeros(6, 3)))
print("Multiplicacion: " + str(multiplicarNumeros(6, 3)))
print("Division: " + str(dividirNumeros(6, 3))) """

# Funcion lambda
potencia = lambda a, b : a**b
# print("Resultado potenciacion: " + str(potencia(2,3)))

# Map
numeros = [4, 1, 4, 2, 9]
listaConSumaCinco = map(lambda x: x + 5, numeros)
# print(list(listaConSumaCinco))

# Filter
paisesDeEuropa = ['Italia', 'Suiza', 'Portugal', 'Suecia']
def tieneMasDeCincoCaracteres(pais):
    return len(pais) > 5
tieneMasCincoCaracteres = lambda pais : len(pais) > 5
paisesDeMasDeCincoCaracteres = filter(tieneMasCincoCaracteres, paisesDeEuropa)
print(list(paisesDeMasDeCincoCaracteres))