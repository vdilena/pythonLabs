# Funcion que muestra los paises de America (Procedimiento)
paisesDeAmerica = list(('Argentina', 'Brasil', 'Peru', 'Chile','Uruguay'))

def mostrarNombrePaises():
    for pais in paisesDeAmerica:
        print(pais)

# mostrarNombrePaises()

# Funcion que devuelve el resultado de sumar dos numeros. Tiene un valor por default
def sumar(a, b = 2):
    return a + b