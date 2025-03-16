def somar(a,b):
    soma = a + b
    return soma
def subtracao(a,b):
    sub = a - b
    return sub
def multiplicacao(a,b):
    mult = a * b
    return mult
def divisao(a,b):
    div = a / b
    return div
while True:
    print(f'Menu de opções:\n1: Adição\n2: Subtração\n3: Multiplicação\n4: Divisão\n5: Sair do programa')
    escolha = int(input('Digite um número de 1 a 5, para escolher uma ação: '))
    if escolha == 1:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        resultado = somar(a,b)
        print(f'O resultado da soma entre {a} e {b} é {resultado}')
    if escolha == 2:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        resultado = subtracao(a,b)
        print(f'O resultado da ssubtração entre {a} e {b} é {resultado}')
    if escolha == 3:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        resultado = multiplicacao(a,b)
        print(f'O resultado da multiplicação entre {a} e {b} é {resultado}')
    if escolha == 4:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        resultado = divisao(a,b)
        print(f'O resultado da divisão entre {a} e {b} é {resultado}')
    if escolha == 5:
        print('Programa encerrado!')
        break