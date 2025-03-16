dic = {}

tamanho = int(input('Digite quantos elementos deseja cadastrar: '))
for i in range(tamanho):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    dic[nome] = idade
print(dic)
