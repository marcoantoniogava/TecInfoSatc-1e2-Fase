dic = {}

for i in range(10):
    amigo = input('Digite qual amigo deseja adicionar: ')
    tel = int(input('Digite o telefone desse amigo: '))
    dic[amigo] = tel
print(dic)
