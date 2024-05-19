int led[] = {2, 3, 4};

void setup() {
  for(int i = 0; i < 3; i++){
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
}
void loop() {
  //Verde
  digitalWrite(led[0], HIGH);
  delay(5000);
  for(int i = 0; i < 5; i++){
    digitalWrite(led[0], HIGH);
    delay(500);
    digitalWrite(led[0], LOW);
    delay(500);
  }
  digitalWrite(led[0], LOW);
  
  //Amarillo
  digitalWrite(led[1], HIGH);
  delay(3500);
  digitalWrite(led[1], LOW);

  //Rojo
  digitalWrite(led[2], HIGH);
  delay(5000);
  for(int i = 0; i < 5; i++){
    digitalWrite(led[2], HIGH);
    delay(500);
    digitalWrite(led[2], LOW);
    delay(500);
  }
  digitalWrite(led[2], LOW);
}
