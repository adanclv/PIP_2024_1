char letra;
int ascii;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    letra = Serial.read();
    if (letra != '\n'){
      ascii = (int)letra;
      Serial.print(letra); 
      Serial.print(" -> ");
      Serial.println(ascii);
    }
  }
}
