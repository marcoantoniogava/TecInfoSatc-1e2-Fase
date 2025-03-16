times = {1: 'Criciuma',  2: 'Avai',  3: 'Marcilio Dias', 4: 'Joinville', 
                5: 'Figueirense',  6: 'Chapecoense',  7: 'Brusque', 8: 'Metropolitano',
                9: 'Hercílio Luz', 10: 'Inter de Lages' }
novo = input('Digite o novo time: ')
times[11] = novo
if 'Joinville' in times.values():
    print("O time 'Joinville' está cadastrado.")
else:
    print("O time 'Joinville' não está cadastrado.")
del times[2]
print(times)
