print("Funcion numeros perfectos")

a=int(input("Digita un numero: "))

def perfect_number(a):
	suma=0
	
	for i in range(1,a):
		if a%i==0:
			suma+=i
	if suma==a:
		print("El numero es un numero perfecto")

	else:
		print("El numero no es un numero perfecto")

perfect_number(a)

print("Final del programa")


