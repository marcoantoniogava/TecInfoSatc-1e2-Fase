estados = {'Acre' : 'Capital Rio Branco',  'Alagoas' :  'Capital Maceió', 
                    'Amazonas': 'Capital Manaus',  'Bahia' : 'Capital Salvador', 
                    'Distrito Federal' : 'Capital Brasília',  'Santa Catarina' : 'Capital Florianópolis', 
                    'Rio Grande do Sul' : 'Capital Porto Alegre',
                    'Paraná' : 'Capital Curitiba', 'São Paulo' : 'Capital São Paulo',
                    'Minas Gerais' : 'Cuiabá', 'Rio de Janeiro' : 'Rio de Janeiro',
                    'Tocantins': 'Capital Palmas'}
print(estados)
novo = input('Digite o novo estado: ')
cap = input('Digite a nova capital: ')
estados[novo] = cap
if "Distrito Federal" in estados:
    print("O estado 'Distrito Federal' está cadastrado.")
else:
    print("O estado 'Distrito Federal' não está cadastrado.")
estados.update({'Minas Gerais': "Belo Horizonte"})
print(estados)
