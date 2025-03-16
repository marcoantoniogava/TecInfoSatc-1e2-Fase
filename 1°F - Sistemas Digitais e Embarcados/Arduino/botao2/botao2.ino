const int pin_I0 = 2;
const int pin_I1 = 3;
const int pin_D2 = 10;
const int pin_D3 = 11;
const int pin_D0 = 8;
const int pin_D1 = 9;
int estado = 0;
unsigned long tempo_anterior = 0;
void setup() {
  pinMode(pin_I0, INPUT);
  pinMode(pin_I1, INPUT);
  pinMode(pin_D2, OUTPUT);
  pinMode(pin_D3, OUTPUT);
  pinMode(pin_D0, OUTPUT);
  pinMode(pin_D1, OUTPUT);
}

void loop() {
  bool i0 = digitalRead(pin_I0);
  bool i1 = digitalRead(pin_I1);
  if (i0 == 1) {
    digitalWrite(pin_D0, 1);
    estado = 1;
    tempo_anterior = millis();
  }
  unsigned long tempo_atual = millis();

  switch (estado) {
    case 0:
      digitalWrite(pin_D0, 0);
      digitalWrite(pin_D1, 0);
      digitalWrite(pin_D2, 0);
      digitalWrite(pin_D3, 0);
      break; case 1 : digitalWrite(pin_D0, 1);
      if (tempo_atual - tempo_anterior >= 1000) {
        estado = 2;
        tempo_anterior = millis();
      }
      break; case 2 : digitalWrite(pin_D1, 1);
      if (tempo_atual - tempo_anterior >= 500) {
        estado = 3;
        tempo_anterior = millis();
      }
      break; case 3 : digitalWrite(pin_D2, 1);
      if (tempo_atual - tempo_anterior >= 250) {
        estado = 4;
        tempo_anterior = millis();
      }
      break; case 4 : digitalWrite(pin_D3, 1);
      if (tempo_atual - tempo_anterior >= 500) {
        estado = 2;
        tempo_anterior = millis();
      }
  } }