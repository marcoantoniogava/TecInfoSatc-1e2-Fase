# print((lambda x : x**2) (8))

# def quadrado(x):
#    return x**2

# quadrado(8)

# quadrado_lambda = lambda x : x **2
# print(quadrado_lambda(8))

# print((lambda x,y : x**y) (5,3))

# ##############################

# lista = [
#    lambda x : x*2,
#    lambda x : x**2,
#    lambda x : x**3
# ]

# valor = int(input('Digite um valor: '))
# for i in lista:
#    print(i(valor))

# nome_idade = lambda x,y : print(f'{x}, possui {y} anos')

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))

# nome_idade(nome, idade)

# (lambda x, y : print(f'{x}, possui {y} anos')) ((input('Digite seu nome: ')), (int(input('Digite sua idade: '))))

# ############## função filter() #################

# numeros = [4,5,8,9,10]

# numeros_pares = list(filter(lambda x : x % 2 == 0, numeros))
# print(numeros_pares)

# nomes = ['mariane', 'sabrina', 'alice', 'pedro']

# nomes_filter = list(filter(lambda x : 'a' in x, nomes))
# print(nomes_filter)

############### função map() #################

# numeros = [12,5,7,9,10,24,64]

# numeros_ao_quadrado = list(map(lambda x : x**2, numeros))
# print(numeros_ao_quadrado)

# nomes = ['mariane', 'sabrina', 'alice', 'pedro']

# nomes_maiusculo = list(map(lambda x: x.upper(), nomes))
# print(nomes_maiusculo)

# nomes_len = list(map(lambda x: len(x), nomes))
# print(nomes_len)


################ função reduce() ################

from functools import reduce

# numeros = [5,7,12,9,1,22,13]

# soma_numeros = reduce(lambda x,y: x+y, numeros)
# print(soma_numeros)

# dobro_numeros = reduce(lambda x,y: x*y, numeros)
# print(dobro_numeros)

# numeros = [5,7,12,9,1]

# numeros_maximo = reduce(lambda x,y: x if x>y else y, numeros)
# print(numeros_maximo)

# numeros_minimo = reduce(lambda x,y: x if x<y else y, numeros)
# print(numeros_minimo)
