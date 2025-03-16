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

void loop() {{
  if (Serial.available())
    led = Serial.read();
    if (led == 'R') {
      digitalWrite(led_verde, HIGH);
    }
    else {
      if (led == 'r') {
        digitalWrite(led_verde, LOW);
      }
    }
    if (led == 'B') {
      digitalWrite(led_vermelho, HIGH);
    }
    else {
      if (led == 'b') {
        digitalWrite(led_vermelho, LOW);
      }
    }
    if (led == 'G') {
      digitalWrite(led_amarelo, HIGH);
    }
    else {   
      if (led == 'g') {
        digitalWrite(led_amarelo, LOW);
      }
    }
  }
}