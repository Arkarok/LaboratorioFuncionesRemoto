print("Algoritmo potencia")

while True:
  a=int(input("Digita un numero: "))
  if a==0:
    print("El valor 0 no esta contemplado")
    break
  
  b=int(input("Digita otro numero: "))
  def potencia(a,b):
      pro=a
      for i in range(1,b):
        pro=pro*a
        
      print(pro)
    
  potencia(a,b)
  
print("Final del programa")
