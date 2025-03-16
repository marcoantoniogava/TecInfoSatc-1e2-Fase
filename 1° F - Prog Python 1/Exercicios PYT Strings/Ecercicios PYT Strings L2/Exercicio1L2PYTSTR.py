nome = input("digite nome: ")
print("---"*10)
print("Cursos: A - Administração")
print("        D - Direito")
print("        C - Contabilidade")
print("        F - Fisioterapia")
print("        O - Odontologia")
print("        M - Medicina")
print("---"*10)
curso = input("digite seu curso: ").upper()
if curso == "A":
    print("curso escolhido foi: Administraçao")
if curso == "D":
    print("curso escolhido foi: Direito")
if curso == "C":
    print("curso escolhido foi: Contabilidade")
if curso == "F":
    print("curso escolhido foi: Fisioterapia")
if curso == "O":
    print("curso escolhido foi: Odontologia")
if curso == "M":
    print("curso escolhido foi: Medicina")
