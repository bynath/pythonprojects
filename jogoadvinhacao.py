import random

numero_sorteado = random.randint(1, 50)

while True:
  numero_palpite = int(input("Jogo: Descubra o número entre 1 e 50. Insira seu palpite: "))
  if numero_palpite == numero_sorteado:
    print("Você acertou!")
    break
  else:
    if numero_sorteado > numero_palpite:
      print(f"Você errou! O número é maior que {numero_palpite}")
    else:
      print(f"Você errou! o número é menor que {numero_palpite}")
