int status = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int valorA;
int valorB;
void loop() {
  // put your main code here, to run repeatedly:
  if(status == 0 || status == 1){
    if(Serial.available() > 0){
        int v = Serial.readString().toInt();
        if(status == 0){ valorA = v; } else { valorB = v; }
        status++;
      }
  } else if(status == 2){
    int r = valorA + valorB;
      Serial.println("Suma de A y B: " + String(r));
      status++;
  } else if(status == 3){
    Serial.println("Desea repetir?....(1=SI, 0=NO)");
    status++;
  } else if(status == 4){
    if(Serial.available() > 0){
      int v = Serial.readString().toInt();
      if(v == 1){ 
        status = 0 
      } else {
        
      }
    }
  }

  '''switch(status){
    case 0:
    case 1:
      if(Serial.available() > 0){
        int v = Serial.readString().toInt();
        if(status == 0){ valorA = v; } else { valorB = v; }
        status++;
      }
    break;
    case 2:
      int r = valorA + valorB;
      Serial.println("Suma de A y B: " + String(r));
      status++;
    break;
    case 3:
      Serial.println("Desea repetir?....(1=SI, 0=NO)");
      status++;
    break;
    case 4:
      if(Serial.available() > 0){
        int v = Serial.readString().toInt();
        if(v == 1){ status = 0 }
      }
    break;
  }'''
  delay(100);
}
