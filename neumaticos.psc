Algoritmo neumaticos
	
	respuesta = 0
	
	Imprimir "Bienvenido al sistema de control de neumaticos de auto"
	Imprimir ""
	Imprimir "Para comprobar las medidas del producto ingrese los valores correspondientes"
	Imprimir "Los valores aceptados son:"
	Imprimir ""
	Imprimir "6, 6.5, 7 y 7.5 pulgadas"
	Imprimir ""
	Imprimir "AYUDA:"
	Imprimir "Utilice puntos en vez de comas"
	Imprimir "Solo ingrese numeros"
	Imprimir "Ingrese los numeros en pulgadas"
	Imprimir "El valor no puede ser mayor que 7.5 pulgadas"
	Imprimir "El valor no puede ser menor que 6 pulgadas"
	Imprimir ""
	Imprimir "Ahora debe ingresar el tamaño de la llanta"
	Imprimir "Ingrese el tamano de la llanta en pulgadas: "
	leer respuesta
	
	
	Si respuesta = 6 Entonces
		Imprimir "El neumatico es de 6 pulgadas"
		Imprimir "Ahora ingrese el ancho del neumatico en milimetros(mm)"
		Leer n
		
		Si n = 175 o n = 195 o n = 185 Entonces
			Imprimir "El tamaño: " n "mm cumple con los estandares de calidad"
			Imprimir "El neumatico es compatible con llantas de 6 pulgadas"
		SiNo
			Imprimir "El neumatico no cumple los estandares de calidad"
			Imprimir "El tamaño: " n "mm es incorrecto"
			Imprimir ""
			Imprimir "AYUDA:"
			Imprimir "Ingrese los datos denuevo correctamente o pruebe el mismo valor para otro tipo de llanta"
		FinSi
		
		
	FinSi
	Si respuesta = 6.5 Entonces
		Imprimir "El neumatico es de 6.5 pulgadas"
		Imprimir "Ahora ingrese el ancho del neumatico en milimetros(mm)"
		Leer n
		
		Si n = 185 o n = 195 o n = 205 Entonces
			Imprimir "El tamaño: " n "mm cumple con los estandares de calidad"
			Imprimir "El neumatico es compatible con llantas de 6.5 pulgadas"
		SiNo
			Imprimir "El neumatico no cumple los estandares de calidad"
			Imprimir "El tamaño: " n "mm es incorrecto"
			Imprimir ""
			Imprimir "AYUDA:"
			Imprimir "Ingrese los datos denuevo correctamente o pruebe el mismo valor para otro tipo de llanta"
		FinSi
		
		
	FinSi
	Si respuesta = 7 Entonces
		Imprimir "El neumatico es de 7 pulgadas"
		Imprimir "Ahora ingrese el ancho del neumatico en milimetros(mm)"
		Leer n
		
		Si n = 195 o n = 205 o n = 215 Entonces
			Imprimir "El tamaño: " n "mm cumple con los estandares de calidad"
			Imprimir "El neumatico es compatible con llantas de 7 pulgadas"
		SiNo
			Imprimir "El neumatico no cumple los estandares de calidad"
			Imprimir "El tamaño: " n "mm es incorrecto"
			Imprimir ""
			Imprimir "AYUDA:"
			Imprimir "Ingrese los datos denuevo correctamente o pruebe el mismo valor para otro tipo de llanta"
		FinSi
		
		
	FinSi
	Si respuesta = 7.5 Entonces
		Imprimir "El neumatico es de 6 pulgadas"
		Imprimir "Ahora ingrese el ancho del neumatico en milimetros(mm)"
		Leer n
		
		Si n = 205 o n = 215 o n = 225 Entonces
			Imprimir "El tamaño: " n "mm cumple con los estandares de calidad"
			Imprimir "El neumatico es compatible con llantas de 7.5 pulgadas"
		SiNo
			Imprimir "El neumatico no cumple los estandares de calidad"
			Imprimir "El tamaño: " n "mm es incorrecto"
			Imprimir ""
			Imprimir "AYUDA:"
			Imprimir "Ingrese los datos denuevo correctamente o pruebe el mismo valor para otro tipo de llanta"
		FinSi
		
		
	FinSi
	Si respuesta > 7.5 o respuesta < 6 Entonces
		Imprimir "El tamaño: " respuesta " de la llanta es incorrecto"
		Imprimir "Recuerde que los valores aceptados son:"
		Imprimir "6, 6.5, 7, 7.5"
		Imprimir "Vuelva a ingresar los datos correctamente"
	FinSi
	
	
	
	Imprimir ""
	Imprimir "Gracias por utilizar el sistema de mediciones michelin"
	Imprimir "Cualquier duda consulte el manual de usuario"
	Imprimir "Que tenga un buen dia"
FinAlgoritmo
