nome = input("digite seu nome: ")
print("----"*10)
print("Estado Civil: C - Casado")
print("              S - Solteiro")
print("              V - Viúvo")
print("              D - Divorciado")
print("----"*10)
estado = input("digite seu estado civil: ").upper()
if estado == "C":
    print("Casado")
if estado == "S":
    print("Solteiro")
if estado == "V":
    print("Viúvo")
if estado == "D":
    print("Divorciado")
