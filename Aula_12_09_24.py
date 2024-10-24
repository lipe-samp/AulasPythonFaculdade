# Exercicio 10 lista 3

##################################################################################################################
# 10 – Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a         #
# quantidade de kWh consumida e o tipo de instalação: R para residencial, I para industrial e C para comércios.  # 
# Calcule o preço a pagar de acordo com a tabela a seguir:                                                       #
#                                                                                                                #
# Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.                                               #
# Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.                                               #
# Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60.                                              #
##################################################################################################################

'''

print("------------------------")
print("Tipos de instalação:") 
print("[R] para Residêncial")
print("[I] para Industrial")
print("[C] para Comércio")
print("------------------------")

tipo_instalacao = input("Tipo de instalação conforme tabela acima: ")

KWh = int(input("Consumo (KHw): "))

if tipo_instalacao == "R" or tipo_instalacao =="r":
    print("Escolheu residêncial")
    if KWh <= 500:
        preco = KWh * 0.40
        print(f"O preço a se pagar é R${preco:.2f}")
    else:
        preco = ((KWh - 500) * 0.65) + 200 # Esse +200 é o custo FIXO em R$ de KWh que eu reduzi em parênteses, que no caso são os -500.
        print(f"O preço a se pagar é R${preco:.2f}")
elif tipo_instalacao == "C" or tipo_instalacao == "c":
    print("Escolheu comércio")
    if KWh <= 1000:
        preco = KWh * 0.55
        print(f"O preço a se pagar é R${preco:.2f}")
    else:
        preco = ((KWh - 1000) * 0.60) + 550 # Esse +550 é o custo FIXO em R$ de KWh que eu reduzi em parênteses, que no caso são os -1000.
        print(f"O preço a se pagar é {preco:.2f}")
elif tipo_instalacao == "I" or tipo_instalacao == "i":
    print("Escolheu industrial")
    if KWh <= 5000:
        preco = KWh * 0.55
        print(f"O preço a se pagar é R${preco:.2f}")
    else:
        preco = ((KWh - 5000) * 0.60) + 2750 # Esse +2750 é o custo FIXO em R$ de KWh que eu reduzi em parênteses, que no caso são os -5000.
        print(f"O preço a se pagar é R${preco:.2f}")
else:
    print("Digite somente a sigla.")


'''

# Exercicio 11 lista 4

############################################################################################################
# 11 – Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança. Exiba os     #
# valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.                #
############################################################################################################

deposito = float(input("Deposito inicial R$: "))
juros = float(input("Taxa mensal (%): "))
prazo = int(input("Meses de aplicação: ")) 

meses = 0
valor = deposito

print(f"Mês {meses}: R${valor:.2f}")

while meses < prazo:
    valor = valor + (valor * juros / 100)
    meses = meses + 1
    print(f"Mês {meses}: R${valor:.2f}")

rendimento = valor - deposito
print(f"Rendeu R${rendimento:.2f} no prazo de {meses}")


