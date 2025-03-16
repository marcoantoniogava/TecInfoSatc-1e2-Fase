def areacirculo(raio):
    resultado = 3.14 * (raio * raio)
    return resultado
def areatriangulo(base,altura):
    resultado2 = (base * altura) / 2
    return resultado2
def arearetangulo(base,altura):
    resultado3 = base * altura
    return resultado3
while True:
    print(f'Menu de opções:\n1: Área do círculo\n2: Área do retângulo\n3: Área do triangulo\n4: Sair do programa')
    escolha = int(input('Digite 1, 2, 3 ou 4 para escolha: '))
    if escolha == 1:
        raio = float(input('Digite o raio do círculo: '))
        resultado = areacirculo(raio)
        print(f'A área do círculo é {resultado}')
    elif escolha == 2:
        base = float(input('Digite a base do triângulo: '))
        altura = float(input('Digite a altura do triângulo: '))
        resultado2 = areatriangulo(base,altura)
        print(f'A área do triângulo é {resultado2}')
    elif escolha == 3:
        base2 = float(input('Digite a base do retângulo: '))
        altura2 = float(input('Digite a altura do retângulo: '))
        resultado3 = arearetangulo(base2,altura2)
        print(f'A área do retângulo é {resultado3}')
    elif escolha == 4:
        print('Programa encerrado!')
        break