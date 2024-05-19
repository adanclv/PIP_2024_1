int estado = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

float peso;
float altura;

void loop() {
  if (estado == 0 || estado == 1) {
    if (Serial.available() > 0) {
      float v = Serial.readString().toFloat();
      if (estado == 0) {
        peso = v;
      } else {
        altura = v;
      }
      estado++;
    }
  } else if (estado == 2) {
    float imc = peso / (altura * altura);
    Serial.print("Su IMC es: ");
    Serial.println(imc);
    estado = 3;
  } else if (estado == 3) {
    Serial.println("Desea repetir?....(1=SI, 0=NO)");
    estado++;
  } else if (estado == 4) {
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
      if (v == 1) {
        estado = 0;
      } else {
        estado = 3;
      }
    }
  }
  delay(100);
}