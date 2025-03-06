primerNumero = 2
segundoNumero = 0

try:
    print(primerNumero / segundoNumero)
except:
    print("No se puede devidir por cero!")


primerNumero = 'Hola'
segundoNumero = 4
try:
    print(primerNumero / segundoNumero)
except ZeroDivisionError:
    print("No se puede devidir por cero!")
except TypeError:
    print("No se puede hacer operaciones entre numeros y letras")
else:
    print("Fin de ejecucion de bloque try/except")

primerPalabra = "Hola"
segundaPalabra = " Mundo"

if len(primerPalabra) + len(segundaPalabra) > 6:
    raise NameError('Las palabras concatenadas no pueden tener mas de 6 letras')