""" 2)	Crie uma tupla preenchida com os 2 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol. Depois mostre:
a.	Apenas os 5 primeiro colocados;
b.	Os últimos 4 colocados da tabela;
c.	Uma lista com os times em ordem alfabética;
d.	Em que posição na tabela está o time de criciuma.
 """
classificados = ("Botafogo", "Fortaleza", "Flamengo","Palmeiras","São Paulo", "Cruzeiro","Bahia","Athletico-PR", "Atlético-MG" ,"Vasco","Bragantino", "Juventude", "Grêmio", "Criciúma", "Internacional","Vitória", "Corinthians", "Fluminense","Cuiabá","Atlético-GO"  )

#a
print(classificados[:5])

#b
print(classificados[:-4])

#c
lista_ordenada = sorted(classificados)
print(lista_ordenada)
	
#d
for i in classificados:
    if i == "Criciúma":
        print(classificados.index(i)+1)







