dic = {}

for i in range(5):
    nome = input('Digite o nome do amigo: ')
    tel = int(input('Digite o telefone dele: '))
    dic[nome] = tel
print(dic)
nome2 = input('Digite o outro nome: ')
tel2 = int(input('Digite o telefone dele: '))
dic[nome2] = tel2
print(dic)
