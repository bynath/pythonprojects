import random

opcoes = ["Pedra", "Papel", "Tesoura"]

def ganhador(jogador, oponente):
    regras = {
        "Pedra": "Tesoura",
        "Tesoura": "Papel",
        "Papel": "Pedra"
    }

    return regras[jogador] == oponente

def jogo():
  while True:
    usuario = input("Escolha sua opção: Pedra, Papel, Tesoura: ").capitalize()
    if usuario in opcoes:
      break

    print('Escolha uma opção válida!')

  computador = random.choice(opcoes)

  if usuario == computador:
    return 'Empate!'

  #Pedra > Tesoura; Tesoura > Papel; Papel > Pedra
  if ganhador(usuario, computador):
    return f'Você escolheu {usuario} e seu oponente escolheu {computador}. Você ganhou!'

  return f'Você escolheu {usuario} e seu oponente escolheu {computador}. Você perdeu!'

print (jogo())
