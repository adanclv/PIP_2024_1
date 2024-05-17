double x1, x2, y1, y2, resultado;
int aux = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(aux == 0){
    if(Serial.available() > 0){
      x1 = Serial.readString().toDouble();
      Serial.println("x1: " + (String)x1);
      aux++;
    }
  }else if(aux == 1){
      if(Serial.available() > 0){
        y1 = Serial.readString().toDouble();
        Serial.println("y1: " + (String)y1);
        aux++;
      }
  }else if(aux == 2){
     if(Serial.available() > 0){
      x2 = Serial.readString().toDouble();
      Serial.println("x2: " + (String)x2);
      aux++;
      }
  }else if(aux == 3){
    if(Serial.available() > 0){
      y2 = Serial.readString().toDouble();
      Serial.println("y2: " + (String)y2);
      aux++;
    }
  }else if(aux == 4){
    resultado = pow(x2 - x1, 2) + pow(y2 - y1, 2);
    resultado = sqrt(resultado);
    Serial.println("Distancia: " + (String)resultado);
    aux = 0;
  }
}