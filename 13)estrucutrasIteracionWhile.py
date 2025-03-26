# 🔁 Ciclos while en Python

# 📌 CICLO WHILE BÁSICO

indice = 0
sumatoria = 0

print("### 🔁 Primer ciclo while ###\n")

while indice < 10:
    sumatoria += 1
    print("🔸 Índice actual:", indice)
    indice += 1
else:
    # El bloque else se ejecuta si el ciclo while no fue interrumpido por un break
    print("\n✅ El ciclo terminó normalmente")
    print("🧮 Sumatoria final:", sumatoria)

# 🚦 Uso de break y continue dentro de un while

print("\n### 🔁 Segundo ciclo while con 'continue' y 'break' ###\n")

indice = 0

while indice < 10:
    if indice % 2 == 0:
        print("🔹 Índice par:", indice)
        indice += 1
        continue  # Salta al siguiente ciclo sin ejecutar lo que sigue

    if indice > 8:
        print("⚠️ El índice es mayor a 8 → se interrumpe el ciclo con break")
        indice = 10
        break  # Sale del bucle completamente

    indice += 1
else:
    # Este else no se ejecutará porque hubo un break
    print("✅ El ciclo terminó normalmente")
    print("Último índice:", indice)

# 🧪 Ejemplo: Buscar el primer múltiplo de 7

print("\n### 🧪 Ejemplo: Buscar el primer múltiplo de 7 entre 1 y 20 ###")

numero = 1
while numero <= 20:
    if numero % 7 == 0:
        print(f"✅ Encontrado: {numero}")
        break
    numero += 1
