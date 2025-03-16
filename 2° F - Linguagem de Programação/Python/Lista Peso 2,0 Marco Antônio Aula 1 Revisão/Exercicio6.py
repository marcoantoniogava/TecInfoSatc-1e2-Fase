n = int(input('Digite quantas pessoas deseja consultar: '))
for cont in range(n):
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    if idade < 16:
        print('A pessoa não pode votar.')
    if idade >= 18 and idade <= 65:
        print('A pessoa é obrigada a votar.')
    if idade >= 16 and idade <= 17:
        print('A pessoa escolha se deseja votar.')
    if idade > 65:
        print('A pessoa escolha se deseja votar.')
