# 8)Crie um dicionário pessoa e coloque nele seus dados: nome, idade, telefone, endereço. Usando o dicionário pessoa criado anteriormente, imprima seu nome.

pessoa = {}

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
telefone = int(input("Digite o seu telefone: "))

pessoa.update({'nome': nome})
pessoa.update({'idade': idade})
pessoa.update({'telefone': telefone})

print(pessoa['nome'])