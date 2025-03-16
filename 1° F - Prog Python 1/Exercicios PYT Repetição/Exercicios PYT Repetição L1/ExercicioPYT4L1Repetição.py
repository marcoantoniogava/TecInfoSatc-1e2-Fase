fatorial = 1
numero = int(input("digite um numero: "))
for contador in range(1,numero+1):
    fatorial = fatorial * contador

print("Fatorial do numero ",numero," = ",fatorial)
