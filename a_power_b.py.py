
def potencia(a,b):
  pro=1
  
  for i in range(1,b):
    if i>100:
      raise(Exception("Programa muy amplio"))
    pro=pro*a  
  print(pro)  
  
  return pro
  
print("Algorito potencia")  

bug=0

while True:
  try:
    
    a=int(input("Digita un numero: "))
    
    if a==0:
      break
    
    B=int(input("Digita un numero: "))
    
    prod=potencia(a,b)
    print(prod)
  except:
    print("Hay un error en el sistema :'v")
    bug+=1
    
print("Final del programa")