produtos = {}

for i in range(1,3):
   chave = input(f'Digite o {i}º produto:')
   valor = int(input('Digite o valor do produto acima:'))
   produtos[chave] = valor
   total = sum(produtos.values())   

print(f'O total da compra foi {total} R$')