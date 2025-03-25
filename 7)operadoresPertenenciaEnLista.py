# 📌 OPERADORES DE PERTENENCIA
# Sirven para verificar si un elemento pertenece o no a una colección (lista, tupla, string, etc.)

paises_de_america = ['Argentina', 'Brasil', 'Peru', 'Chile', 'Uruguay']

print("### Operadores de Pertenencia ###\n")

# Verificamos si un país está en la lista
print("¿'Peru' está en la lista de países de América? →", 'Peru' in paises_de_america)  # True

# Verificamos si un país NO está en la lista
print("¿'Italia' NO está en la lista? →", 'Italia' not in paises_de_america)  # True

# Verificamos un país mal escrito (¡cuidado con los errores!)
print("¿'Ecudor' está en la lista? →", 'Ecudor' in paises_de_america)  # False, error de ortografía

# Ejemplo con nombre correcto
print("¿'Ecuador' está en la lista? →", 'Ecuador' in paises_de_america)  # False, no está

# Agregamos Ecuador a la lista
paises_de_america.append('Ecuador')
print("Agregamos 'Ecuador' a la lista.")
print("¿Ahora 'Ecuador' está en la lista? →", 'Ecuador' in paises_de_america)  # True

print("\n✅ elemento in lista devuelve True si el elemento está en la lista.\n")
print("❌ elemento not in lista devuelve True si el elemento no está en la lista.\n")
print("⚠️ El operador distingue mayúsculas, minúsculas y errores de ortografía.\n")
print("🔄 Podés modificar la lista con métodos como .append() para agregar elementos.\n")

# 📌 Extra: También funciona con cadenas de texto
frase = "Python es un lenguaje muy versátil"
print("\n### Pertenencia en cadenas de texto ###")
print("'lenguaje' in frase →", 'lenguaje' in frase)  # True
print("'java' in frase →", 'java' in frase)  # False

