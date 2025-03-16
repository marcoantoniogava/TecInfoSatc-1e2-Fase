listanumeros = []
while True:
    print('****************')
    print('Menu de opções:') 
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Exibir')
    print('4 - Exibir Pares')
    print('5 - Exibir Ímpares')
    print('6 - Exibir Primos')
    print('7 - Sair')
    print('****************')
    opcao = int(input('Escolha entre as opções acima: ')) 
    if opcao == 1:
        numero = input('Digite o número desejada: ')
        listanumeros.append(numero)
        print('Lista de números:')
        print(listanumeros)
    if opcao == 2:
        remover = input('Digite o número desejada para remover: ')
        listanumeros.remove(remover) 
        print('Lista de números:')
        print(listanumeros)
    if opcao == 3:
        print('Lista de números:')
        print(listanumeros)
    if opcao == 7:
        print('Fim do programa!')
        break
