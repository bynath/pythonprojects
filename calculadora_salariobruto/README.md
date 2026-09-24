# Calculadora de Salário Líquido
Projeto desenvolvido durante meus estudos de Python para praticar **funções, reutilização de código, estruturas condicionais e cálculos utilizando diferentes faixas salariais**.

## Sobre o projeto
O programa recebe um **salário bruto mensal** e calcula os principais descontos aplicados ao salário, utilizando funções separadas para cada etapa do cálculo.

O programa calcula:
- Contribuição do **INSS**
- Imposto de Renda **(IRRF)**
- **Salário líquido** após os descontos

## Como funciona
O cálculo é dividido em três funções:

### `calcular_inss()`
Calcula o desconto do INSS com base no salário bruto e nas diferentes faixas de contribuição.

### `calcular_imposto_de_renda()`
Calcula o Imposto de Renda utilizando como base o salário bruto após a dedução do INSS.

### `calcular_salario_liquido()`
Utiliza os valores calculados anteriormente para determinar o salário líquido:

```text
Salário líquido = Salário bruto - INSS - IR
