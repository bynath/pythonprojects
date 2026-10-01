import time

while True:
  try:
    numero = int(input("digite um numero para iniciar a contagem regressiva: "))
  except ValueError:
    print("Informe um número inteiro!")
    continue

  if numero < 1:
    print("Informe um número positivo!")
    continue
  
  for numero in range(numero, 0, -1):
    print(numero)
    time.sleep(1)

  print("FIM")

  break
