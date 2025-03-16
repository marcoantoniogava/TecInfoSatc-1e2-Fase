n = int(input('Digite quantos pacientes deseja consultar: '))
for cont in range(n):
    nome = input('Digite o nome do paciente: ')
    idade = int(input('Digite a idade do paciente: '))
    peso = float(input('Digite o peso do paciente: '))
    if idade >= 0 and idade <= 15:
        print('O paciente',nome,'não pode doar sangue devido a sua idade.')
    if idade >= 16 and idade <= 17 and peso > 55:
        print('O paciente',nome,'pode doar sangue com autorização dos pais ou responsáveis.')
    if idade >= 18 and idade <= 69 and peso > 60:
        print('O paciente',nome,'pode doar sangue.')
    if idade > 69:
        print('O paciente',nome,'não pode doar sangue devido a sua idade.')
