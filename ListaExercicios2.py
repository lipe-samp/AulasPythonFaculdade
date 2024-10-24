############################################################################################################
#                                                                                                          #
#  1. Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado.    #
#                                                                                                          #
############################################################################################################
print(50 * "*", "Exercício 1", 50 * "*")

print(type(5))     # Classe int
print(type(5.0))   # Classe float
print(type(4.3))   # Classe float
print(type(-2))    # Classe int
print(type(100))   # Classe int
print(type(1.333)) # Classe float

############################################################################################################
#                                                                                                          #
#  2. Complete a tabela a seguir, respondendo True ou False. Considerando a=4, b=10, c=5.0, d=1 e e=5.     #
#                                                                                                          #
############################################################################################################
print(50 * "*", "Exercício 2", 50 * "*")

A_exercicio2 = 4
B_exercicio2 = 10
C_exercicio2 = 5.0
D_exercicio2 = 1
E_exercicio2 = 5

print(A_exercicio2 == C_exercicio2)  # False
print(A_exercicio2 < B_exercicio2)   # True
print(D_exercicio2 > B_exercicio2)   # False
print(C_exercicio2 != E_exercicio2)  # False
print(A_exercicio2 == B_exercicio2)  # False
print(C_exercicio2 < D_exercicio2)   # False
print(B_exercicio2 > A_exercicio2)   # True
print(C_exercicio2 >= E_exercicio2)  # True
print(E_exercicio2 >= C_exercicio2)  # True
print(C_exercicio2 <= C_exercicio2)  # True
print(C_exercicio2 <= E_exercicio2)  # True

#########################################################################
#                                                                       #
#  3. Complete a tabela a seguir utilizando a=True, b=False e c=True.   #
#                                                                       #
#########################################################################
print(50 * "*", "Exercício 3", 50 * "*")

A_exercicio3 = True
B_exercicio3 = False
C_exercicio3 = True

print(A_exercicio3 and A_exercicio3)  # True
print(B_exercicio3 and B_exercicio3)  # False
print(not C_exercicio3)               # False
print(not B_exercicio3)               # True
print(not A_exercicio3)               # False
print(A_exercicio3 and B_exercicio3)  # False
print(B_exercicio3 and C_exercicio3)  # False
print(A_exercicio3 or C_exercicio3)   # True
print(B_exercicio3 or C_exercicio3)   # True
print(C_exercicio3 or A_exercicio3)   # True
print(C_exercicio3 or B_exercicio3)   # True
print(C_exercicio3 or C_exercicio3)   # True
print(B_exercicio3 or B_exercicio3)   # False

###################################################################################################################################################################
#                                                                                                                                                                 #
#  4. Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.    #
#                                                                                                                                                                 #
###################################################################################################################################################################
print(50 * "*", "Exercício 4", 50 * "*")

SALARIO_exercicio4 = 1500.00  # input(float("Digite seu salário: "))
IMPOSTO_exercicio4 = 1200.00

if SALARIO_exercicio4 > IMPOSTO_exercicio4:
    print(f"O salário R${SALARIO_exercicio4:.2f} ultrapassou o valor de {IMPOSTO_exercicio4:.2f}. Deve pagar imposto.")
else:
    print(f"O salário R${SALARIO_exercicio4:.2f} não deve pagar imposto.")

#######################################################################################################################################
#                                                                                                                                     #
#  5. Calcule o resultado da expressão A > B and C or D, utilizando os valores a seguir e após, confirme programando o resultado.     #
#                                                                                                                                     #
#######################################################################################################################################
print(50 * "*", "Exercício 5", 50 * "*")

# a) A = 1, B = 2, C = True, D = False
A_exercicio4 = 1
B_exercicio4 = 2
C_exercicio4 = True
D_exercicio4 = False
print(A_exercicio4 > B_exercicio4 and C_exercicio4 or D_exercicio4) # False

# b) A = 10, B = 3, C = False, D = False 
A_exercicio4 = 10
B_exercicio4 = 3
C_exercicio4 = False
D_exercicio4 = False
print(A_exercicio4 > B_exercicio4 and C_exercicio4 or D_exercicio4) # False

# c) A = 5, B = 1, C = True, D = True  
A_exercicio4 = 10
B_exercicio4 = 3
C_exercicio4 = True
D_exercicio4 = True
print(A_exercicio4 > B_exercicio4 and C_exercicio4 or D_exercicio4) # True

####################################################################################################################################################################
#                                                                                                                                                                  #
#  6. Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7.  # 
#  Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2, materia3.               #                                                                  #
#                                                                                                                                                                  #
####################################################################################################################################################################
print(50 * "*", "Exercício 6", 50 * "*")

materia1_exercicio6 = 2  # int(input("Digite nota de Matemática: "))
materia2_exercicio6 = 7   # int(input("Digite nota de Português: "))
materia3_exercicio6 = 5   # int(input("Digite nota de História: "))
media_exercicio6 = 7
media_conjunta__exercicio6 = (materia1_exercicio6 + materia2_exercicio6 + materia3_exercicio6) / 3

