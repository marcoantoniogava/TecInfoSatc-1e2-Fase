const int pin_B = 2;
const int pin_B2 = 3;
const int pin_B3 = 4;
const int pin_L1 = 8;
const int pin_L2 = 9;
const int pin_L3 = 10;
//Declarando os pinos
void setup() {
pinMode(pin_B, INPUT);
pinMode(pin_B2, INPUT);
pinMode(pin_B3, INPUT);
pinMode(pin_L1, OUTPUT);
pinMode(pin_L2, OUTPUT);
pinMode(pin_L3, OUTPUT);
//Declarando entradas e saídas
}

void loop() {
bool B = digitalRead(pin_B);
bool B2 = digitalRead(pin_B2);
bool B3 = digitalRead(pin_B3);
//Declarando botões como bool, 1 ou 0, (verdadeiro ou falso)
if (B == 1){ //Se botão1 ligado, ligar Led1. Ao contrário: (else)
  digitalWrite(pin_L1, HIGH);
}
else{
  digitalWrite(pin_L1, LOW);
}
if (B2 == 1){ //Se botão2 ligado, ligar Led2. Ao contrário: (else)
  digitalWrite(pin_L2, HIGH);
}
else{
  digitalWrite(pin_L2, LOW);
}
if (B3 == 1){ //Se botão3 ligado, ligar Led3. Ao contrário: (else)
  digitalWrite(pin_L3, HIGH);
}
else{
    digitalWrite(pin_L3, LOW);
}
}
// Variáveis: L1 = Led 1 / L2 = Led 2 / L3 = Led3 / B = Botão1 / B2 = Botão2 / B3 = Botão3