numero = int(input("Digite um numero inteiro: "))
cont = 0
divisor = 0

while divisor <= numero or cont < 2:
    divisor = divisor + 1
    restodivisao = numero % divisor

    if restodivisao == 0:
        cont = cont + 1

if cont <= 2:
    print("numero digitado: ",numero," é primo")
else:
        print("numero digitado: ",numero," não é primo")
