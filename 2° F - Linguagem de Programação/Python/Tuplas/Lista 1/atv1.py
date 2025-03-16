while True:
    tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco'
    escolha = int(input('Digite o numero que deseja escrito por extenso: '))
    if 0 <= escolha <= 5:
        print(f'O número {escolha} fica em extenso: {tupla[escolha]}')
    else:
        print(f'O número está fora do permitido, tente novamente')