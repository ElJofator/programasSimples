#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
n = 4
suma = 0
for i in range(0,n):
    try:
        suma += float(input(f"Ingresa el número {i+1}: "))
    except ValueError:
        print("No es un número válido")
        break
print(f"El promedio es: {suma/n}")