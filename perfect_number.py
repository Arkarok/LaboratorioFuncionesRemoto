print("Funcion numeros Casi perfectos")

a=int(input("Digita un numero: "))

def casi_perfecto(a):
	suma=0
	
	for i in range(1,a):
		if a%i==0:
			suma+=i
	if suma<=(a-3):
		print("El numero no es un numero casi perfecto")

	else:
		print("El numero es un numero casi perfecto")

casi_perfecto(a)

print("Final del programa")


