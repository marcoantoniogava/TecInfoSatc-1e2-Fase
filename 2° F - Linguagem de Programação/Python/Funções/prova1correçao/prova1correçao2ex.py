#OK

funcionarios = {}

while True:
    print(f'*************************\nMenu de opções:\nC - Cadastrar\nA - Alterar\nE - Excluir\nP - Pesquisar\nS - Sair\n*************************')
    escolha = input('Digite a opção desejada: ').upper()
    if escolha == 'C': #1
        cadastrarfunc = input('Digite o nome do funcionário: ')
        if cadastrarfunc not in funcionarios:
            cadastrarcargo = input('Digite o cargo do funcionário: ')
            funcionarios[cadastrarfunc] = cadastrarcargo
            print('Funcionário cadastrado!')
        else:
            print('Erro, o funcionário já foi cadastrado!')
    elif escolha == 'A': #2
        escolha2 = int(input('Você deseja alterar um funcionário ou um cargo? digite 1 para funcionário e 2 para cargo: '))
        if escolha2 == 1:
            alterarfunc = input('Digite o funcinário que deseja alterar: ')
            if alterarfunc in funcionarios:
                novofuncionario = input('Digite o novo funcionário: ')
                funcionarios[novofuncionario] = funcionarios.pop(alterarfunc)
                print('Funcionário alterado!')
            else:
                print('Erro, funcionário não está cadastrado!')
        elif escolha2 == 2:
            alterarcargo = input('Digite o cargo que deseja alterar: ')
            if alterarcargo in funcionarios.values():
                novocargo = input('Digite o novo cargo: ')
                funcionarios[alterarfunc] = novocargo
                print('Cargo alterado!')
            else:
                print('Erro, funcionário não está cadastrado!')
    elif escolha == 'E': #3
        excluirfunc = input('Digite o nome do funcionário que deseja excluir: ')
        if excluirfunc in funcionarios:
            del funcionarios[excluirfunc]
            print('Funcionário excluído!')
        else:
            print('Erro, o funcionário não está cadastrado!')
    elif escolha == 'P': #4
        print(f'Lista completa: {funcionarios}\n Lista em ordem alfabética: {sorted(funcionarios)}\nTotal de funcionários cadastrados: {len(funcionarios)}')
    elif escolha == 'S': #5
        print('Programa encerrado!')
        break
