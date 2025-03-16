Algoritmo "exercicio10"
var
nome: caracter
horas: inteiro
valorhora: inteiro
salariobruto: real
salarioliquido: real
Inicio
escreva ("digite seu nome: ")
leia (nome)
escreva ("digite suas horas trabalhadas: ")
leia (horas)
escreva ("digite o valor da sua hora: ")
leia (valorhora)
salariobruto := horas * valorhora
escreva ("valor salario bruto R$ : ", salariobruto)
salarioliquido := salariobruto - (salariobruto * 0.02)
escreva ("valor salario liquido R$ : ", salarioliquido)
Fimalgoritmo