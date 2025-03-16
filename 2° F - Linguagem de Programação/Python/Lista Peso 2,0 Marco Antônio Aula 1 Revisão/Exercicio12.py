n = int(input('Digite quantos funcionários deseja consultar: '))
for cont in range(n):
    nome = input('Digite o nome do funcionário: ')
    idade = int(input('Digite a idade do funcionário: '))
    valorplano = float(input('Digite o valor do plano: '))
    if idade >= 0 and idade <= 18:
        aumento = (valorplano * 1.05)
        print('O valor a ser pago é de R$:',aumento)
    if idade >= 19 and idade <= 35:
        aumento = (valorplano * 1.10)
        print('O valor a ser pago é de R$:',aumento)
    if idade >= 36 and idade <= 60:
        aumento = (valorplano * 1.15)
        print('O valor a ser pago é de R$:',aumento)
    if idade > 60:
        aumento = (valorplano * 1.20)
        print('O valor a ser pago é de R$:',aumento)
