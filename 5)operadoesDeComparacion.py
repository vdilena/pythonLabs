# 📌 OPERADORES DE COMPARACIÓN EN PYTHON

print("### Operadores de Comparación ###\n")

# Igualdad
print("¿5 es igual a 2? →", 5 == 2)  # False

# Desigualdad
print("¿9 es distinto de 3? →", 9 != 3)  # True

# Mayor que
print("¿9 es mayor que 3? →", 9 > 3)  # True

# Menor que
print("¿10 es menor que 20? →", 10 < 20)  # True

# Mayor o igual que
print("¿12 es mayor o igual que 5? →", 12 >= 5)  # True

# Menor o igual que
print("¿7 es menor o igual que 11? →", 7 <= 11)  # True

# 🧪 Ejemplo práctico con variables

edad_juan = 22
edad_maria = 30

print("\n### Comparaciones con Variables ###\n")

print(f"Juan tiene {edad_juan} años.")
print(f"María tiene {edad_maria} años.\n")

print("¿Juan y María tienen la misma edad?", edad_juan == edad_maria)
print("¿Juan es menor que María?", edad_juan < edad_maria)
print("¿Juan tiene al menos 18 años?", edad_juan >= 18)
print("¿María es mayor de 25 años?", edad_maria > 25)
