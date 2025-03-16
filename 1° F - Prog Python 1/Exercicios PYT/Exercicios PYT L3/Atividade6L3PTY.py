nome = input("digite nome vendedor: " )
salariofixo = float(input("digite salario fixo: "))
totalvendas = float(input("digite total vendas: "))
comissao = totalvendas * 0.15
salariofinal = salariofixo + comissao
print("nome funcionario: ",nome)
print("salario fixo: ",salariofixo)
print("comissao: ",comissao)
print("salario final: ",salariofinal)
