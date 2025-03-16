n = int(input('Digite quantas pessoas deseja consultar: '))
for cont in range(n):
    nome = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa: '))
    altura = float(input('Digite a altura da pessoa: '))
    IMC = peso / (altura * altura)
    if IMC < 18.5:
        print('Condição de ',nome,'é abaixo do peso.')
    if IMC >= 18.5 and IMC < 25:
        print('Condição de ',nome,'é peso normal.')
    if IMC >= 25 and IMC < 30:
        print('Condição de ',nome,'é acima do peso.')
    if IMC > 30:
        print('Condição de ',nome,'é obeso.')
