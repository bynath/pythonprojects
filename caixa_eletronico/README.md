# Caixa Eletrônico
Projeto desenvolvido durante meus estudos de **Python** para praticar funções, estruturas de repetição, validação de dados, manipulação de listas e implementação de regras de negócio.
O programa simula um **caixa eletrônico**, permitindo consultar o saldo, realizar depósitos e efetuar saques, incluindo a distribuição das cédulas disponíveis.

## Sobre o projeto
O sistema inicia com um saldo de **R$ 1.000,00** e apresenta um menu com as principais operações de um caixa eletrônico.

O usuário pode:
- Consultar o saldo;
- Realizar depósitos;
- Realizar saques;
- Encerrar o sistema.

## Funcionalidades

### Consultar saldo
Exibe o saldo atual da conta, formatado em reais.

### Depositar
Permite informar um valor para depósito.

O programa valida se:
- O valor informado é numérico;
- O valor é maior que zero.

Após o depósito, o saldo é atualizado.

### Sacar
Permite informar o valor desejado para saque.

Antes de realizar a operação, o programa verifica:
- Se o valor informado é numérico;
- Se o valor é maior que zero;
- Se existe saldo suficiente;
- Se o valor pode ser formado pelas cédulas disponíveis.

Após um saque válido, o saldo é atualizado e o programa informa a quantidade de cada cédula utilizada.

### Encerrar sistema
Finaliza a execução do programa.
