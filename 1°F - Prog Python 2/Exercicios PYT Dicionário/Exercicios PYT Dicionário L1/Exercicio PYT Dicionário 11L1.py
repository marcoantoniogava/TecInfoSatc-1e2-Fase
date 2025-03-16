atletas = { 'Cristiano Ronaldo' : 'Futebol', 'LeBron James' : 'Basquete',
                    'Lionel Messi' : 'Futebol', 'Neymar' : 'Futebol',
                    'Conor McGregor' : 'MMA', 'Roger Federer' : 'Tênis',
                     'Rafael Nadal' : 'Tênis',  'Stephen Curry' : 'Basquete',
                     'Tiger Woods' : 'Golfe',  'Kevin Durant' : 'Basquete',
                      'Lewis Hamilton' : 'Fórmula 1', 'Sun Yang' : 'Natação' }
novo = input('Digite o novo atleta: ')
func = input('Digite a função dele: ')
atletas[novo] = func
if "Roger Federer" in atletas:
    print("O atleta está cadastrado.")
else:
    print("O atleta não está cadastrado.")
del atletas['Tiger Woods']
print(atletas)
