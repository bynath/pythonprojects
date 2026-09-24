def calcular_inss(salario_bruto: float) -> float:
  """Calcula a contribuição do INSS (regime CLT, progressivo) sobre o salário bruto.

  Aplica as alíquotas progressivas por faixa salarial, com dedução
  do desconto das faixas anteriores, e arredonda o resultado para
  2 casas decimais. Valores acima do teto são descontados no valor
  máximo da última faixa (14%).

  Args:
    salario_bruto: Salário bruto mensal em reais (R$). Valores menores
      ou iguais a zero retornam 0.

  Returns:
    float: Valor da contribuição do INSS em reais (R$), arredondado
      para 2 casas decimais.
  """
  if salario_bruto <= 0:
    return 0
  if salario_bruto <= 1621:
    return round(salario_bruto*0.075, 2)
  if salario_bruto <= 2902.84:
    return round(salario_bruto*0.09 - 24.32, 2)
  if salario_bruto <= 4354.27:
    return round(salario_bruto*0.12 - 111.40, 2)
  return round(salario_bruto*0.14 - 198.49, 2)

def calcular_imposto_de_renda(salario_bruto: float) -> float:
    """Calcula o Imposto de Renda Retido na Fonte (IRRF) sobre o salário bruto.

    Aplica as alíquotas progressivas por faixa salarial, considerando o salário
    base de cálculo após a dedução do INSS, e arredonda o resultado para
    2 casas decimais.

    Args:
      salario_bruto: Salário bruto mensal em reais (R$).

    Returns:
      float: Valor do Imposto de Renda em reais (R$), arredondado
        para 2 casas decimais.
    """
    inss = calcular_inss(salario_bruto)
    salario_base = salario_bruto - inss

    if salario_base <= 2428.80:
        return 0.0
    if salario_base <= 2826.65:
        return round(salario_base*0.075 - 182.16, 2)
    if salario_base <= 3751.05:
        return round(salario_base*0.15 - 394.16, 2)
    if salario_base <= 4664.68:
        return round(salario_base*0.225 - 675.49, 2)
    return round(salario_base*0.275 - 908.73, 2)

def calcular_salario_liquido(salario_bruto: float) -> None:
  """Calcula e imprime o salário líquido a partir do salário bruto.

  Esta função calcula o desconto do INSS e do Imposto de Renda (IR)
  com base no salário bruto fornecido, e então determina o salário líquido.
  Os resultados (salário bruto, desconto INSS, desconto IR e salário líquido)
  são impressos no console.

  Args:
    salario_bruto: Salário bruto mensal em reais (R$).
  """
  inss = calcular_inss(salario_bruto)
  ir = calcular_imposto_de_renda(salario_bruto)
  salario_liquido = round(salario_bruto - inss - ir, 2)
  
  print(f'Salário bruto: {salario_bruto}')
  print(f'Desconto INSS: {inss}')
  print(f'Desconto imposto de renda: {ir}')
  print(f'Salário líquido: {salario_liquido}')
