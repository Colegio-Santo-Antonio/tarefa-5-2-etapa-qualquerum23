numero = input()
impares = []
for i in numero[-1::-2]:
  impares.append(int(1))
pares = []
for i in numeros[-2::-2]:
  if 2*int(i)<10:
    pares.append(2*int(i))
  else:
    pares.append(2*int(i) - 10+1)
  somatório = sum(pares) + sum (ímpares)
  if int(somatório/10) == somatório/10:
    print("Cartão Válido")
    else: 
      print ("Cartão inválido")
  
        

