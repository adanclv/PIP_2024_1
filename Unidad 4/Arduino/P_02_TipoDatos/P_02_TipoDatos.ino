short corto;
byte bb;
int entero;
long largo;

float floating;
double doble;

char c;
bool booleano;

String cadena;

int numero[5];

void setup() {
  // put your setup code here, to run once:
  // Modulo UART (Modulo Asincrono Universal de Transmision y Recepcion de Datos)
  Serial.begin(9600); // Inicializa la comunicacion serial
  // 9600 badios a los que se comunica arduino con otros dispositivos
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println('Holas');
  delay(500); // milisegundos

}
