import serial as conn

arduino = conn.Serial(port="COM8", baudrate=9600, timeout=1)
print('Conexion con arduino exitosa')

file = open('../Archivos/dato_potenciometro.csv', 'w')
i = 0
while i < 10:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)
    file.write(a + '\n')
    i += 1

file.flush()
file.close()