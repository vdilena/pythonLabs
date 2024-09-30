# Iteracion de lista
paisesDeAmerica = list(('Argentina', 'Brasil', 'Peru', 'Chile','Uruguay', 'Finlandia'))
for paisDeAmerica in paisesDeAmerica:
    if len(paisDeAmerica) < 6:
        continue
    if paisDeAmerica == 'Finlandia':
        break
    print("Pais actual en el recorrido: " + paisDeAmerica)

# Iteracion de tupla
numeros = (1, 6, 9, 4, 7, 5)
for numero in numeros:
    print('Numero del indice actual de la tupla: ' + str(numero))

# Iteracion de diccionario
productos = {
    "nombre": "Samsung",
    "categoria": "Televisor",
    "stock": 100,
    "activo": True
}
for keyProducto,valueProducto  in productos.items():
    print("El valor de la key " + keyProducto + " es " + str(valueProducto))

# Iteracion de rangos
for numero in range(1, 10):
    print("Numero actual: " + str(numero))