soma = 0
quantidade = 0
maior = 0
menor = 9999
while True:
    numero = int(input("Digite um numero inteiro: "))
    if numero < 0:
        break
    soma = soma + numero
    quantidade = quantidade + 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print("Quantidade: ",quantidade)
print("Soma: ",soma)
media = soma / quantidade
print("Media: ",media)
print("Maior: ",maior)
print("Menor: ",menor)
