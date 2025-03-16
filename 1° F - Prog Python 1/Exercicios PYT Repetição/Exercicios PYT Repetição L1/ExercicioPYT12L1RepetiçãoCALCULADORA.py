while True:
    print("******************************")
    print("Operações da calculadora: ")
    print("1 - Adição                ")
    print("2 - Subtração             ")
    print("3 - Multiplicação         ")
    print("4 - Divisão               ")
    print("5 - Sair do programa      ")
    opcao = int(input("Escolha a opção desejada: "))
    if (opcao == 5):
        print("Fim do programa.....")
        break
    valor1 = int(input("digite o primeiro valor: "))
    valor2 = int(input("digite o segundo valor: "))
    print("******************************")
    if (opcao == 1):
        resultado = valor1 + valor2
        print("Resultado: ",valor1," + ",valor2," = ",resultado)
    if (opcao == 2):
        resultado = valor1 - valor2
        print("Resultado: ",valor1," - ",valor2," = ",resultado)
    if (opcao == 3):
        resultado = valor1 * valor2
        print("Resultado: ",valor1," * ",valor2," = ",resultado)
    if (opcao == 4):
        resultado = valor1 / valor2
        print("Resultado: ",valor1," / ",valor2," = ",resultado)
