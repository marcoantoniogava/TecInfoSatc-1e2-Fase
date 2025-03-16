const int pin_I0 = 2;
const int pin_I1 = 3;
const int pin_D0 = 8;
const int pin_D1 = 9;
bool estado = 0;
unsigned long tempo_anterior = 0;
void setup() {
  pinMode(pin_I0, INPUT);
  pinMode(pin_I1, INPUT);
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
  if (estado == 1){
    unsigned long tempo_atual = millis();
    if(tempo_atual - tempo_anterior >= 1000){
      digitalWrite(pin_D1, 1);
    }
  }
  if (i1 == 1) {
    digitalWrite(pin_D0, 0);
    digitalWrite(pin_D1, 0);
    estado = 0;
  }
  
}