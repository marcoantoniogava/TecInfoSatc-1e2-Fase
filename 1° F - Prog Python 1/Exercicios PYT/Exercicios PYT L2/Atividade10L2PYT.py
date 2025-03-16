valor1 = float(input("Digite o Valor1: "))
valor2 = float(input("Digite o Valor2: "))
print("A - Adição")
print("S - Subtração")
print("M - Multiplicação")
print("D - Divisão")
operacao = input("Escolha a operação matematica: ")
if operacao == "A":
    resultado = valor1 + valor2
    print("Resultado de ",valor1," + ",valor2," = ",resultado)
if operacao == "S":
    resultado = valor1 - valor2
    print("Resultado de ",valor1," - ",valor2," = ",resultado)
if operacao == "M":
    resultado = valor1 * valor2
    print("Resultado de ",valor1," * ",valor2," = ",resultado)
if operacao == "D":
    resultado = valor1 / valor2
    print("Resultado de ",valor1," / ",valor2," = ",resultado)
