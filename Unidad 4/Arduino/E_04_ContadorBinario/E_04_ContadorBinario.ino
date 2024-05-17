int led[] = {2, 3, 4, 5, 6, 7, 8, 9};
bool estado[] = {false, false, false, false, false, false, false, false};
int aux = 0;
int temp;

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 8; i++){
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 1; i < 256; i++){
    temp = i;
    while(temp > 0){
      estado[7 - aux] = (temp % 2 == 1) ?true :false;
      temp = (int)temp / 2;
      aux++;
    }
    Serial.print(String(i) + " -> ");

    for (int j = 0; j < 8; j++) {
      digitalWrite(led[j], estado[j]);
      Serial.print(estado[j]);
      estado[j] = false;
    }
    Serial.println();
    aux = 0;
    delay(700);
  }
}
