#OK

tarefas = {}
a = ''
b = ''


def cadastrar(a, b): #1
    a = input('Digite a tarefa que deseja cadastrar: ')
    if a not in tarefas.keys():
        b = input('Digite quando deseja fazer essa tarefa: ')
        tarefas[a] = b
        print('Tarefa cadastrada!')
    else:
        print('Tarefa já cadastrada!')


def alterar(a, b): #2
    a = input('Digite a tarefa que deseja alterar: ')
    if a in tarefas.keys():
        b = input('Digite a nova tarefa: ')
        tarefas[b] = tarefas.pop(a)
        print('Tarefa alterada!')
    else:
        print('Erro, tarefa não cadastrada!')


def excluir(a): #3
    a = input('Digite a tarefa que deseja remover: ')
    if a in tarefas.keys():
        del tarefas[a]
        print('Tarefa excluída!')
    else:
        print('Erro, a tarefa não existe!')


def pesquisar(): #4
    print(f'As tarefas cadastradas são: {tarefas}\nO número de tarefas é: {len(tarefas)}')


while True:
    print(f'*************************\nMenu de opções:\nC - Cadastrar\nA - Alterar\nE - Excluir\nP - Pesquisar\nS - Sair\n*************************')
    escolha = input('Digite qual a opção desejada: ').upper()
    if escolha == 'C': #1
        cadastrar(a, b)
    elif escolha == 'A': #2
        alterar(a, b)
    elif escolha == 'E': #3
        excluir(a)
    elif escolha == 'P': #4
        pesquisar()
    elif escolha == 'S': #5
        print('Programa encerrado')
        break
