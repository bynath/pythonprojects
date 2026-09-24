#Perguntar o Nome do Usuário
nome = input("Qual o seu nome? ")

#Definir quando repetir o bloco
continuar = True

#Iniciar estrutura de repetição
while continuar:

  #Solicitar a operação para o usuário
  operacao = input(f"Olá, {nome}! Qual operação deseja realizar? (Digite apenas: + - * /) ")

  #Verificar se a operação está dentro dos parâmetros permitidos
  if operacao not in ["+","-","*","/"]:
    print("Operação Inválida, tente novamente!")

  #Solicitar os números para a execução da operação
  else:
    numero1 = float(input("informe o primeiro número: "))
    numero2 = float(input("informe o segundo número: "))

    #Verificar qual a operação solicitada pelo usuário e realizar o calculo esperado
    if operacao == "+":
      resultado = numero1 + numero2

    elif operacao == "-":
      resultado = numero1 - numero2

    elif operacao == "*":
      resultado = numero1 * numero2

    elif operacao == "/":
      resultado = numero1 / numero2

    #Exibir o resultado da operação solicitada
    print(f"{nome}, o resultado da sua operação é: {resultado}")

    #Verificar se o usuário deseja realizar outra operação
    verificacao = True

    while verificacao:
      resposta = input("Você deseja realizar outra operação? (sim/nao) ")
      if resposta == "nao":
        continuar = False
        verificacao = False

      elif resposta == "sim":
        verificacao = False
