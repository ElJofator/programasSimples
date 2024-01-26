Algoritmo numero_invertido
	Escribir "Ingrese el número:"
	Leer num1
	validacion = Verdadero
	cantidad = Longitud(num1)
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		num = Falso
		Para j <- 0 Hasta 9 Con Paso 1 Hacer
			Si Subcadena(num1, i, i) == ConvertirATexto(j) Entonces
				num = Verdadero
				j = 10
			FinSi
		Fin Para
		Si !num Entonces
			validacion = Falso
			i = cantidad + 1
		FinSi
	Fin Para
	Si validacion Entonces
		inverso = ""
		Para i<-cantidad Hasta 1 Con Paso -1 Hacer
			inverso = Concatenar(inverso,Subcadena(num1,i,i))
		Fin Para
		Escribir inverso
	SiNo
		Escribir "No es un número válido"
	FinSi
FinAlgoritmo
