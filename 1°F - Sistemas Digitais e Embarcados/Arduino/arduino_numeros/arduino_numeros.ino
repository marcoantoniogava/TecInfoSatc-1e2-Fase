int incomingByte = 0;
void setup() {
  Serial.begin(9600);
  Serial.println("Digite um numero ");
}

void loop() {
  if (Serial.available() > 0) {
   incomingByte = Serial.read();
   Serial.print("Eu recebi ");
   Serial.write(incomingByte);
   Serial.println();
   Serial.println("Digite um numero ");
  }
}