#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.
try:
    cateto1 = float(input('Ingrese el cateto a: '))
    cateto2 = float(input('Ingrese el cateto b: '))
    print(f"La hipotenusa es {((cateto1))**2+((cateto2)**2)**0.5}")
except ValueError:
    print("No es un número válido")