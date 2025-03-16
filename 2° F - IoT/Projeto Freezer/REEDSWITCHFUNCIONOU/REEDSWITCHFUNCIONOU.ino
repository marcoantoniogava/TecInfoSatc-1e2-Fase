const int reedPin = 23; // Pino onde o reed switch está conectado
int reedState = 0;      // Variável para armazenar o estado do reed switch

void setup() {
  Serial.begin(115200);
  pinMode(reedPin, INPUT_PULLUP); // Configura o pino com pull-up interno
}

void loop() {
  reedState = digitalRead(reedPin); // Lê o estado do reed switch

  if (reedState == LOW) {
    Serial.println("Porta fechada (íman próximo)");
  } else {
    Serial.println("Porta aberta (íman afastado)");
  }
  delay(500);
}
