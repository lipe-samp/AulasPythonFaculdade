###############################################################################################################################
# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). # 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.                      #
###############################################################################################################################

# Precisei pesquisar pois não compreendi a lógica para alcançar esse exercício

numeros_guardados = [] # Aqui vou listar todos os números digitados
    
while True:
    numero = int(input("Digite o número para somar ou digite 0 (zero) para interromper a soma: "))
    
    if numero == 0:
        break
        
    numeros_guardados.append(numero) # Nesse momento estou armazenando os números em >> numeros_guardados = [] <<


quantidade = len(numeros_guardados) # Contar números na variável

# Ao pesquisar no google verifiquei que o len() em uma variável "lista" mostra a quantidade de itens armazenados na lista
# Importante pois esse resultado que permite fazer a média aritmética

soma = sum(numeros_guardados)
media = soma / quantidade

print(f"Você digitou esses números: {numeros_guardados}") # Aparece a lista completa dos números
print(f"Quantidade de números digitados: {quantidade}") # A quantidade de números na lista
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")