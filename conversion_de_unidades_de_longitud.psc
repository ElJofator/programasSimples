Algoritmo conversion_de_unidades_de_longitud
	Definir texto_medida Como Cadena
	Definir medida, pulgadas Como Real
	Escribir "Ingrese longitud:"
	Leer texto_medida
	medida = ConvertirANumero(texto_medida)
	pulgadas = medida/2.54
	Escribir medida, " cm = ", pulgadas, " in"
FinAlgoritmo