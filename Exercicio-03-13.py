# Escreva um programa que imprima a tabuada de um número selecionado e que o usuário possa escolher o início e o final da sequência

'''

tabuada_inicio = int(input("Digite o inicio da tabuada: "))
tabuada_fim = int(input("Digite o fim da tabuada: "))
numero_intervalo_inicio = int(input("Onde começa o início do intervalo da tabuada: "))
numero_intervalo_fim = int(input("Onde começa o início do intervalo da tabuada: "))
numero_intervalo_inicio_fixo = numero_intervalo_inicio


while tabuada_inicio <= tabuada_fim:
    numero_intervalo_inicio_fixo
    while numero_intervalo_inicio_fixo <= numero_intervalo_fim:
        print(f"{tabuada_inicio} x {numero_intervalo_inicio_fixo} = {tabuada_inicio * numero_intervalo_inicio_fixo} ")
        numero_intervalo_inicio_fixo = numero_intervalo_inicio_fixo + 1
    tabuada_inicio = tabuada_inicio + 1 

'''


###########################################################################################################

# Escreva um programa que pergunte qual o depósito inicial de uma aplicação, a taxa de juros mensal e imprima o valor existente, mês a mês,
# para os primeiros 24 meses e o valor total ganho com juros.

'''

deposito_inicial = float(input("Digite o depósito inicial: "))
juros = int(input("Qual a taxa de juros: "))

meses = int(input("Digite a quantidade de meses: "))

for i in range(meses):
    i = i + 1
    deposito_inicial = deposito_inicial + (deposito_inicial * (juros / 100))
    print(f"{deposito_inicial:.2f}")

'''

##########################################################################################################

# Escreva um programa que imprime uma contagem regressiva iniciando em 10, para o lançamento de um foguete. Ao final imprima Fogo

'''
import time

timer = 10
fim_timer = 1

while timer >= fim_timer:
    print(f"O foguete se parte em: {timer}")
    time.sleep(1)
    timer = timer - 1

print("Falha no lançamento")

'''

################################################

# Verificar se o número é primo

'''
numero_primo = int(input("Digite um número para saber se é primo: "))
if numero_primo <= 1:
    print("Número não é primo")
else:
    for i in range(2, int(numero_primo ** 0.5) + 1):
        if numero_primo % i == 0:
            print("Número não é primo")
            break
    else:
        print("O número é primo")
'''

##############################################

# Crie um programa qur receba uma string e conta a quantidade de vogais (maiusculas e minusculas) que ela possui.

vogais = "aeiouAEIOU"
quantidade = 0
pergunta = input("Digite para saber se é volgal ou consoante: ")

for i in pergunta:
        if i in vogais:
            quantidade = quantidade + 1
print(f"O número de vogais é: {quantidade}")

