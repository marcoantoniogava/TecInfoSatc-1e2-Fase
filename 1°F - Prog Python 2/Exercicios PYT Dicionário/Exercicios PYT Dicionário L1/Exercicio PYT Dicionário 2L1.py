dic = {}

for i in range(4):
    nome = input('Digite o nome do funcionario: ')
    codigo = int(input('Digite o indice numerico dele: '))
    dic[nome] = codigo
excluir = input('Digite o funcionario a ser demitido: ')
del dic[excluir]
print(dic)
