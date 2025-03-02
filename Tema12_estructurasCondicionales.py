# Uso de estructura if
numeroAEvaluar = 16
if numeroAEvaluar < 20:
    print("El numero es menor a 20")
    print("Pero el numero debe ser mayor a 10")
    print("Y el numero debe ser mayor a cero")

# Uso de sentencia pass
if numeroAEvaluar > 20:
    pass

# Uso de estructura if/else
if (numeroAEvaluar % 2) == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# Uso de estrucutra elif
if numeroAEvaluar > 0:
    print("El numero es positivo")
elif numeroAEvaluar < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")