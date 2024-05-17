//Voltaje de referencia 9V o 5 jejeje
//Bits de resolucion: 10 bits de resolucion... 1024 valores posibles

// cada valor que les da el arduino se distancia uno del otro en 4.8V
// la señal analogica del arduino funciona con los pines analogicos

int potenciometro = A0;

void setup() {
  // put your setup code here, to run once:
  //pinMode no se utiliza para pines analogicos
  //NOTA: un pin analogico solo es de entrada
  Serial.begin(9600);
}

// P1    P2    P3
//GND    A#     5V
//       A0

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciometro);
  Serial.println(valor);
}

// POTENCIOMETRO

