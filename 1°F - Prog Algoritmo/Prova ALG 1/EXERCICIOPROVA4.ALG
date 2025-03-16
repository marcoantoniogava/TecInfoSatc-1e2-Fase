Algoritmo "exercicioprova4"
//Nome: Marco Antônio
Var
nome: caracter
peso: real
altura: real
imc: real
Inicio
escreva ("digite seu nome: ")
leia (nome)
escreva ("digite seu peso: ")
leia (peso)
escreva ("digite sua altura: ")
leia (altura)
imc := peso / (altura * altura)
//Utilizei * para multiplicaçao
se (imc <= 18.5) entao
//Utilizei <= para determinar menor ou igual
escreva ("Abaixo do peso")
fimse
se (imc >= 18.5) e (imc <=25) entao
//Utilizei <= para determinar menor ou igual e >= para determinar maior ou igual
escreva ("Peso Normal")
fimse
se (imc >= 25) e (imc <=30) entao
//Utilizei <= para determinar menor ou igual e >= para determinar maior ou igual
escreva ("Acima do Peso")
fimse
se (imc >= 30) entao
//Utilizei >= para determinar maior ou igual
escreva ("Obeso")
fimse
Fimalgoritmo