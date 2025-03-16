def pares(a,b,c):
    a = []
    while True:
        b = int(input('Digite um número para adicionar a lista, ou 190 para sair: '))
        if b == 190:
            print('programa encerrado!')
            break
        else:
            a.append(b)
    print(a)
    c = list(filter(lambda x : x % 2 == 0, a))
    print(c)


pares('a','b','c')