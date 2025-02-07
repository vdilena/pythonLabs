import csv

# Lectura del archivo csv
with open('hollywood_actors_filmography_with_type.csv') as archivo: # Abrimos el archivo csv

    # Guardamos los elementos en una matriz
    matrizDatos = list(csv.reader(archivo, delimiter=','))

#print(matrizDatos)

#Cuál fue el año que se lanzaron más y cuál fue el que se lanzaron menos películas.
aniosLanzamiento = {}
actorPorCalificacionMas60 = {}
ratings = []
actoresConMas60 = []
leyoHeader = False
for fila in matrizDatos:

    # Descartamos lectura de header
    if not leyoHeader:
        leyoHeader = True
        continue
    #print(fila[2])

    # Guardo el diccionario de los anios de lanzamiento
    if aniosLanzamiento.get(fila[2]) == None:
        aniosLanzamiento[fila[2]] = 0
    else:
        aniosLanzamiento[fila[2]] += 1

    # Guardo el diccionario de cant veces de los actores con calif mayor a 60
    if actorPorCalificacionMas60.get(fila[0]) == None:
        actorPorCalificacionMas60[fila[0]] = {"anios": [fila[2]], "cantidadVeces": 0}
    else:
        actorPorCalificacionMas60[fila[0]]["anios"].append(fila[2])
        actorPorCalificacionMas60[fila[0]]["cantidadVeces"] += 1

    # Guardo la lista de ratings
    rating = int (fila[4].replace("%",""))
    ratings.append(rating)


#print(aniosLanzamiento)
#print(f"Ratings: {ratings}")

menorCantidadPeliculas = min(aniosLanzamiento.values())
mayorCantidadPeliculas = max(aniosLanzamiento.values())
anioMenosPeliculas = 0
anioMasPeliculas = 0

for anio, cantidadPeliculas in aniosLanzamiento.items():
    #print(type(menorCantidadPeliculas))
    if cantidadPeliculas == menorCantidadPeliculas:
        anioMenosPeliculas = anio
        break

for anio, cantidadPeliculas in aniosLanzamiento.items():
    if cantidadPeliculas == mayorCantidadPeliculas:
        anioMasPeliculas = anio
        break

print(f"Anio menos peliculas: {anioMenosPeliculas}")
print(f"Anio mas peliculas: {anioMasPeliculas}")

#Cual es el promedio de los ratings de Rotten Tomatoes de las películas que se lanzaron en el año 2020
promedioRating = sum(ratings) / len(ratings)
print(f"Promedios: {promedioRating}")

""" Una lista con los actores de series con una calificación superior al 60% de Rotten Tomatoes, en la que aparezca la siguiente información:
Nombre del actor/actriz
Año más actual donde se obtuvo esa calificación
Cantidad de veces en las que obtuvo esa calificación """
print(actorPorCalificacionMas60)