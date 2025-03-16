#include <ESP32Servo.h>
#include <DHT.h>

#define DHTPIN 15         // Pino de dados do DHT11
#define DHTTYPE DHT11     // Tipo de sensor
#define REED_PIN 21       // Pino do reed switch
#define RED_PIN 25        // Pino do LED RGB vermelho
#define GREEN_PIN 26      // Pino do LED RGB verde
#define BLUE_PIN 27       // Pino do LED RGB azul
#define SERVO_PIN 18      // Pino do servo
#define TEMPERATURE_THRESHOLD 25 // Limite de temperatura (em °C)

DHT dht(DHTPIN, DHTTYPE);
Servo myServo;

bool doorClosed = true;

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(REED_PIN, INPUT_PULLUP);  // Pino do reed switch com pull-up interno
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);

  myServo.attach(SERVO_PIN);
  myServo.write(0);  // Posição inicial do servo (porta fechada)
}

void loop() {
  float temperature = dht.readTemperature();
  int reedState = digitalRead(REED_PIN);

  if (isnan(temperature)) {
    Serial.println("Falha na leitura do sensor DHT!");
    return;
  }

  // Verificação das condições e controle do LED RGB
  if (temperature > TEMPERATURE_THRESHOLD && reedState == HIGH) {
    Serial.println("Alerta: Porta aberta e temperatura elevada, em: " + String(temperature) + " °C");
    setLEDColor(255, 0, 0);  // Vermelho
  } else if (temperature > TEMPERATURE_THRESHOLD) {
    Serial.println("Alerta: Temperatura elevada em: " + String(temperature) + " °C");
    setLEDColor(255, 255, 0);  // Amarelo
  } else if (reedState == HIGH) {
    Serial.println("Aviso: Porta aberta!");
    setLEDColor(0, 0, 255);  // Azul

    // Inicia o fechamento automático da porta se estiver aberta
    if (doorClosed) {
      delay(5000);  // Espera 5 segundos com a porta aberta
      myServo.write(180);  // Fecha a porta (gira 180 graus)
      doorClosed = false;  // Atualiza o status da porta
      delay(5000);  // Espera mais 5 segundos
      myServo.write(0);  // Retorna o servo à posição inicial
    }
  } else {
    Serial.println("Status: Tudo normal.");
    setLEDColor(0, 255, 0);  // Verde
    doorClosed = true;  // Porta fechada novamente
  }

  delay(2000); // Ajuste o tempo de delay conforme necessário
}

void setLEDColor(int redValue, int greenValue, int blueValue) {
  analogWrite(RED_PIN, redValue);
  analogWrite(GREEN_PIN, greenValue);
  analogWrite(BLUE_PIN, blueValue);
}
