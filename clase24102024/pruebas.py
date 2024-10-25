import csv

#Generamos una matriz
matrizDatosUniversitarios = []

# Lectura del archivo csv
with open('datos_universitarios.csv') as archivo: # Abrimos el archivo en modo lectura
    #csv_reader = csv.reader(archivo, delimiter=',') # Determinamos el delimitador usado en el archivo

    # Comenzamos a leer cada linea
    #for row in csv_reader:
        #print(type(row)) 

    # Guardamos los elementos en una matriz
    matrizDatosUniversitarios = list(csv.reader(archivo, delimiter=','))

# Matriz de 1000 * 6
# print(matrizDatosUniversitarios[2])

# Guardar lista de edades
edades = []
contador = 0
for itemMatriz in matrizDatosUniversitarios:
    #print(itemMatriz)
    #print(len(itemMatriz))
    if contador == 0:
        contador +=1
        continue
    edades.append(itemMatriz[3])
    contador +=1
contador = 0
#print(edades)
# Hago el saneamiento de datos
edadesSaneadas = []
for edad in edades:
    if edad == '' or int(edad) < 17 or int(edad) > 120:
        continue
    edadesSaneadas.append(int(edad))

#print(edadesSaneadas)
#print(f"Cantidad de elementos de edades sin sanear: {len(edades)}")
#print(f"Cantidad de elementos de edades saneados: {len(edadesSaneadas)}")

# Obtengo promedio de edades en general prom = sum elementos/#elementos
sumaElementosLista = sum(edadesSaneadas)
# print(sumaElementosLista)
cantidadElementosListaEdades = len(edadesSaneadas)
promedio = sumaElementosLista/cantidadElementosListaEdades
#print(f"Promedio: {promedio}")

# Ahora quiero obtener La media de edades que hay en Argentina para la carrera Medicina
edadesDeARGEstudianMED = []
for itemMatriz in matrizDatosUniversitarios:
    if contador == 0:
        contador +=1
        continue
    pais = itemMatriz[1]
    carrera = itemMatriz[2]
    if pais == "Argentina" and carrera == "Medicine":
        #print(itemMatriz)
        edadesDeARGEstudianMED.append(int(itemMatriz[3]))
    contador +=1

#print(f"Cantidad edades de ARG que estudian MED: {len(edadesDeARGEstudianMED)}")
sumaEdadesMedArg = sum(edadesDeARGEstudianMED)
cantidadEdadesMedArg = len(edadesDeARGEstudianMED)
promedioEdadMedArg = sumaEdadesMedArg/cantidadEdadesMedArg
print(f"Promedio de edad de personas que estudian medicina en ARG: {promedioEdadMedArg}")