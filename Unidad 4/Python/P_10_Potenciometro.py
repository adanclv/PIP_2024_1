import serial as conn

arduino = conn.Serial(port="COM8", baudrate=9600, timeout=1)
# arduino = conn.Serial(port="/dev/ttyACM0")

print('Conexion con arduino exitosa')

while True:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)