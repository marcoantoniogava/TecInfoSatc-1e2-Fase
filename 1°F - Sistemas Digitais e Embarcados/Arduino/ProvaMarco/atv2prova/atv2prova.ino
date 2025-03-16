const int pin_SEV = 2;
const int pin_SSV = 3;
const int pin_VER = 10;
const int pin_LIB = 9;
const int pin_LOT = 8;
const int pin_BOT = 4;
int estado = 0;
unsigned long tempo_anterior = 0;
//Declarando os pinos, estado e tempo anterior
void setup() {
pinMode(pin_SEV, INPUT);
pinMode(pin_SSV, INPUT);
pinMode(pin_BOT, INPUT);
pinMode(pin_VER, OUTPUT);
pinMode(pin_LIB, OUTPUT);
pinMode(pin_LOT, OUTPUT);
//Declarando entradas e saídas
}

void loop() {
bool BOT = digitalRead(pin_BOT);
bool SEV = digitalRead(pin_SEV);
bool SSV = digitalRead(pin_SSV);
//Declarando botões como bool, 1 ou 0, (verdadeiro ou falso)
if (SEV == 1){ //Se SEV ligado, ligar LOT. Ao contrário: (else)
  digitalWrite(pin_LOT, HIGH);
}
else{
  digitalWrite(pin_LOT, LOW);
}
if (SSV == 1){ //Se SSV ligado, ligar LIB. Contar  Ao contrário: (else)
  digitalWrite(pin_LIB, HIGH);
  estado = 1; // Define estado = 1
  tempo_anterior = millis(); //Conta tempo anterior
}
else{
  digitalWrite(pin_LIB, LOW);
}
unsigned long tempo_atual = millis(); //Define e começa a contar o tempo atual
switch (estado) {
    case 0: //Se estado 0, Tudo desligado
      digitalWrite(pin_LIB, 0);
      digitalWrite(pin_LOT, 0);
      digitalWrite(pin_VER, 0);
      break; case 1 : digitalWrite(pin_VER, 1); // Se estado 1, Ligar VER
      if (tempo_atual - tempo_anterior >= 500) { //Se passou 500ms, estado muda para 2.
        estado = 2;
        tempo_anterior = millis();
      }
      break; case 2 : digitalWrite(pin_VER, 0); // Se estado 2, VER desliga.
      if (tempo_atual - tempo_anterior >= 500) { // Se passou 500ms, estado vira 1 e recomeça o loop.
        estado = 1;
        tempo_anterior = millis();
      }
      break;
}
if (BOT == 1){ //Se BOT = 1, Desliga VER
  digitalWrite(pin_VER, 0);
}
}