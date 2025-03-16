def inicio():
    print("Minha primeira função")

#inicio()

def cores():
    cor1 = input('Digite uma cor: ')
    cor2 = input('Digite outra cor: ')
    print(f'As cores escolhidas foram {cor1} e {cor2}')

#cores()

###########Parâmetros

def nome(name):
    print(f'Seja bem vindo {name}')

#nome('Marco')
#nome('Maria')


def somar(a,b):
    soma1 = a + b
    print(f'O resultado da soma dos valores {a} e {b} é {soma1}')

#somar(6,7)



def somar2(a=0,b=0):
    soma2 = a + b
    print(f'O resultado da soma dos valores {a} e {b} é {soma2}')

#somar2(15)
#somar2(15,55)


def somar3(*args):
    soma3 = sum(args)
    print(f'O resultado da soma foi {soma3}')

#somar3(15,13,16,12,14)
#somar3(34,35,36)
#somar3(54,53,52)


def somar4(*args):
    soma4 = 0
    for i in args:
        soma4 += i
    print(f'O resultado da soma foi {soma4}')

#somar4(12,6,5,7,34,76)

def nomes(*n):
    for i in range(len(n)):
        print(f'Nome: {n[i]}')

#nomes('mariane', 'joaquim', 'carlos')
#print('\n')
#nomes('Thor', 'Homem de ferro', 'Homem aranha', 'Deadpool')


def pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

#pessoa(nome = 'Mariane', idade = '19', cidade = 'Criciuma', altura = '1,57')

def pessoa2(**dados):
    for chave2, valor2 in dados.items():
        print(f'{chave2}: {valor2}')

#pessoa2(nome = 'Mariane', idade = '19', cidade = 'Criciuma', altura = '1,57')


def somar5(a,b):
    soma5 = a + b
    return soma5

#print(somar5(12,6))





def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Numero = int(input('Digite um número: '))
#print(par(Numero))

def par2(n):
    if n % 2 == 0:
        return 'O valor é par'
    else:
        return 'O valor é ímpar'

#Numero2 = int(input('Digite um número: '))
#print(par2(Numero2))

def calculo(n1,n2):
    soma6 = n1+n2
    media = soma6 / 2
    return soma6, media

soma_media = calculo(9,25)
#print(soma_media)

soma, media = soma_media

#print(f'A soma é {soma} e a média é {media}')


def cadastro():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    endereço = input('Digite seu endereço: ')
    return nome, idade, endereço

#pessoa3 = cadastro



#nome2, idade, endereço = cadastro()
#print(f'O nome da pessoa é {nome2}, tem {idade} anos, e reside em {endereço}')

def somar6(a,b):
    global soma6
    soma6 = a+b
    return soma6

#somar6(5,6)
#print(soma6)


def somar7(a,b): return a+b
def multiplicar(a,b): return a*b

#print(somar7(5,6))
#print(multiplicar(5,6))



#DATATIME

from datetime import *

#data = date(2021,7,25)
#print(data)

#data_atual = date.today()
#print(data_atual)

#ano = data_atual.year
#print(ano)

#mes = data_atual.month
#print(mes)

#dia = data_atual.day
#print(dia)

from time import *

#print('Iniciando nosso código...')
#sleep(2)
#print('Bem vindos!')


from math import *

#raiz = sqrt(121)
#print(raiz)

#potencia = pow(3,2)
#print(potencia)

#fatorial = factorial(4)
#print(fatorial)
















