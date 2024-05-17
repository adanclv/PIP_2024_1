int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Cualquier valor numerico > 0 or < 0 prende el led
  // Cualquier valor no numerico apaga el led
  if(Serial.available() > 0){
    int v = Serial.readString().toInt();
    digitalWrite(led, v);
  }
}
