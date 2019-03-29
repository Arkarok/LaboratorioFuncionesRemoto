print("Funcion primo")

cont=0

while True:
	n=int(input("Digita un numero: "))
	if n<=0:
		print("Numeros no contemplados")
		break

	else:
		cont+=1
		print("Primos contados= " + str(cont))

	def is_prime():
		try:
			cont=0
			for i in range(1,n+1):
				if n%i==0:
					cont+=1
			if cont>2:
				print("0")
			else:
				print("1")
		except:
			print("-1")
	is_prime()

print("Final del programa")			