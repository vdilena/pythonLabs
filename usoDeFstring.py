# Imprimo por pantalla con f-string de variables sueltas
nombre = 'Carolina'
apellido = 'Gomez'
edad = 29
print(f'Nombre {nombre}, Apellido: {apellido}, Edad: {edad}')

# Imprimo por pantalla con f-string de un diccionario
empleado = dict([
    ("nombre", "Carolina"),
    ("apellido", "Gomez"),
    ("edad", 37),
    ("jefe", True)
])

for key,value in empleado.items():
    print(f"{key} : {value}")