while 1:
	espacios,caracteres,vocales,consonantes=0,0,0,0
	texto = input("Ingrese el texto con un minimo de 5 palabras : ")
	for c in texto:
		if c==" ":
			espacios+=1
		elif c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
			vocales+=1
		elif ord("a")<=ord(c) or ord(c)<ord("z"):
			consonantes+=1
		caracteres+=1
	if espacios>=4:
		print("total de caracteres ingresados : ",caracteres)
		print("total de vocales :",vocales) 
		print("total de consonantes :",consonantes) 
		print("total de espacios :",espacios) 
		break