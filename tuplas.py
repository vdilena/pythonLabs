tuplaNumeros = (1, 9, 4, 7, 9)
listaPaises = ["Italia", "Suiza", "Irlanda","Noruega"]
tuplaPaises = tuple(listaPaises)
print(tuplaNumeros)
print(tuplaPaises)
print(tuplaPaises[2]) # Accedo al tercer elemento de la tupla
print(len(tuplaPaises)) # Obtengo la longitud de la tupla
tuplaNumeros[1] = 10 # Esto deberia dar error, porque las tuplas son inmutables