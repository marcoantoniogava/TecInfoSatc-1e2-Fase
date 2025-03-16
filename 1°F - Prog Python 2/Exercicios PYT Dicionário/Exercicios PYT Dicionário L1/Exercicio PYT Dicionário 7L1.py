dic = {}

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = (nota1 + nota2 + nota3) / 3
    print('Média: ',media)
    if media >= 7:
        print('Aluno aprovado!')
    if media < 7 and media >= 5:
        print('Aluno em recuperação!')
    if media < 5:
        print('Aluno reprovado!')
    notas = []
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    dic[nome] = notas
    print(dic)
    break
