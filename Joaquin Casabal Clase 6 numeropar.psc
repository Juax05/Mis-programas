Funcion ValorRetornado <- numeroPar (unNumero)
	Si (unNumero mod 2) = 0
		ValorRetornado = Verdadero
	SiNo
		ValorRetornado = Falso
	FinSi
	
FinFuncion

Algoritmo numerosPares
	Escribir "Ingresa un numero y yo te digo si es par o es impar"
	Leer n
	Si numeroPar(n)
		Escribir "El numero es par"
	SiNo
		Escribir "El numero es impar"
	FinSi
FinAlgoritmo
