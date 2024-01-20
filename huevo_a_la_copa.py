#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.
import math

M = 47 #masa
p = 1.038 #densidad
c = 3.7 #capacidad calórica específica
K = 0.0054 #conductividad térmica
Tw = 100 #Temperatura de la ebullición del agua
Ty = 70 #Temperatura máxima para hacer huevo a la copa

try:
    T0 = float(input("Ingrese la temperatura del huevo: "))

    t = (M**(2/3)*c*p**(1/3))/(K*math.pi**2*(4*math.pi/3)**(2/3))*math.log(0.76*(T0-Tw)/(Ty-Tw))
    print(f"El tiempo que toma el huevo para llegar a {Ty}°C es: {t} segundos")
except ValueError:
    print("No es un número válido")
    