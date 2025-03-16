nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
if idade >= 0 and idade <= 3:
    print("categoria: bebê")
if idade >= 4 and idade <= 11:
    print("categoria: criança")
if idade >=12 and idade <= 17:
    print("categoria: Adolescente")
if idade >=18 and idade <= 60:
    print("categoria: Adulto")
if idade >= 61:
    print("categoria: 3a. Idade")
