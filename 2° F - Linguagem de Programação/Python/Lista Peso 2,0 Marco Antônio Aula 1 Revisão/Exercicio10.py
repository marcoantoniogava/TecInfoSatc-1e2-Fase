print('********************************')
print('A - álcool - R$: 4,22/Litro')
print('G - Gasolina - R$: 5,65/Litro')
print('********************************')
escolha = input('Digite a opção escolhida: ').upper()
if escolha == 'A':
    quantalcool = int(input('Digite a quantidade em litros: '))
    if quantalcool <= 20:
        preçoalcool = (quantalcool * 4.22) * 0.97
        print('Quantidade a pagar em R$:',preçoalcool)
    if quantalcool > 20:
        preçoalcool = (quantalcool * 4.22) * 0.95
        print('Quantidade a pagar em R$:',preçoalcool)
if escolha == 'G':
    quantgas = int(input('Digite a quantidade em litros: '))
    if quantgas <= 20:
        preçogas = (quantgas * 5.65) * 0.96
        print('Quantidade a pagar em R$:',preçogas)
    if quantgas > 20:
        preçogas = (quantgas * 5.65) * 0.94
        print('Quantidade a pagar em R$:',preçogas)
