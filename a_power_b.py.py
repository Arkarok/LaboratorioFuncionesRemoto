print("Algoritmo potencia")

a=int(input("Digita un numero: "))
b=int(input("Digita otro numero: "))

def potencia(a,b):
  pro=a
  for i in range(1,b):
    pro=pro*a
    
  print(pro)

potencia(a,b)    
    
print("Final del programa")