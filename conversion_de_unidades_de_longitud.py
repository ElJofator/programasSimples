#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
try:
    longitud = float(input("Ingrese longitud: "))
    print(f"{longitud} cm = {longitud/2.54} in")
except ValueError:
    print("No es un número válido")