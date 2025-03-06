paisesDeAmerica = list(('Argentina', 'Brasil', 'Peru', 'Chile','Uruguay'))
paisesDeEuropa = ['Italia', 'Suiza', 'Portugal', 'Suecia']

print(paisesDeAmerica[0]) # Accedo al primer elemento de la lista
paisesDeEuropa[1] = 'Alemania' # Modifico el valor del segundo elemento
print(paisesDeEuropa)
paisesDeEuropa.append('Francia') # Agrego un nuevo elemento a la lista
print(paisesDeEuropa)
print(f'Subconjunto: {paisesDeAmerica[0:3]}') # Obtengo un conjunto de la primera lista
paisesDeAmerica.remove('Brasil') # Elimino uno de los paises de la primera lista
print(paisesDeAmerica)
print(paisesDeAmerica.sort()) # Ordeno de forma asc la primera lista
print(paisesDeEuropa.sort(reverse=True)) # Ordeno de forma desc la primera lista
paisesAmericoEuropeos = paisesDeAmerica + paisesDeEuropa
print(paisesAmericoEuropeos) # Obtengo una union de las dos listas
print(len(paisesAmericoEuropeos)) # Obtengo la cantidad de elementos de la lista