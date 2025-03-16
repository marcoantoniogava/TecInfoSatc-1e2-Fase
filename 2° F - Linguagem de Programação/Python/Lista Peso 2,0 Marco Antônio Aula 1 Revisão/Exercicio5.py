n = int(input('Digite quantos produtos deseja consultar: '))
for cont in range(n):
    nome = input('Digite o nome do produto: ')
    quant = int(input('Digite a quantidade do produto: '))
    preço = float(input('Digite o preço do produto: '))
    pagar = quant * preço
    print('***************************************************')
    print('Tipos de pagamento:')
    print('1 - Á vista em dinheiro (Desconto de 10%)')
    print('2 - Á vista no cartão de crédito (Desconto de 5%)')
    print('3 - Em duas vezes (Preço normal sem juros)')
    print('4 - Em três vezes (Preço normal com juros de 5% acréscimo')
    print('***************************************************')
    escolha = int(input('Digite a forma de pagamento: '))
    if escolha == 1:
        dezdesc = pagar * 0.90
        print('O produto',nome,'ficará R$:',dezdesc)
    if escolha == 2:
        cincdesc = pagar * 0.95
        print('O produto',nome,'ficará R$:',cincdesc)
    if escolha == 3:
        duasvzs = pagar * 0.50
        print('O produto',nome,'ficará R$:',duasvzs,'por mês, durante dois meses.')
    if escolha == 4:
        acres1 = (pagar * 1.05) / 3
        print('O produto',nome,'ficará R$:',acres1,'por mês, durante três meses.')
