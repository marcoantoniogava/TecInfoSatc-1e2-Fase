papelaria = {}

for i in range(5):
    prod = input('Digite qual produto deseja adicionar: ')
    preco = float(input('Digite o preço desse produto: '))
    papelaria[prod] = preco
print(papelaria)
