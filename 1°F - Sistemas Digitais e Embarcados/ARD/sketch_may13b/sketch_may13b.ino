const int pin_botaoA = 9;
const int pin_botaoB = 10;
const int pin_led1 = 2;
const int pin_led2 =3;
const int pin_led3= 4;
bool botaoA = false;
bool botaoB = false;


void setup() {
    pinMode(pin_botaoA,INPUT);
    pinMode(pin_botaoB ,INPUT);
    pinMode(pin_led1, OUTPUT);
    pinMode(pin_led2, OUTPUT);
    pinMode(pin_led3, OUTPUT);

}

void loop() {
   botaoA = digitalRead(pin_botaoA);
   botaoB = digitalRead(pin_botaoB);
   if(botaoA && botaoB){
    digitalWrite(pin_led1, HIGH);
    
   }
 
   else { 
     digitalWrite(pin_led1, LOW);
   }


     if (botaoA || botaoB){
      digitalWrite(pin_led2, HIGH);
   }

   else { 
    digitalWrite(pin_led2, LOW);
   }
   
     if (botaoA ^ botaoB){
      digitalWrite(pin_led3, HIGH);
   }
   else { 
    digitalWrite(pin_led3, LOW);
   }
  }




   

