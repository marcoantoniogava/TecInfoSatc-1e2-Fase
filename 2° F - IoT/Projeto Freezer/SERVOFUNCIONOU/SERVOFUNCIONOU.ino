#include <ESP32Servo.h> // Inclui a biblioteca ESP32Servo

Servo myServo; // Cria um objeto Servo

void setup() {
  myServo.attach(18); // Conecta o pino de controle ao GPIO 18 do ESP32
}

void loop() {
  // Move o servo de 0 a 180 graus
  for (int pos = 0; pos <= 180; pos += 1) {
    myServo.write(pos); // Diz ao servo para ir para a posição "pos"
    delay(5000);          // Aguarda 15 ms para o servo alcançar a posição
  }

  // Move o servo de 180 a 0 graus
  for (int pos = 180; pos >= 0; pos -= 1) {
    myServo.write(pos); // Diz ao servo para ir para a posição "pos"
    delay(5000);          // Aguarda 15 ms para o servo alcançar a posição
  }
}
