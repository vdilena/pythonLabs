# Leo datos ingresados por el usaurio
nombre = input("Cual es su nombre? ")
apellido = input("Y tu apellido? ")
print(f'Nombre {nombre}, Apellido: {apellido}')

# Leo datos ingresados con formatos numericos
primerNumero = int(input("Ingrese el primero numero: "))
segundoNumero = int(input("Ingrese el segundo numero: "))
print(f'La suma de {primerNumero} y {segundoNumero} es {primerNumero + segundoNumero}')

# Leo varios datos al mismo tiempo y hago la asignacion con la funcion split()
primero, segundo, tercero = input("Ingrese primer segundo tercer numero: ").split()
print(f'La multiplicacion de {primero} * {segundo} * {tercero} es igual a {int(primero) * int(segundo) * int(tercero)}')