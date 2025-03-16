nv = int(input('Digite o número total de votantes: '))
cand1 = 0
cand2 = 0
cand3 = 0
for cont in range(nv):
    voto = int(input('Digite 1 para canditato 1, 2 para candidato 2 ou 3 para candidato 3: '))
    if voto == 1:
        cand1 = (cand1 + 1)
    if voto == 2:
        cand2 = (cand2 + 1)
    if voto == 3:
        cand3 = (cand3 + 1)
print('Tabelas de votos para candidatos 1, 2 e 3, respectivamente.')
print(cand1)
print(cand2)
print(cand3)
