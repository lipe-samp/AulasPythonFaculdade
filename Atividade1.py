# Utilizei o input para tornar livre o salário e a porcentagem de aumento desejada.

salario_str = input("Digite seu salário: ")
aumento_str = input("Quantos por cento será o aumento?: ")
salario_novo = None

#  TRY / EXCEPT caso fosse digitado letras ao invés de números. Dessa forma o programa alerta para digitar somente números.

try:
  salario = float(salario_str)
  aumento = int(aumento_str)
  salario_novo = (float(salario / 100) * aumento)
  print(f"Seu salário atual, R${salario}, com o aumento de {aumento}%,  é igual a R${salario_novo + salario}")
except:
  print("Por gentileza, digite somente números.")