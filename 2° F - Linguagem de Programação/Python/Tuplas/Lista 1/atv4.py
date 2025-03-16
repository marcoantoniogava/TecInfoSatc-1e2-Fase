lista = []
pares = []
for i in range(4):
    valores = int(input('Digite o valor que deseja adicionar:'))
    lista.append(valores)
tupla = tuple(lista)
numero = 9
contagem = tupla.count(numero)
print(f'O número {numero} aparece {contagem} vez(es) na tupla')
valor = 3
posicao = tupla.index(valor)
print(f'O valor {valor} aparece na posição {posicao + 1}')
for i in tupla:
    if i % 2 == 0:
        pares.append(i)
print(f'Números pares: {pares}')