int led[] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 8; i++){
    pinMode(led[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);
}

String cadena = "";
int aux = 1;
int patron[8];
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    cadena = Serial.readString();
    aux = 2;
    Serial.println(cadena);
    for(int i = 0; i < cadena.length() - 1; i++){
      patron[i] = cadena.charAt(i) - '0';
    }
    }
    
  if(aux == 2){
      for(int i = 0; i < cadena.length()-1; i++){
      digitalWrite(led[patron[i] - 1], true);
      delay(500);
      digitalWrite(led[patron[i] - 1], false);
      delay(500);
    }
  }
}
