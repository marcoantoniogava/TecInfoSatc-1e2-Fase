Algoritmo "exercicio5L2"
Var
altura, imc : real
sexo: caracter
Inicio
escreva ("digite sexo M - masculino  ou F - feminino: ")
leia (sexo)
escreva ("digite altura: ")
leia (altura)
se (sexo = "M") entao
   imc := 72.7 * altura - 58
   escreva ("imc calculado foi = ", imc)
fimse
se (sexo = "F") entao
    imc := 62.1 * altura - 44.7
     escreva ("imc calculado foi = ", imc)
fimse
Fimalgoritmo