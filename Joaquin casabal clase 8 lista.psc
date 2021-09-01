Algoritmo lista
	Imprimir "con este sistema podra crear listas de alumnos para organizarse mejor"
	imprimir "Cuantos alumnos tiene?"
	leer n
	Dimension nombres[n]
	Dimension edad[n]
	Dimension año[n]
	cantidadVueltas<-n
	
	imprimir "Anota los nombres y las edades de los alumnos uno por uno "
	
	Para i<-1 Hasta cantidadVueltas
		Imprimir "Escriba el nombre: "
		Leer nombres[i]
	FinPara
	
	imprimir "ahora anota las edades"
	
	para i<-1 Hasta cantidadVueltas
		Imprimir "anote la edad: "
		Leer edad[i]
	FinPara
	
	Imprimir "Ahora anota en que año estan los alumnos"
	
	Para i<-1 hasta cantidadVueltas
		Imprimir "año de su alumno"
		Leer año[i]
	FinPara
	
	imprimir "Estos son los nombres de los alumnos y sus edades: "
	imprimir " "
	imprimir "---------------"
	
	Para i<-1 hasta cantidadVueltas
		Imprimir "Nombre: " nombres[i]
		Imprimir "Edad: " edad[i]
		imprimir "año: " año[i]
		imprimir "---------------"
	FinPara
	
FinAlgoritmo