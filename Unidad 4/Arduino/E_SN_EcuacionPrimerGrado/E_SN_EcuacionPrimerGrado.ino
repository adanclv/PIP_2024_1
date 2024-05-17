double m, x, b, resultado;
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
      m = Serial.readString().toDouble();
      Serial.println("m: " + (String)m);
      aux++;
    }
  }else if(aux == 1){
      if(Serial.available() > 0){
        x = Serial.readString().toDouble();
        Serial.println("x: " + (String)x);
        aux++;
      }
  }else if(aux == 2){
     if(Serial.available() > 0){
      b = Serial.readString().toDouble();
      Serial.println("b: " + (String)b);
      aux++;
      }
  }else if(aux == 3){
    resultado = m * x + b;
    Serial.println("y = " + (String)resultado);
    aux = 0;
  }
}