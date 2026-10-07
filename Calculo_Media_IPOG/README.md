# Cálculo de Notas IPOG
Projeto desenvolvido durante meus estudos de **Python** para praticar funções, validação de dados, estruturas de repetição, cálculos com médias ponderadas e organização de um programa por meio de funções.
O programa permite calcular a **nota necessária na Avaliação Formal (AFI)** para atingir a média de aprovação ou verificar a **nota final** do aluno.

## Sobre o projeto
O sistema utiliza a seguinte fórmula para calcular a nota final:
**Nota final = (AFI × 0,6) + (API × 0,4)**

Onde:
- **AFI** = Avaliação Formal
- **API** = Avaliações Processuais
- **AFI** possui peso de **60%**
- **API** possui peso de **40%**
- **Média mínima para aprovação:** 6,0

As quatro notas das Avaliações Processuais (API) são informadas pelo usuário e utilizadas para calcular a média das atividades.

## Funcionalidades
O programa possui um menu com três opções:

1. **Verificar Nota Necessária**
   - Solicita as quatro notas das APIs.
   - Calcula a média das APIs.
   - Calcula quantos pontos o aluno já possui na média final.
   - Informa quantos pontos ainda faltam para atingir a média 6,0.
   - Calcula a nota mínima necessária na AFI para aprovação.

2. **Verificar Nota Final**
   - Solicita as quatro notas das APIs.
   - Calcula a média das APIs.
   - Solicita a nota da AFI.
   - Calcula a nota final.
   - Informa se o aluno está aprovado ou reprovado.

3. **Encerrar**
   - Finaliza a execução do programa.

## Conceitos praticados
Durante o desenvolvimento deste projeto foram praticados:

- Variáveis e constantes
- Tipos de dados
- Listas
- `input()`
- `print()`
- Conversão de tipos com `int()` e `float()`
- Estruturas condicionais `if`, `elif` e `else`
- Estruturas de repetição `while` e `for`
- `try` e `except`
- Tratamento de erros com `ValueError`
- Funções com `def`
- Parâmetros e argumentos
- `return`
- Type hints
- Listas e método `append()`
- `sum()` e `len()`
- Cálculos matemáticos
- Média aritmética
- Média ponderada
- F-strings
- Formatação de números com `:.2f`
- Docstrings
- Reutilização de funções
- Organização do código em funções
- Controle de fluxo por meio de menu

## Estrutura das funções
O programa foi dividido em funções, deixando cada parte do processo responsável por uma tarefa específica.

### `menu()`
Exibe o menu principal e recebe a opção escolhida pelo usuário.

### `coletar_notas_api()`
Solicita as quatro notas das Avaliações Processuais e realiza a validação dos valores informados.

### `calculo_media_api()`
Calcula a média das quatro notas das APIs.

### `coletar_nota_afi()`
Solicita e valida a nota da Avaliação Formal.

### `calculo_pontos_faltantes()`
Calcula quantos pontos ainda faltam para atingir a média de aprovação.

### `calculo_nota_necessaria()`
Calcula a nota mínima que o aluno precisa obter na AFI para atingir a média de aprovação.

### `calculo_nota_final()`
Calcula a nota final utilizando os pesos da AFI e da API.

### `executar()`
Controla o fluxo principal do programa e conecta todas as funções por meio do menu.
