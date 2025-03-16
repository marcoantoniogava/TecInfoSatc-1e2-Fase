#include <DHT.h>

#define DHTPIN 23     // Pino onde o DHT11 está conectado
#define DHTTYPE DHT11 // Define o tipo de sensor

DHT dht(DHTPIN, DHTTYPE); // Inicializa o sensor DHT11

void setup() {
  Serial.begin(115200); // Inicia a comunicação serial
  dht.begin();          // Inicia o sensor
}

void loop() {
  // Espera alguns segundos entre as leituras
  delay(2000);
  
  // Leitura da umidade e temperatura
  float h = dht.readHumidity();
  float t = dht.readTemperature(); // Em Celsius
  
  // Verifica se a leitura falhou e imprime um aviso
  if (isnan(h) || isnan(t)) {
    Serial.println("Falha ao ler do DHT11!");
    return;
  }

  // Imprime os valores na Serial Monitor
  Serial.print("Umidade: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" °C");
}
