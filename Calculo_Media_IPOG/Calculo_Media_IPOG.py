# Fórmula de calculo: Nota final = (prova formal * 0,6) + (atividades processuais * 0,4)

MEDIA_APROVACAO = 6.0
PESO_AFI = 0.6
PESO_API = 0.4

def menu() -> int:
  """
  Exibe o menu principal do programa e solicita ao usuário
  a opção desejada.

  Returns:
      int: Opção escolhida pelo usuário.
  """

  while True:
    try:
      print('Calculo de Notas IPOG')
      print('\n0- Encerrar \n1- Verificar Nota Necessária \n2- Verificar Nota Final')
      opcao = int(input('Digite a opção: '))

      if opcao in [0, 1, 2]:
        return opcao

      print('\nOpção inválida! Escolha 0, 1 ou 2.\n')

    except ValueError:
      print('\nOpção Inválida! Digite um número.\n')

def coletar_notas_api() -> list[float]:
  """
  Solicita ao usuário as quatro notas das Avaliações Processuais (API).

  Cada nota é validada para garantir que esteja entre 0 e 10.
  Notas inválidas são solicitadas novamente.

  Returns:
      list: Lista contendo as quatro notas das APIs.
  """

  notas_api = []

  for i in range(1, 5):

    while True:

      try:
        nota = float(input(f'Informe a sua nota da Avaliação Processual (API) {i}: '))

        if nota < 0 or nota > 10:
          print('Nota inválida, digite um número de 0 a 10!')

        else:
          notas_api.append(nota)
          break

      except ValueError:
        print('\nOpção Inválida! Digite um número.\n')

  return notas_api

def calculo_media_api(notas_api: list[float]) -> float:
  """
  Calcula a média das notas das Avaliações Processuais (API).

  Args:
      notas_api (list[float]): Lista contendo as notas das APIs.

  Returns:
      float: Média das notas das APIs.
  """

  media_api = sum(notas_api) / len(notas_api)

  return media_api

def coletar_nota_afi() -> float:
  """
  Solicita ao usuário a nota da Avaliação Formal (AFI).

  A nota é validada para garantir que esteja entre 0 e 10.
  Caso seja inválida, será solicitada novamente.

  Returns:
      float: Nota válida da AFI.
  """
  while True:
    try:
      nota_afi = float(input(f'Informe a sua nota da Avaliação Formal (AFI): '))

      if nota_afi < 0 or nota_afi > 10:
        print('Nota inválida, digite um número de 0 a 10!')
      else:
        break

    except ValueError:
      print('Entrada inválida! Digite um número.')

  return nota_afi

def calculo_pontos_faltantes(media_api: float) -> float:
    """
    Calcula quantos pontos ainda faltam para atingir a média de aprovação.

    Args:
        media_api (float): Média das notas das Avaliações Processuais.

    Returns:
        float: Quantidade de pontos que faltam para atingir a média 6.0.
    """
    falta = MEDIA_APROVACAO - (media_api * PESO_API)

    return falta

def calculo_nota_necessaria(media_api: float) -> float:
  """
  Calcula a nota mínima necessária na Avaliação Formal (AFI)
  para atingir a média de aprovação.

  Args:
      media_api (float): Média das notas das Avaliações Processuais.

  Returns:
      float: Nota mínima necessária na AFI para aprovação.
  """
  falta = calculo_pontos_faltantes(media_api)
  nota_necessaria = falta / PESO_AFI

  return nota_necessaria

def calculo_nota_final(nota_afi: float, media_api: float) -> float:
  """
  Calcula a nota final do aluno considerando os pesos da API e da AFI.

  A média das APIs possui peso de 40% e a nota da AFI possui
  peso de 60%.

  Args:
      nota_afi (float): Nota obtida na Avaliação Formal.
      media_api (float): Média das notas das Avaliações Processuais.

  Returns:
      float: Nota final do aluno.
  """

  nota_final = nota_afi * PESO_AFI + media_api * PESO_API
  return nota_final

def executar() -> None:
  """
  Executa o programa e controla o fluxo do menu principal.

  Permite ao usuário verificar a nota necessária para aprovação,
  calcular a nota final ou encerrar o programa.
  """
  while True:
    opcao = menu()

    if opcao == 1:
      print('\nCALCULO DE NOTA NECESSÁRIA')
      notas_api = coletar_notas_api()
      media_api = calculo_media_api(notas_api)
      nota_necessaria = calculo_nota_necessaria(media_api)
      falta = calculo_pontos_faltantes(media_api)
      print(f'\nVocê já possui {media_api * PESO_API:.2f} pontos de Atividade Processual (API).')
      print(f'\nAinda faltam {falta:.2f} pontos para atingir a média de aprovação ({MEDIA_APROVACAO})')
      print(f'\nVocê precisa tirar pelo menos {nota_necessaria:.2f} na Avaliação Formal (AFI) para ser aprovado!\n')

    elif opcao == 2:
      print('\nCALCULO DE NOTA FINAL')
      notas_api = coletar_notas_api()
      media_api = calculo_media_api(notas_api)
      nota_afi = coletar_nota_afi()
      nota_final = calculo_nota_final(nota_afi, media_api)
      if nota_final >= MEDIA_APROVACAO:
        print(f'\nSua nota final é {nota_final:.2f}, você está APROVADO!\n')
      else:
        print(f'\nSua nota final é {nota_final:.2f}, você está REPROVADO!\n')

    elif opcao == 0:
      print('\n')
      print('Sistema Encerrado!\n')
      break

executar()
