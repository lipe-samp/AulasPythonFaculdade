
# Lista de exercícos 3 ****************************************************************************************************************8

#######################################################################################################
# Exercício 1 : Escreva um no qual leia dois valores numéricos e imprima o maior deles. Caso ambos os #
# números forem iguais, imprima na tela “números iguais”.                                             #
#######################################################################################################

'''
print("Saiba qual número é maior.")
exercicio1_num1 = input("Digite o primeiro número: ")
exercicio1_num2 = input("Digite o segundo número: ")

try:
    exercicio1_num1 = (int(exercicio1_num1))
    exercicio1_num2 = (int(exercicio1_num2))
    if exercicio1_num1 > exercicio1_num2:
        print(f"O primeiro número '{exercicio1_num1}' é maior que o segundo número '{exercicio1_num2}'")
    elif exercicio1_num1 < exercicio1_num2:
        print(f"O segundo número '{exercicio1_num2} é maior que o primeiro número '{exercicio1_num1}'")
    else:
        print("Ambos números são iguais.")

except:
    print("Digite somente numeros")
'''

################################################################################################################
# Exercício 2: Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h,  #
# exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa, cobrando R$        #
# 5,00 por km acima de 80 km/h.                                                                                #
################################################################################################################


##############################################################################################
# Exercício 3: Escreva um programa que leia três números e que imprima o maior e o menor.    #
##############################################################################################

'''
print("Entre com 3 números diferentes: ")
exercicio3_num1 = input("Número 1: ")
exercicio3_num2 = input("Número 2: ")
exercicio3_num3 = input("Número 3: ")


try:
    exercicio3_num1 = int(exercicio3_num1)
    exercicio3_num2 = int(exercicio3_num2)
    exercicio3_num3 = int(exercicio3_num3)
    
    if exercicio3_num1 > exercicio3_num2 and exercicio3_num1 > exercicio3_num3:
        if exercicio3_num2 > exercicio3_num3:
            print(f"Ordem do maior para o menor: {exercicio3_num1}, {exercicio3_num2} e {exercicio3_num3}.")
        else:
            print(f"Ordem do maior para o menor: {exercicio3_num1}, {exercicio3_num3} e {exercicio3_num2}.")
    elif exercicio3_num2 > exercicio3_num1 and exercicio3_num2 > exercicio3_num3:
        if exercicio3_num1 > exercicio3_num3:
            print(f"Ordem do maior para o menor: {exercicio3_num2}, {exercicio3_num1} e {exercicio3_num3}.")
        else:
            print(f"Ordem do maior para o menor: {exercicio3_num2}, {exercicio3_num3} e {exercicio3_num1}.")
    elif exercicio3_num3 > exercicio3_num1 and exercicio3_num3 > exercicio3_num2:
        if exercicio3_num1 > exercicio3_num2:
            print(f"Ordem do maior para o menor: {exercicio3_num3}, {exercicio3_num1} e {exercicio3_num2}.")
        else:
            print(f"Ordem do maior para o menor: {exercicio3_num3}, {exercicio3_num2} e {exercicio3_num1}.")
    else:
        print("Todos iguais")
except:
    print("Digite somente números.")
'''

#######################################################################################################################
# Exercício 4 – Escreve um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários #
# superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.                           #
#######################################################################################################################            

'''
exercicio4_salario_atual = float(input("Digite seu salário atual: "))
exercicio4_salario_novo = None

if exercicio4_salario_atual > 1250:
    exercicio4_salario_novo = (exercicio4_salario_atual / 100) * 10
    print(f"Com o aumento de 10% seu novo salário é R${exercicio4_salario_atual +exercicio4_salario_novo:.2f}")
else:
    exercicio4_salario_novo = (exercicio4_salario_atual / 100) * 15
    print(f"Com o aumento de 15% seu novo salário é R${exercicio4_salario_atual + exercicio4_salario_novo:.2f}")
'''

