dicSERIES = {} #Criando Dicionário

while True: #Estrutura de Repetição
    print('***********************') #Menu de opcções
    print('Menu de opções:')
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Excluir')
    print('4 - Pesquisar')
    print('5 - Listar Totais')
    print('6 - Sair')
    print('***********************')
    opcao = int(input('Digite a opção desejada: ')) #Pede a opção do menu
    if opcao == 1: #Se 1, cadastra a série, verificando se ela ja está cadastrada
        addSERIE = input('Digite a serie desejada: ')
        if addSERIE in dicSERIES:
            print('A série já foi cadastrada!')
        else:
            addNUM = int(input('Digite o numero em sequência dessa série: '))
            dicSERIES[addSERIE] = addNUM
    if opcao == 2: #Se 2, altera uma posição, Verificando se a série para ocupar essa posição já existe
        novaSERIE = input('Digite a nova série: ')
        if novaSERIE in dicSERIES:
            print('A série já foi cadastrada!')
        else:
            novoNUM = int(input('Digite o numero da nova série: '))
            dicSERIES.update({novaSERIE:novoNUM})
    if opcao == 3: #Se 3, exclui a série do dicionário, verificando se ele é existente
        excluir = (input('Digite a série que deseja excluir: '))
        if excluir in dicSERIES:
            del dicSERIES[excluir]
        else:
            print('Série não cadastrada!')
    if opcao == 4: #Se 4, pesquisa se a série está cadastrada
        verSERIE = input('Digite a série para pesquisar: ')
        if verSERIE in dicSERIES:
            print('A série está cadastrada!')
        else:
            print('A série não está cadastrada!')
    if opcao == 5: #Se 5, exibe o total de séries cadastradas, e elas em ordem alfabética
        print('Total de séries cadastradas: ', len(dicSERIES))
        print('Séries em ordem alfabética: ', sorted(dicSERIES))
    if opcao == 6: #Se 6, encerra o programa
        print('Programa encerrado!')
        break
