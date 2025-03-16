nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
setor = input("Digite setor: V - Vendas   C - Compras   P - Produção ")
if setor == "V":
    novosalario = salario + (salario * 0.10)
    print("Novo Salário = ",novosalario)
if setor == "C":
    novosalario = salario + (salario * 0.08)
    print("Novo Salário = ",novosalario)
if setor == "P":
    novosalario = salario + (salario * 0.15)
    print("Novo Salário = ",novosalario)
    