if materia1_exercicio6 >= media_exercicio6 and materia2_exercicio6 >= media_exercicio6 and materia3_exercicio6 >= media_exercicio6:
  print("Todas as matérias atingiram a média.")
elif materia1_exercicio6 >= media_exercicio6 and materia2_exercicio6 >= media_exercicio6 and materia3_exercicio6 <= media_exercicio6:
  print("Reprovado. História não atingiu a média.")
elif materia1_exercicio6 >= media_exercicio6 and materia2_exercicio6 <= media_exercicio6 and materia3_exercicio6 <= media_exercicio6:
  print("Português e História não atingiram a média.")
elif materia1_exercicio6 <= media_exercicio6 and materia2_exercicio6 <= media_exercicio6 and materia3_exercicio6 >= media_exercicio6:
  print("Matemática e Português não atingiram a média.")
elif materia1_exercicio6 <= media_exercicio6 and materia2_exercicio6 >= media_exercicio6 and materia3_exercicio6 <= media_exercicio6:
  print("Matemática e História não atingiram a média.")
elif materia1_exercicio6 >= media_exercicio6 and materia2_exercicio6 <= media_exercicio6 and materia3_exercicio6 >= media_exercicio6:
  print("Português não atingiu a média.")
elif materia1_exercicio6 <= media_exercicio6 and materia2_exercicio6 >= media_exercicio6 and materia3_exercicio6 >= media_exercicio6:
  print("Matemática não atingiu a média.")
else:
  print("Nenhuma matéria atingiu a média.")

# Média de todas juntas:

if media_conjunta__exercicio6 > media_exercicio6:
  print(f"Juntando todas as matérias, sua média é {media_conjunta__exercicio6:.2f}. Aprovado.")
else:
  print(f"Juntando todas as matérias, sua média é {media_conjunta__exercicio6:.2f}. Reprovado.")

#####################################################################################################
#                                                                                                   #
#  7. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.  #
#                                                                                                   #
#####################################################################################################
print(50 * "*", "Exercício 7", 50 * "*")

numero1_exercicio7 = 6734 # int(input("Digite o primeiro número inteiro: "))
numero2_exercicio7 = 5893 # int(input("Digite o segundo número inteiro: "))

print(f"A soma de {numero1_exercicio7} com {numero2_exercicio7} é igual a {numero1_exercicio7 + numero2_exercicio7}")

###########################################################################################################################################
#                                                                                                                                         #
#  8. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros. 1 metro é igual a 100 cm que é igual a 10 mm.   #
#                                                                                                                                         #
###########################################################################################################################################
print(50 * "*", "Exercício 8", 50 * "*")

metro_exercicio8 = 3480.43 # float(input("Digite a quantidade de metros: "))
centimetro_exercicio8 = metro_exercicio8 * 100
milimetro_exercicio8 = centimetro_exercicio8 * 10

print(f"{metro_exercicio8:.2f} metros é igual a {centimetro_exercicio8:.0f} centímetros e {milimetro_exercicio8:.0f} milímetros.")

################################################################################################################################
#                                                                                                                              #
#  9. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.    #
#                                                                                                                              #
################################################################################################################################
print(50 * "*", "Exercício 9", 50 * "*")

dias_exercicio9 = 53      # int(input("Digite total de dias: "))
horas_exercicio9 = 34     # int(input("Digite o total de horas:"))
minutos_exercicio9 = 95   # int(input("Digite o total de minutos:"))
segundos_exercicio9 = 34  # int(input("Digite o total de segundos:"))

total_segundos_exercicio9 = ((((dias_exercicio9  * 24 * 60 ** 2) + horas_exercicio9 * 60 * 60) + minutos_exercicio9 * 60) + segundos_exercicio9)

print(f"{dias_exercicio9} dias, {horas_exercicio9} horas, {minutos_exercicio9} minutos e {segundos_exercicio9} segundos poussui um total de {total_segundos_exercicio9} segundos")

###############################################################################################################################################################################
#                                                                                                                                                                             #
#  10. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.    #
#                                                                                                                                                                             #
###############################################################################################################################################################################
print(50 * "*", "Exercício 10", 50 * "*")

salario_exercicio10 = 1400             # float(input("Digite seu salário: "))
aumento_porcentagem_exercicio10 = 20   # float(input("Quantos por cento será o aumento?: "))
salario_novo_exercicio10 = (float(salario_exercicio10 / 100) * aumento_porcentagem_exercicio10)

print(f"Seu salário atual, R${salario_exercicio10:.2f}, com o aumento de {aumento_porcentagem_exercicio10}%, é igual a R${salario_exercicio10 + salario_novo_exercicio10:.2f}")

########################################################################################################################################
#                                                                                                                                      #
#  11. Faça um programa solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.    #
#                                                                                                                                      #
########################################################################################################################################
print(50 * "*", "Exercício 11", 50 * "*")

