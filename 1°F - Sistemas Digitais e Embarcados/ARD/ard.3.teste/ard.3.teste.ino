int incomingByte = 0;


void setup() {
  Serial.begin(9600); //velocidade de transmissão bps
  Serial.print("Digite um número");
}

void loop() {
  if(Serial.available() > 0 ){
    incomingByte = Serial.read();
    Serial.print("Eu recebi");
    Serial.write(incomingByte);
    Serial.println();
    Serial.println("Digite um numero");
    
    
  }
}



