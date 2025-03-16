minha_tupla = ()
string = "arroz"
inteiro = 2
decimal = 1.6
lista = []
print(type(minha_tupla))
print(type(string))
print(type(inteiro))
print(type(decimal))
print(type(lista))


#Declarando uma tupla
minha_tupla = 2.5, 'joão', False, 21
minha_tupla2 = 1.6, 'pão', True, 12
print(type(minha_tupla2))

#Acessando valores da tupla

#Acessou valor 1, "1.6"
print(minha_tupla2[0])
#Acessou o valor 4, "12"
print(minha_tupla2[3])

#Fatiamento da tupla

#Acessa o index 0 e 1
print(minha_tupla2[:2])

#Acessa o index -1 e -2 (True, 12)
print(minha_tupla2[-2:])

#Acessa o index do -2 para frente ou seja (1.6 e pão)
print(minha_tupla2[:-2])

#Acessa o comprimenta da tupla
print(len(minha_tupla2))

#Concatena as tuplas
tupla_nova = minha_tupla + minha_tupla2
print(tupla_nova)

#Replicação de uma tupla
tupla_replicada = minha_tupla * 2
print(tupla_replicada)

#Valor mínimo e máximo
minha_tupla_valores = 1.5, 8, 12, 0, 26
valor_min = min(minha_tupla_valores)
valor_max = max(minha_tupla_valores)
print(valor_min)
print(valor_max)


#Percorrendo valores de uma tupla

for i in minha_tupla2:
    print(f'valor: {i}')
#1.6
#pão
#True
#12
              #Range(4)
for i in range(len(minha_tupla)):
    print(i)
#0
#1
#2
#3

#Desempacotamento
tupla_coordenadas = 5, 7

variavel_x, variavel_y = tupla_coordenadas

print(type(tupla_coordenadas))
print(variavel_x)
print(variavel_y)

tupla_idades = 22, 19, 17, 30
idade1, idade2, idade3, idade4 = tupla_idades
print(f'idade 1: {idade1}\nidade 2: {idade2}\nidade 3: {idade3}\nidade 4: {idade4}')


#Função enumerate()
tupla_frutas = 'maça', 'morango', 'uva', 'banana', 'melancia'

for index, i in enumerate(tupla_frutas):
    print(f'A fruta {i} está na posição {index}')