########################################################################################################################
# Exercício 5: Execute o programa no qual o usuário entre com a idade do carro e caso o valor seja menor ou igual a 3  #
# anos imprima “Seu carro é novo”, caso contrario “Seu carro é velho”.                                                 #
########################################################################################################################

####################################################################################################################
# Exercício 6 – Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o   #
# preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.       #
####################################################################################################################

'''
exercicio6_distancia = float(input("Qual a distância você pretente percorrer: "))
exercicio6_passagem = None
exercicio6_preco_passagem = None

if exercicio6_distancia <= 200:
    exercicio6_passagem = 0.50
    exercicio6_preco_passagem = exercicio6_distancia * exercicio6_passagem
    print(f"Com a distância de {exercicio6_distancia:.2f} KM, você pagara R${exercicio6_preco_passagem:.2f}, pois o custo por KM é R${exercicio6_passagem:.2f}.")
else:
    exercicio6_passagem = 0.45
    exercicio6_preco_passagem = exercicio6_distancia * exercicio6_passagem
    print(f"Com a distância de {exercicio6_distancia:.2f} KM, você pagara R${exercicio6_preco_passagem:.2f}, pois o custo por KM é R${exercicio6_passagem:.2f}.")
'''

#################################################################################################################
# Exercício 7 – Escreva um programa que calcular a categoria de um produto e determine o preço pela tabela:     #
# Categoria 1 valor de R$ 10,00; Categoria 2 valor de R$ 15,00; Categoria 3 valor de R$ 19,00;                  #
# Categoria 4 valor de R$ 23,00 e Categoria 5 valor de R$ 27,00.                                                #
#################################################################################################################

###############################################################################################################################
# Exercício 8 – Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder  #
# calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.                #
###############################################################################################################################

'''
print("--- Calculadora ---")
print("Digite 1 para somar")
print("Digite 2 para subtrair")
print("Digite 3 para multiplicar")
print("Digite 4 para dividir")

exercicio8_operacao = int(input("Qual operação deseja? "))
exercicio8_numero1 = int(input("Digite o número 1: "))
exercicio8_numero2 = int(input("Digite o número 2: "))
exercicio8_resultado = None

if exercicio8_operacao == 1:
    exercicio8_resultado = exercicio8_numero1 + exercicio8_numero2
    print("Somar")
    print(f"{exercicio8_numero1} + {exercicio8_numero2} = {exercicio8_resultado}")
elif exercicio8_operacao == 2:
    exercicio8_resultado = exercicio8_numero1 - exercicio8_numero2
    print("Subtrair")
    print(f"{exercicio8_numero1} - {exercicio8_numero2} = {exercicio8_resultado}")
elif exercicio8_operacao == 3:
    exercicio8_resultado = exercicio8_numero1 * exercicio8_numero2
    print("Multiplicar")
    print(f"{exercicio8_numero1} x {exercicio8_numero2} = {exercicio8_resultado}")
elif exercicio8_operacao == 4 and exercicio8_numero1 == 0 or exercicio8_numero2 == 0:
    print("Não é possível divisão com número 0")
elif exercicio8_operacao == 4:
    exercicio8_resultado = exercicio8_numero1 / exercicio8_numero2
    print("Dividir")
    print(f"{exercicio8_numero1} / {exercicio8_numero2} = {exercicio8_resultado}")
else:
    print("Digite somente entre 1 a 4")
'''



# Falta 9 e 10

# Lista de exercícos 4 ****************************************************************************************************************



# Exercicio 7 Escreva um programa que exiba a tabuada do número digitado, onde o usuário pode escolher o inicio e o fim da tabuada

'''
qualTabuada = int(input("Digite a tabuada que deseja ver: "))
inicioTabuada = int(input(f"Onde quer começar na tabuada do {qualTabuada}? "))
fimTabuada = int(input(f"Onde quer finalizar na tabuada do {qualTabuada}? "))

for i in range (inicioTabuada, fimTabuada +1):
    print(f"{qualTabuada} x {i} = {i * qualTabuada}")

# Exercício 14
'''

