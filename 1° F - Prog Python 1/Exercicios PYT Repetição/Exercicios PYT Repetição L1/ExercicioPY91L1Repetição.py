nome = input("Digite nome aluno: ")

nota = float(input("Digite nota de 0 a 10: "))

while (nota>10) or (nota<0):
    print("Nota inválida... Digite valor de 0 a 10")
    nota = float(input("digite nota aluno: "))