mercadoria_exercicio11 = 40.52             # float(input("Qual o valor da mercadoria? "))
desconto_porcentagem_exercercicio11 = 15   # float(input("Qual o valor do desconto? "))
valor_novo_mercadoria_exercicio11 = (float(mercadoria_exercicio11 / 100) * desconto_porcentagem_exercercicio11)

print(f"A mercadoria com valor de R${mercadoria_exercicio11:.2f}, com o desconto de {desconto_porcentagem_exercercicio11:.2f}%, é igual a R${mercadoria_exercicio11 - valor_novo_mercadoria_exercicio11:.2f}")
print(f"O desconto foi de R${valor_novo_mercadoria_exercicio11:.2f}")

#########################################################################################################################################################
#                                                                                                                                                       #
#  12. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.    #
#                                                                                                                                                       #
#########################################################################################################################################################
print(50 * "*", "Exercício 12", 50 * "*")

distancia_percorrida_quilometros_exercicio12 = 200.00 # float(input("Quantos KM de distância? "))
velocidade_km_hora_exercicio12 = 80                # int(input("Quantos KM/H por hora de viagem? "))

horas_dirigidas_exercicio12 = float(distancia_percorrida_quilometros_exercicio12 / velocidade_km_hora_exercicio12)

hora = int(horas_dirigidas_exercicio12)
minutos = (horas_dirigidas_exercicio12-hora)*60

print(f"Você dirigiu aproximadamente {horas_dirigidas_exercicio12} hora(s).")
print(f"Tempo medio percorrido e de: {hora: 2.0f}:{minutos: 0.2f}")

####################################################################################################################################
#                                                                                                                                  #
#  13. Escreva um programa que converta uma temperatura digitada em ºC em ºF. A formula para a conversão é: F = ((9 x C)/5)=32     #
#                                                                                                                                  #
####################################################################################################################################
print(50 * "*", "Exercício 13", 50 * "*")

graus_celcius_exercicio13 = 77.5 # float(input("Quantos graus Celsius você quer converter para Fahrenheit? "))
graus_fahrenheit_exercicio13 = (((9 * graus_celcius_exercicio13) / 5) + 32)

print(f"{graus_celcius_exercicio13} graus Celsius é igual a {graus_fahrenheit_exercicio13} graus Fahrenheit")

########################################################################################################################################
#                                                                                                                                      #
#  14. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade      # 
#  de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.  #
#                                                                                                                                      #
########################################################################################################################################
print(50 * "*", "Exercício 14", 50 * "*")

valor_diaria_exercicio14 = 60        # Valor FIXO
valor_km_rodado_exercicio14 = 0.15   # Valor FIXO

quantos_dias_exercicio14 = 14 * valor_diaria_exercicio14              # int(input("Quantos dias você usou o carro? ") * valor_diaria_exercicio13)
quantos_km_rodado__exercicio14 = 478 * valor_km_rodado_exercicio14    # int(input("Quantos KM foram rodados desde o primeiro dia? "))

valor_a_pagar_exercicio14 = quantos_dias_exercicio14 + quantos_km_rodado__exercicio14

print(f"O valor a pagar, somando os dias com KM rodados é R${valor_a_pagar_exercicio14:.2f}")

######################################################################################################################################################################
#                                                                                                                                                                    #
#  15. Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade  de cigarros fumados por dia e quantos anos ela já fumou.   #
#  Considere que um fumante perde 10 minutos de  vida a cada cigarro e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.                       #
#                                                                                                                                                                    #
######################################################################################################################################################################
print(50 * "*", "Exercício 15", 50 * "*")

cigarro_diario_exercicio15 = 10      # int(input("Quantos cigarros você fuma por dia? "))
cigarro_por_ano_exercico15 = 365.25 * cigarro_diario_exercicio15
quantos_anos_fumou_exercicio16 = 40  # int(input("Quantos anos você fuma? "))
total_cigarros_fumados_exercicio16 = cigarro_por_ano_exercico15 * quantos_anos_fumou_exercicio16

tempo_perdido_dias_exercicio15 = (((total_cigarros_fumados_exercicio16 * 10) / 60) / 24) # Transformando os minutos em dias

print(f"Você fumou um total de {total_cigarros_fumados_exercicio16:.0f} cigarros durante {quantos_anos_fumou_exercicio16} anos, perdendo aproximadamente {tempo_perdido_dias_exercicio15:.2f} dias de vida")


#################################################################################################################################################################################
#                                                                                                                                                                               #
#  Considere um Datacenter com SLA de disponibilidade anual de 99,99% (porcentagem de tempo que o prestador garante acesso e disponibilidade dos recursos) e calcule o tempo    #
#  (em minutos) que o serviço pode ficar indisponível. Para isso, crie um código em Python que, dado o SLA do datacenter (em porcentagem) e assumindo que um ano possui 365,25  # 
#  dias (código deve perguntar a porcentagem de disponibilidade anual ao usuário), calcula em minutos o tempo que o datacenter pode ter de indisponibilidade.                   #
#                                                                                                                                                                               #
#################################################################################################################################################################################

# INCOMPLETO >> NÃO COMPREENDI O EXERCÍCIO EXTRA <<

print(10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)