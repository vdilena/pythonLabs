# 🛠️ Manejo de Excepciones en Python (try, except, raise)

# ⚠️ 1️⃣ División por cero (excepción general)
primer_numero = 2
segundo_numero = 0

print("### División por cero con except general ###")

try:
    print(primer_numero / segundo_numero)
except:
    print("❌ No se puede dividir por cero (except genérico)")

# 🎯 2️⃣ Captura de errores específicos (ZeroDivisionError, TypeError)

primer_numero = 'Hola'
segundo_numero = 4

print("\n### Captura de errores específicos ###")

try:
    print(primer_numero / segundo_numero)  # Esto lanza TypeError
except ZeroDivisionError:
    print("❌ No se puede dividir por cero")
except TypeError:
    print("❌ No se pueden hacer operaciones entre números y letras")
else:
    print("✅ Fin de ejecución sin errores")

# 🚨 3️⃣ Lanzar errores manualmente con raise

primer_palabra = "Hola"
segunda_palabra = " Mundo"

print("\n### Uso de raise para lanzar una excepción personalizada ###")

# Validamos la longitud total
longitud_total = len(primer_palabra) + len(segunda_palabra)

if longitud_total > 6:
    raise NameError("❗ Las palabras concatenadas no pueden tener más de 6 letras")


