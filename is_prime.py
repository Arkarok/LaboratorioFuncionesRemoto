print("Funcion primo")

n=int(input("Digita un numero: "))

def is_prime():
	cont=0
	for i in range(1,n+1):
		if n%i==0:
			cont+=1
	if cont>2:
		print("Is NOT a prime number")
	else:
		print("Is a prime number")

is_prime()

print("Final del programa")

			