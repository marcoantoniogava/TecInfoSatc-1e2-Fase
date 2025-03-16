# 10)	Crie um dicionário que será uma agenda e coloque nele os seguintes dados: cpf, nome, idade, telefone. O programa deve ler um número 5 usuários, criar a agenda e imprimir todos os itens do dicionário formatados.

agenda = []


for i in range(5):
    pessoa = {}

    cpf = input("Digite o seu CPF: ")
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    telefone = int(input("Digite o seu telefone: "))
    
    pessoa.update({'cpf': cpf})
    pessoa.update({'nome': nome})
    pessoa.update({'idade': idade})
    pessoa.update({'telefone': telefone})
    
    agenda.append(pessoa)

    
print('='*10, 'AGENDA','='*10)

for i in agenda:
    for chave,valor in i.items():
        print(f'{chave}: {valor}')