# 12)	Crie um programa PYTHON para um dicionário, contendo uma lista de informações, para cadastrar os Carros de uma revenda, seguindo a ordem:  
#                Carros = { 1 : [ “fiat”, “palio”, “ano 2022”, “prata”], 
#                                  2 : [ “ford”, “fiesta”, “ano 2023”, “branca”],
#                                  3 : [ “honda”, “fit”, “ano 2024”, “preta”], etc }
# Deve conter um MENU de opções para: 
# 1 – Cadastrar
# 2 – Excluir
# 3 – Pesquisar
# 4 - Sair
# Para as opções de Cadastrar, Excluir e Pesquisar, perguntar antes qual codigo do carro deseja e verificar se já foi cadastrada antes de realizar a operação. Mostrar depois o dicionario atualizado.

# Carros = { 1 : [ 'fiat”, “palio', 'ano 2022', 'prata'], 2 : [ 'ford', 'fiesta', 'ano 2023', 'branca'],3 : ['honda', 'fit', 'ano 2024', 'preta'] }


revenda = {}
count = 0

while True:
    
    op = int(input('Digite sua opção:\n1-Cadastrar\n2-Excluir\n3-Pesquisar\n4-sair\n'))

    if op == 4:
        break
    
    elif op == 1:
        count += 1
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = int(input("Digite o ano do carro: "))
        cor = input("Digite a cor do carro: ")
        carros = [marca,modelo,ano,cor]
        revenda.update({count:carros})
        print(revenda)

    elif op == 2:
        cod = int(input('qual o código do carro que deseja excluir? '))
        print(revenda[cod])
        if cod in revenda.keys():
            del revenda[cod]
            count -= 1
        else:
            print('Esse código não está na nossa frota') 
        print(revenda)

    elif op == 3:
        cod = int(input('qual o código do carro que deseja pesquisar? '))
        if cod in revenda.keys():
            print(revenda[cod])
        else:
            print('Esse código não está na nossa frota') 
    
    else:
        print('Opção inválida')


else:
        print(f'funcionário {verifica_funcionario} não encontrado')