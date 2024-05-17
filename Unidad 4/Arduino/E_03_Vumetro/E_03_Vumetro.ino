int led[] = {2, 3, 4, 5, 6};
bool estado[] = {false, false, false, false, false};
int intensidad = 0;

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 5; i++){
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    intensidad = Serial.readString().toInt();
    for(int i = 0; i < intensidad; i++){
      estado[i] = true;
    }

    for(int i = 0; i < 5; i++){
      digitalWrite(led[i], estado[i]);
      estado[i] = false;
    }

    
  }
}
