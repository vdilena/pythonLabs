# Quiero sumar
# resultado = numeroUno + numeroDos
#print("El resultado es ", resultado)

# Quiero restar
#resultado = numeroUno - numeroDos
#print("El resultado es ", resultado)
#print("El resultado es " + str(resultado))

# Quiero multiplicar
#resultado = numeroUno * numeroDos
#print("El resultado es ", resultado)
#print("El resultado es " + str(resultado))

# Quiero dividir
#resultado = numeroUno / numeroDos
#print("El resultado es ", resultado)
#print("El resultado es " + str(resultado))

# Decoradores
def decoradorOperaciones(funcionRetornaOperacion):
    def funcionEjecutoraOperacion(n1, n2):
        return funcionRetornaOperacion(n1, n2)
    return funcionEjecutoraOperacion

# Creamos una funcion
@decoradorOperaciones
def sumar(n1, n2):
    return n1 + n2

@decoradorOperaciones
def restar(n1, n2):
    return n1 - n2

@decoradorOperaciones
def multiplicar(n1, n2):
    return n1*n2

@decoradorOperaciones
def dividir(n1, n2):
    return n1/n2

# Quiero hacer la operacion que recibo por input
def ejecutarOperacion (n1, n2, operacion):
    if operacion == "SUM":
        return sumar(n1, n2)
    elif operacion == "RES":
        return restar(n1, n2)
    elif operacion == "MUL":
        return multiplicar(n1, n2)
    elif operacion == "DIV":
        try:
            return dividir(n1, n2)
        except ZeroDivisionError:
            return "No se puede dividir por cero"
    else:
        print("Operacion invalida")

numeroUno = None
numeroDos = None

while (not isinstance(numeroUno, int) and not isinstance(numeroDos, int)):
    try:
        numeroUno = int(input("Ingrese el primer numero: "))
        numeroDos = int(input("Ingrese el segundo numero: "))
    except:
        continue

tipoOperacion = input("Tipo operacion: SUM, RES, MUL, DIV: ").upper()
print("El resultado de la operacion es " + str(ejecutarOperacion(numeroUno, numeroDos, tipoOperacion)))

