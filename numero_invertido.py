#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
n = input("Ingrese el número: ")
inverso = ""
for i in range(len(n)):
    inverso += n[-(i+1)]
print(inverso)