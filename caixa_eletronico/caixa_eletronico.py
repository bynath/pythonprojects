SALDO_INICIAL = 1000.00

def menu() -> int:
  """
  Exibe o menu principal do programa e solicita ao usuário
  a opção desejada.

  Returns:
      int: Opção escolhida pelo usuário.
  """

  while True:
    try:
      print('=== CAIXA ELETRÔNICO ===\n')
      print('0- Encerrar sistema\n1- Consultar Saldo\n2- Depositar\n3- Sacar')
      opcao = int(input('Digite a opção: '))

      if opcao in [0, 1, 2, 3]:
        return opcao

      print('\nOpção inválida! Escolha 0, 1, 2 ou 3.\n')

    except ValueError:
        print('\nOpção Inválida! Digite um número.\n')

def consultar(saldo: float) -> None:
  """
  Exibe o saldo atual da conta.

  Args:
      saldo (float): Saldo atual da conta.
  """
  print('\n=== CONSULTAR ===\n')
  print(f'SALDO ATUAL: R$ {saldo:.2f}\n')

def depositar(saldo: float) -> float:
  """
  Solicita ao usuário o valor do depósito, valida a entrada,
  atualiza o saldo da conta e retorna o novo saldo.

  Args:
      saldo (float): Saldo atual da conta.

  Returns:
      float: Novo saldo da conta após o depósito.
  """
  while True:
    try:
      print('\n=== DEPOSITAR ===\n')
      deposito = float(input('Informe o valor que deseja depositar: '))

      if deposito <= 0:
        print('\nDigite um valor positivo para depositar!\n')
        continue

      saldo += deposito

      print(f'\nDepósito realizado! Seu saldo atual é R$ {saldo:.2f}\n')

      return saldo

    except ValueError:
      print('\nOperação Inválida! Digite um número.\n')

def saque(saldo: float) -> float:
  """
  Solicita ao usuário o valor do saque, valida a entrada,
  atualiza o saldo da conta e retorna o novo saldo.

  Args:
      saldo (float): Saldo atual da conta.

  Returns:
      float: Novo saldo da conta após o saque.
  """
  while True:
    try:
      print('\n=== SACAR ===\n')
      valor_saque = float(input('Informe o valor que deseja sacar: '))

      if valor_saque <= 0:
        print(f'\nSeu saldo atual é R$ {saldo:.2f}')
        print('\nDigite um valor maior que zero.')
        continue

      if valor_saque > saldo:
        print(f'\nSeu saldo atual é R$ {saldo:.2f}')
        print('\nSaldo Insuficiente.')
        continue

      notas = calcular_notas(valor_saque)

      if notas is None:
        print('\nSaque impossível!')
        continue

      saldo -= valor_saque
      print(f'\nSaque de R$ {valor_saque:.2f} realizado! Seu saldo atual é R$ {saldo:.2f}\n')
      print(f'Notas de R$ 100: {notas[0]}')
      print(f'Notas de R$ 50: {notas[1]}')
      print(f'Notas de R$ 20: {notas[2]}')
      print(f'Notas de R$ 10: {notas[3]}\n')
      return saldo

    except ValueError:
      print('\nOperação Inválida! Digite um número.\n')


def calcular_notas(valor_saque: float):
  """
  Verifica se o valor do saque pode ser formado pelas
  notas disponíveis no caixa.

  Args:
      valor_saque (float): Valor que o usuário deseja sacar.

  Returns:
      list: Quantidade de notas de R$100, R$50, R$20 e R$10,
            ou None caso o valor não possa ser formado.
  """
  restante = valor_saque

  notas_100 = int(valor_saque // 100)
  restante = valor_saque % 100

  notas_50 = int(restante // 50)
  restante = restante % 50

  notas_20 = int(restante // 20)
  restante = restante % 20

  notas_10 = int(restante // 10)
  restante = restante % 10

  if restante > 0:
    return None

  return [notas_100, notas_50, notas_20, notas_10]

def executar():
    """
    Executa o caixa eletrônico.
    """
    saldo = SALDO_INICIAL

    while True:
      opcao = menu()

      if opcao == 0:
          print('\nSistema Encerrado!')
          break

      elif opcao == 1:
          consultar(saldo)

      elif opcao == 2:
          saldo = depositar(saldo)

      elif opcao == 3:
          saldo = saque(saldo)
  
executar()
