# 5)	Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos valores. No final, mostre uma listagem de preços, organizando os dados de forma tabular.


tupla = ('arroz', 1.99, 'feijão', 9.90, 'café', 6.75)
print('====== Produtos e Preço =======')

for i in range(0, len(tupla), 2):
    print(f'{tupla[i]}:   R${tupla[i+1]}')

