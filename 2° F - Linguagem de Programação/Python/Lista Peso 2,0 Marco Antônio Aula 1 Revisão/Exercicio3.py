quant = int(input('Quantos alunos deseja conferir: '))
for cont in range(quant):
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    if idade >= 0 and idade <= 2:
        print('O aluno',nome,'se encontra no nível escolar: Berçário')
    if idade >= 3 and idade <= 6:
        print('O aluno',nome,'se encontra no nível escolar: Educação Infantil')
    if idade >= 7 and idade <= 10:
        print('O aluno',nome,'se encontra no nível escolar: Fundamental Nível I')
    if idade >= 11 and idade <= 15:
        print('O aluno',nome,'se encontra no nível escolar: Fundamental Nível II')
    if idade >= 16 and idade <= 18:
        print('O aluno',nome,'se encontra no nível escolar: Ensino Médio')
    else:
        print('Aluno não está entre as idades possíveis.')
