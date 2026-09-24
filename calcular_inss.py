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
