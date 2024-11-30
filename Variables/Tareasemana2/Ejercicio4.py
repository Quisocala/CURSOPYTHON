#EJERCICIO 4
#Pedir datos al usuario

# Pedir la edad del cliente
edad = int(input("Introduce tu edad: "))

# Calcular el precio según la edad
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio
print(f"El precio de la entrada es: {precio}soles ")
