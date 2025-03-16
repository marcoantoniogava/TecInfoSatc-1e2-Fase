# 11)	Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e as adicione em um dicionário. Mostre os nomes de todas as pessoas menores de 18 anos.

pessoas_cadastradas = []

while True:
    pessoa = {}

    op = int(input('Digite sua opção:\n1-cadastrar\n2-sair\n'))
    if op == 1:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite o seu CPF: ")

        pessoa.update({'nome': nome})
        pessoa.update({'idade': idade})
        pessoa.update({'cpf': cpf})
     
        pessoas_cadastradas.append(pessoa)
    elif op == 2:
        break
    else:
        print('Opção inválida')


for i in pessoas_cadastradas:
    if i['idade'] >= 18:
        print(f"A pessoa {i['nome']} tem {i['idade']} anos, logo é maior de idade")