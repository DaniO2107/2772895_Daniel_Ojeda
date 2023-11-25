numeros = []
contador = 0
while contador < 5:
	try: 
		numero = float(input("Ingrese por teclado"))
		numeros.append(numero)
		contador += 1
	except ValueError:
		print("No es un numero par")

if numeros:
	promedio  = sum(numeros) / len(numeros)
	print(f"los numeros ingresados son {numeros }")
	print(f"el promedio de los numeros son {promedio}")
else:
	print("No se imgreso numeros")
		
	




