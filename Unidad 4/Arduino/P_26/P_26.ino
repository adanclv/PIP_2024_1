// Puente H l298
// EN - velocidad del giro
// IN1 - 
// IN2
// OUT1
// OUT2
int enA = 3;
int in1 = 5;
int in2 = 6;

// OUT1 y OUT2 se conectan del puente H al motor

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  // EnableA no lleva pinMode
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    int v = Serial.readString().toInt();
    digitalWrite(in1, 1);
    analogWrite(enA, v);
  }
  delay(100);
}
