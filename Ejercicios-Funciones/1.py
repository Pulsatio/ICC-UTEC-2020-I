def maravilla(operacion,a,b):
	if operacion=="+":
		return a+b
	elif operacion=="-":
		return a-b
	elif operacion=="*":
		return a*b
	elif operacion=="/":
		if b!=0:
			return a/b
		else:
			print("Error el divisor no puede ser 0")
			return
	else:
		print("operacion invalida")
		return
