int LDR = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(LDR);
  Serial.println("Valor :" + String(valor));
  delay(200);
}
