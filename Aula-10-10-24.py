# Dicionário: Armazenar dados em PARES

# exemplo:
# pessoa = {"Nome":"Paulo", "Idade":"61", "Filhos:":["Lucas, Eduardo"]}

# Crie um programa no qual tenha um dicionário com o nome de estoque, contendo o nome de 5 itens, as quantidades e o valor de cada produto

estoque = { 
    #"Item":[Quantidade, Preço]
    "Caneta":[["Quantidade: ", 1372], ["Valor: R$", 1.00]],
    "Lápis":[["Quantidade: ", 3821, "Valor: R$", 0.90]], 
    "Borracha":[["Quantidade: ", 891, "Valor: R$", 1.20]],
    "Apontador":[["Quantidade: ", 925, "Valor: R$", 3.20]],
    "Caderno":[["Quantidade: ", 691, "Valor: R$", 24.90]],
    "Estojo":[["Quantidade: ",852, "Valor: R$", 19.90]],
    "Mochila":[["Quantidade: ",721, "Valor: R$", 140.50]],
    "Corretivo":[["Quantidade: ",924, "Valor: R$", 1,50]]
}

itens = list(estoque.keys())

print("Os produtos da à venda são: ")
for itens in estoque:
    print(itens, ":", estoque[itens])
