# Ciclo while
indice = 0
sumatoria = 0
while indice < 10:
    sumatoria += 1
    print("Indice:" + str(indice))
    indice +=1
else:
    print("Primera sumatoria:" + str(sumatoria))
indice = 0

# Ciclo while con break y continue
while indice < 10:
    if indice % 2 == 0:
        print("Indice par:" + str(indice))
        indice +=1
        continue # Si es un numero par, sigo al proximo paso de la iteracion
    if indice > 8:
        print("Es mayor a 8")
        indice = 10
        break # Si es 9 se detiene la iteracion
    indice +=1
else:
    print("Ultimo indice:" + str(indice))