import random
 
numero_sorteado = random.randint(1, 50)
tentativa = 1
 
while True:
  try:
    numero_palpite = int(input("Jogo: Descubra o número entre 1 e 50. Insira seu palpite: "))
  except ValueError:
    print("Digite um número entre 1 e 50!")
    continue
 
  if numero_palpite < 1 or numero_palpite > 50:
    print("Digite um número entre 1 e 50!")
    continue
 
  elif numero_palpite == numero_sorteado:
    print(f"Você acertou! Você utilizou {tentativa} tentativa(s).")
    break
 
  else:
    tentativa += 1
    if numero_sorteado > numero_palpite:
      print(f"Você errou! O número é maior que {numero_palpite}")
    else:
      print(f"Você errou! o número é menor que {numero_palpite}")
