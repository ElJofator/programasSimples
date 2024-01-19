#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
texto_hora_actual = input("Hora actual (hh:mm): ")
paso = int(input("Cantidad de horas: "))
bandera = True
cont = 0
texto_minutos = "0"
texto_hora = ""
while(bandera and cont < len(texto_hora_actual)):
    if(texto_hora_actual[cont] != ":"):
        texto_hora += texto_hora_actual[cont]
        cont += 1
    else:
        texto_minutos = texto_hora_actual[-2:]
        bandera = False
hora = int(texto_hora)
minutos = int(texto_minutos)
hora_final = hora + paso
while(hora_final > 24):
    hora_final -= 24
seccion = "am"
if(hora_final > 12):
    hora_final -= 12
    seccion = "pm"
mensaje = f"En {paso} horas, el reloj marcará las {hora_final}"
if(minutos != 0):
    mensaje += f":{minutos}"
else:
    mensaje += ":00"
print(mensaje, seccion)