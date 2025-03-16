contador = 1
numero = int(input("digite um numero: "))
maior = numero
menor = numero
for contador in range(2,11):
    numero = int(input("digite um numero: "))
    if (numero > maior):
        maior = numero

    if (numero < menor):
        menor = numero
        
print("Maior numero lido: ",maior)
print("Menor numero lido: ",menor)
