while True:
  notas = []
  qtde = int(input("Para quantas notas você quer fazer a média? "))

  if qtde < 2:
    print("Informe pelo menos duas notas para calcular a média")

  else:
    for i in range(qtde):
      nota = float(input("Informe a sua nota: "))
      notas.append(nota)

    media = sum(notas) / len(notas)

    print(f"A média de {notas} é {media:.2f}")
    break
