int estado = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

float calificaciones[5];
int contadorCalificaciones = 0;

void loop() {
  if (estado == 0 || estado == 1 || estado == 2 || estado == 3 || estado == 4) {
    if (Serial.available() > 0) {
      float v = Serial.readString().toFloat();
      calificaciones[contadorCalificaciones] = v;
      contadorCalificaciones++;
      estado++;
    }
  } else if (estado == 5) {
    float suma = 0;
    for (int i = 0; i < 5; i++) {
      suma += calificaciones[i];
    }
    float promedio = suma / 5;
    Serial.print("El promedio de las calificaciones es: ");
    Serial.println(promedio, 2); // Muestra el promedio con 2 decimales
    estado = 6;
  } else if (estado == 6) {
    Serial.println("Desea repetir?....(1=SI, 0=NO)");
    estado++;
  } else if (estado == 7) {
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
      if (v == 1) {
        estado = 0;
        contadorCalificaciones = 0; // Reinicia el contador de calificaciones
      } else {
        estado = 6;
      }
    }
  }
  delay(100);
}