#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include <DHT.h>

// Credenciais do WiFi
#define WIFI_SSID "Marco"
#define WIFI_PASSWORD "12345678"

// Credenciais do Bot Telegram
#define BOT_TOKEN "Token"
#define CHAT_ID "ChatID"

// Configurações do sensor DHT11
#define DHTPIN 15        // PINO de dados do DHT11
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Configurações do Reed Switch
#define REED_PIN 21      // PINO de entrada do reed switch

// WiFi e Telegram Bot
WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

// Variáveis de status
bool portaAberta = false;
bool temperaturaAlta = false;
float temperatura = 0.0;
unsigned long tempoAnterior = 0;
const long intervaloEnvio = 30000; // 30 segundos de intervalo entre mensagens

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(REED_PIN, INPUT_PULLUP); // Configura o reed switch como entrada com pull-up
  
  // Conectar ao WiFi
  conectarWiFi();
}

void conectarWiFi() {
  Serial.print("Conectando ao WiFi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");
  client.setInsecure();
}

void enviarMensagem(String mensagem) {
  if (bot.sendMessage(CHAT_ID, mensagem, "")) {
    Serial.println("Mensagem enviada com sucesso!");
  } else {
    Serial.println("Falha ao enviar mensagem.");
  }
}

void verificarEstado() {
  // Lê o status da porta
  portaAberta = digitalRead(REED_PIN) == HIGH;

  // Lê a temperatura atual
  temperatura = dht.readTemperature();

  // Verifica se houve erro de leitura do DHT11
  if (isnan(temperatura)) {
    Serial.println("Falha ao ler o sensor DHT11");
    return;
  }

  // Define se a temperatura é alta (ajuste o valor conforme necessário)
  temperaturaAlta = temperatura > 5.0; // Exemplo: temperatura alta acima de 5°C

  // Lógica para enviar a mensagem correta
  String mensagem;
  if (portaAberta && temperaturaAlta) {
    mensagem = "Alerta: Porta aberta e temperatura alta!";
  } else if (portaAberta) {
    mensagem = "Alerta: Porta do freezer está aberta!";
  } else if (temperaturaAlta) {
    mensagem = "Alerta: Temperatura alta no freezer!";
  } else {
    mensagem = "Tudo ok: Freezer funcionando normalmente.";
  }

  // Enviar a mensagem se o intervalo de tempo foi atingido
  if (millis() - tempoAnterior >= intervaloEnvio) {
    enviarMensagem(mensagem);
    tempoAnterior = millis();
  }
}

void loop() {
  verificarEstado();
  delay(2000); // Aguarda 2 segundos antes de verificar novamente
}
