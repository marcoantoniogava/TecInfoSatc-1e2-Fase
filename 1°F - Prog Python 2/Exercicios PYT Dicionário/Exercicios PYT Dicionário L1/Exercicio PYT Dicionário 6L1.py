dic = {}

for i in range(5):
    produto = input('Digite qual produto deseja adicionar: ')
    preco = float(input('Digite o preço desse produto: '))
    dic[produto] = preco
print(dic)
