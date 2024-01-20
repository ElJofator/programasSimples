#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
import math

try:
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Perímetro: {2*math.pi*radio}\nÁrea: {math.pi*radio**2}")
except ValueError:
    print("No es un número válido")