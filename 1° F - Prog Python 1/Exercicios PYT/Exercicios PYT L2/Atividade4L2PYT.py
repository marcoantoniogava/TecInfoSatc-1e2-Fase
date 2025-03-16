nome = input("digite seu nome: ")
mediafinal = float(input("Digite sua media final: "))
if mediafinal < 5:
    print("Aluno reprovado")
if mediafinal >= 5 and mediafinal < 7:
    print("Aluno em recuperação")
if mediafinal >= 7:
    print("Aluno Aprovado")
