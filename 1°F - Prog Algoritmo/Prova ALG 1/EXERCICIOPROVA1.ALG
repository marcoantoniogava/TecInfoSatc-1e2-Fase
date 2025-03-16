Algoritmo "exercicioprova1"
//Nome: Marco Antônio
Var
cel: real
temperatura2: caracter
resultado: real
Inicio
escreva ("Digite a temperatura em c: ")
leia (cel)
escreva ("Escolha temperatura K - Kelvin ou Re - Realmur ou F - Fahrenheit: ")
leia (temperatura2)
se (temperatura2 = "F") entao
//Utilizei * para multiplicaçao e + para soma
resultado := (cel * 1.8) + 32
escreva ("Resultado: ", resultado)
fimse
se (temperatura2 = "K") entao
//Utilizei + para soma
resultado := (cel + 273.15)
escreva ("Resultado: ", resultado)
fimse
se (temperatura2 = "Re") entao
//Utilizei * para multiplicaçao
resultado := (cel * 0.8)
escreva ("Resultado: ", resultado)
fimse
Fimalgoritmo