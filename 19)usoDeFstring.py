# 🖨️ Impresión por pantalla con f-strings

# 🔤 1️⃣ F-string con variables sueltas

# Definición de variables individuales
nombre = 'Carolina'
apellido = 'Gomez'
edad = 29

# Impresión usando f-string (forma moderna y clara)
print("### Datos personales con variables sueltas ###")
print(f"👤 Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")

# 📋 2️⃣ F-string con datos desde un diccionario

# Definición de un diccionario con datos de un empleado
empleado = {
    "nombre": "Carolina",
    "apellido": "Gomez",
    "edad": 37,
    "jefe": True
}

# Impresión de cada clave y valor usando f-string
print("\n### Datos del diccionario 'empleado' ###")
for clave, valor in empleado.items():
    print(f"🔹 {clave.capitalize()}: {valor}")

