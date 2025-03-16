medias = []
total = 0


for cont in range(0,5):
    print(f"digite notas do aluno {contador+1}")
    nota1 = float(input("Insira uma nota1: "))
    nota2 = float(input("Insira uma nota2: "))
    nota3 = float(input("Insira uma nota3: "))
    nota4 = float(input("Insira uma nota4: "))
    media = (nota1 = nota2 + nota3 + nota4)/4
    print("Média do aluno = ",media)
    medias.append(media)

    if (media >= 7):
        total +=1
print("Lista de médias digitados:",medias)
print("Total alunos com média >= 7:",total)
    
