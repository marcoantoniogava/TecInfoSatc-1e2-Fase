for contador in range(10):
    numero = int(input("Digite um numero inteiro positivo: "))
    if numero < 0:
        print("numero negativo encerra o programa!")
        break
    if (numero % 2) == 0:
        print("Numero digitado é par")
    else:
       print("Numero digitado é impar")
