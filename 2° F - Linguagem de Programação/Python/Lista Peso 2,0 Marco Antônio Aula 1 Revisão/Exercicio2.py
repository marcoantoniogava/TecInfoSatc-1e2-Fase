while True:
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    print('**************************')
    print('Menu de opções:')
    print('1 - Graus F (Fahrenheit)')
    print('2 - Graus K (Kelvin)')
    print('3 - Graus RE (Réaumur)')
    print('4 - Sair')
    print('**************************')
    escolha = int(input('Escolha a temperatura desejada: '))
    if escolha == 1:
        f = (celsius * 1.8) + 32
        print('Graus em fahrenheit:',f)
    if escolha == 2:
        k = (celsius + 273.15)
        print('Graus em kelvin:',k)
    if escolha == 3:
        r = (celsius * 0.8)
        print('Graus em réaumur:',r)
    if escolha == 4:
        print('Programa encerrado!')
        break
