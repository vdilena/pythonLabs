from calculadora import Calculadora

#Ejecucion de metodos estaticos
suma = Calculadora.sumar(3,5)
resta = Calculadora.restar(6,4)
multiplicacion = Calculadora.multiplicar(8,2)
division = Calculadora.dividir(9,3)
potencia = Calculadora.potencia(2,3)

print(f'Suma: {suma}')
print(f'Resta: {resta}')
print(f'Multplicacion: {multiplicacion}')
print(f'Division: {division}')
print(f'Potencia: {potencia}')