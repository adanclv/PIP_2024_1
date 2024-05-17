// El Arduino posee un led interno de pruebas en el pin digital 13
int led = 13;

// Arduino tiene 14 pines digitales (0 al 13)
// Sin embargo, cuando se utiliza comunicacion serial no se pueden utilizar los pines 0 y 1 como digitales

void setup() {
  // put your setup code here, to run once:
  // Se debe definir el modo de trabajo (Entrada o salida) de todos los pines digitales
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, LOW);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);
}
