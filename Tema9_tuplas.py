tuplaNumeros = (1, 9, 4, 7, 9)
listaPaises = ["Italia", "Suiza", "Irlanda","Noruega"]
tuplaPaises = tuple(listaPaises)
print(tuplaNumeros)
print(tuplaPaises)
print(tuplaPaises[2]) # Accedo al tercer elemento de la tupla
print(len(tuplaPaises)) # Obtengo la longitud de la tupla
# Hago un unpack de la tupla de paieses
(primero, segundo, tercero, cuarto) = listaPaises
print(f'Primer pais: {primero}, segundo pais: {segundo}, tercer pais: {tercero}')
tuplaNumeros[1] = 10 # Esto deberia dar error, porque las tuplas son inmutables