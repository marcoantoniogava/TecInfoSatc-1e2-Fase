#Criando dicionários

carros = {'marca': 'chevrolet', 'modelo': 'onix', 'ano': 2023}
print(carros)
print(type(carros))

pessoas = {}
print(type(pessoas))

#Acessando dados do dicionário

print(carros['marca'])
print(carros['modelo'])
#print(carros['placa'])

#Acessando valores com "get"

print(carros.get('modelo', 'Chave inexistente'))
print(carros.get('placa', 'Chave inexistente'))

#Acessando todas as chaves do dicionário

print(carros.keys())

#Acessando todos os valores

print(carros.values())

#Acessando as chaves e valores

print(carros.items())

#Adicionando ou alterando o dicionário

#Alterando

carros['ano'] = 2015 
print(carros.items())

#Adicionando

carros['placa'] = 'AQG1H45'
print(carros.items())

#Deletando itens do dicionário

#carros.pop('placa')
#print(carros.items())

del carros['placa']
print(carros.items())

#Verificando se um item esá presente no dicionário

print('placa' in carros)
print('ano' in carros)

#Verificando se o valor de um item no dicionário

print('onix' in carros.values())
print('tracker' in carros.values())

#Iterando sobre um dicionário

for i in carros:
    print(i)

for i in carros.values():
    print(i)

for chave, valor in carros.items():
    print(f'{chave}: {valor}')


filmes = [
    {'name': 'O homem de Ferro', 'genre': 'Ação e Aventura'},
    {'name': 'Meu malvado favorito', 'genre': 'Animação'},
    {'name': 'Se beber não case', 'genre': 'Comédia'}
]
print(filmes)

print(filmes[0]['genre'])
print(filmes[2]['name'])

print(filmes[0].values())
print(filmes[2].keys())
print(filmes[1].items())

for i in filmes:
    print(i)

for i in filmes:
    for chave, valor in i.items():
        print(f'{chave} : {valor}')

#Criando dicionários com inputs

#filmes = {}

#nome = input('Digiteo nome do filme: ')
#genero = input('Digite o genero do filme: ')

#filmes['name'] = nome
#filmes['genre'] = genero

#print(filmes)

#Criando uma lista com dicionários com inputs

locadora = []
filmes = {}

for i in range(3):
    nome = input('Digiteo nome do filme: ')
    genero = input('Digite o genero do filme: ')
    filmes['name'] = nome
    filmes['genre'] = genero
    locadora.append(filmes)
    print(locadora)
