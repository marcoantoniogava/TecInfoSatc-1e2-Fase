listaTarefas = []
while True:
    print('****************')
    print('Menu de opções:') 
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Exibir')
    print('4 - Buscar')
    print('5 - Sair')
    print('****************')
    opcao = int(input('Escolha entre as opções acima: ')) 
    if opcao == 1:
        tarefa = input('Digite a tarefa desejada: ')
        listaTarefas.append(tarefa)
        print('Lista de tarefas:')
        print(listaTarefas)
    if opcao == 2:
        remover = input('Digite a tarefa desejada para remover: ')
        listaTarefas.remove(remover) 
        print('Lista de tarefas:')
        print(listaTarefas)
    if opcao == 3:
        print('Lista de tarefas:')
        print(listaTarefas)
    if opcao == 4:
        buscar = input('Digite a tarefa que deseja procurar: ')
        if buscar in listaTarefas:
            print('A tarefa está na lista.')
        else:
            print('A tarefa não está na lista.')
    if opcao == 5:
        print('Fim do programa!')
        break
