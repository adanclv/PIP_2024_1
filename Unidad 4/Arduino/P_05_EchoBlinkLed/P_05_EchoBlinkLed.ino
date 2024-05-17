int led = 13;
int v;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, HIGH);
  Serial.println("Led Prendido");
  delay(1000);
  digitalWrite(led, LOW);
  Serial.println("Led Apagado");
  delay(1000);
}
