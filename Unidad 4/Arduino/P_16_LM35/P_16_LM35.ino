// Sensor de temperatura analogico
// en el que cada grado equivale aproximadamente 5mV

int lm35 = A0;

// ADC - Conversor analogo digital
// (Convierte una señal analogica a una señal digital)
// Voltaje de referencia: %V
// Bits de resolucion: 10.... 2^10 = 1024 valores posibles
// 0V = 0 - 5V = 1023

// 5/1023 = .0048Volts.... = 4.8mV

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(lm35);
  Serial.println("Valor leido: " + String(valor));
  valor = (5.0 * valor * 100.0) / 1023.0; // °C
  Serial.println(" Temp: " + String(valor));
  delay(100);
}
