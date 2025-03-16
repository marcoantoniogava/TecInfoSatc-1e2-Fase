#OK

times = 'botafogo', 'fortaleza', 'flamengo', 'palmeiras', 'sao paulo', 'cruzeiro', 'bahia', 'athletico-pr', 'atletico-mg', 'vasco', 'bragantino', 'juventude', 'gremio', 'criciuma', 'internacional', 'vitoria', 'corinthians', 'fluminense', 'cuiaba', 'atletico-go'

print(f'Os 5 primeiros colocados são: {times[0]}, {times[1]}, {times[2]}, {times[3]} e {times[4]}') #1
print(f'Os 4 últimos colocados são: {times[-4]}, {times[-3]}, {times[-2]} e {times[-1]}') #2
print(f'Lista com os times em ordem alfabética: {sorted(times)}') #3
print(f'O time Criciúma está na posição: {times.index("criciuma") + 1}') #4
