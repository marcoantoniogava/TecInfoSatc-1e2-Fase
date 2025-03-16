# 9)	Crie um dicionário pessoa e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone, endereço. Imprima todos os itens do dicionário no formato chave: valor

pessoas_cadastradas = []

while True:
    pessoa = {}

    op = int(input('Digite sua opção:\n1-cadastrar\n2-sair\n'))
    if op == 1:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        telefone = int(input("Digite o seu telefone: "))
        endereço = input('Digite o seu endereço')

        pessoa.update({'nome': nome})
        pessoa.update({'idade': idade})
        pessoa.update({'telefone': telefone})
        pessoa.update({'endereço': endereço})

        pessoas_cadastradas.append(pessoa)
    elif op == 2:
        break
    else:
        print('Opção inválida')


for i in pessoas_cadastradas:
    for chave,valor in i.items():
        print(f'{chave}: {valor}')