#EJERCICIO 3
#Pedir datos al usuario
#Pedir la renta anual al usuario
Renta = float(input("Intruduce tu Renta Anual (soles): "))

if Renta <10000:
    tipo_impositivo = "5%"
elif 10000 <= Renta <= 20000:
    tipo_impositivo = "15%"
elif 20000 < Renta <= 35000:
    tipo_impositivo = "20%"
elif 35000 < Renta <= 60000:
    tipo_impositivo = "30%"
else: 
    tipo_impositivo = "45%"
    

print(f"Tu tipo impositivo es: {tipo_impositivo}.")
    
    