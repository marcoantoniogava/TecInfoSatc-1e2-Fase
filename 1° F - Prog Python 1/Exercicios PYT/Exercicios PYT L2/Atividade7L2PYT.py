nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
if idade >= 0 and idade <= 10:
    print("Categoria Infantil")
if idade >= 11 and idade <= 17:
    print("Categoria Juvenil")
if idade >= 18 and idade <= 30:
    print("Categoria Adulto")
if idade >= 31 and idade <= 60:
    print("Categoria Sênior")
