#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
try:
    n = float(input("Ingrese un número: "))
    print(n - int(n))
except ValueError:
    print("No es un número válido")