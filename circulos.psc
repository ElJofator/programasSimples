Algoritmo circulo
	Definir texto_radio Como Cadena
	Definir radio Como Real
	Escribir 'Ingrese el radio del c�rculo:'
	Leer texto_radio
	radio <- ConvertirANumero(texto_radio)
	perimetro <- 2*PI*radio
	area <- PI*radio^2
	Escribir 'Per�metro: ', perimetro
	Escribir '�rea: ', area
FinAlgoritmo