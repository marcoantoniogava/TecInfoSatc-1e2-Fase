
const int led_verdao = 8;			//
const int led_azul = 9;			//
const int led_verde = 10;			//
char led;					//

void setup() {
  pinMode(led_verdao, OUTPUT);		//
  pinMode(led_azul, OUTPUT);			//
  pinMode(led_verde, OUTPUT);			//
  Serial.begin(9600); 			// Definição da velocide de transmissão em 115200 bps
}

void loop() {{
  if(Serial.available()) {			//
    led = Serial.read();	
    switch(led) {
    case 'R':	                     // Led verdao - greenzão
      digitalWrite(led_verdao, HIGH); 	// Acende o led
    					break;
    case 'r':			                    //
      digitalWrite(led_verdao, LOW);  	// Apaga o led
             break;
    case 'G':                           // Led azul - blue
      digitalWrite(led_azul, HIGH); 		// Acende o led
             break;
  					//
    case 'g': 				
        digitalWrite(led_azul, LOW); 		// Apaga o led
               break;
    case 'B':  				                 // Led verde - green
     digitalWrite(led_verde, HIGH); 		// Acende o led
    			  break;
     case 'b': 				
        digitalWrite(led_verde, LOW);
        
      default:
               break;  
   
   
    }
  }
} 

   

    
  

    
