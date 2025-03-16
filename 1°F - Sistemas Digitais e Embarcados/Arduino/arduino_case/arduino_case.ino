const int led_verde = 8;
const int led_vermelho = 9;
const int led_amarelo = 10;
char led;

void setup() {
  pinMode(led_verde, OUTPUT);
  pinMode(led_vermelho, OUTPUT);
  pinMode(led_amarelo, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    led = Serial.read();
    switch (led) {
      case 'R': digitalWrite(led_verde, HIGH);
        break;
      case 'r': digitalWrite(led_verde, LOW);
        break;
      case 'B': digitalWrite(led_vermelho, HIGH);
        break;
      case 'b': digitalWrite(led_vermelho, LOW);
        break;
      case 'G': digitalWrite(led_amarelo, HIGH);
        break;
      case 'g': digitalWrite(led_amarelo, LOW);
        break;
      default: Serial.println("Nenhum led selecionado!!!");
       break;
    }
  }
}