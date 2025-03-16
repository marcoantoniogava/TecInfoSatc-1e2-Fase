# 7)	Faça um programa que receba nome e a média de um aluno.
# a.	Crie um dicionário para guardar a situação do aluno (aprovado, reprovado)
# b.	No final mostre se o aluno foi aprovado ou reprovado.


while True:

    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média desse aluno: "))

    if media < 0 or media > 10 :
        print('dados inválidos')
        continue

    #a
    alunos = {}
    alunos["nome"] = nome
    alunos["media"] = media

    #b
    if(alunos["media"]>=7):
        alunos["situação"] = "aprovado"
    else:
        alunos["situação"] = "reprovado"

    print(f"O aluno {alunos['nome']} está: {alunos['situação']}")

    op = int(input('Se deseja parar o programa digite 0 '))

    if op == 0:
        break
