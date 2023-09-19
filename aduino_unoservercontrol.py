from getchar import Getchar
from getchar import Getchar
import serial
sp = serial.Serial('COM3', 9600, timeout=1)

kb =Getchar ()
key = ''
while key!='Q':
    key = kb.getch()
    if key == '.':
        sp.write('.'.encode())
    elif key == ',':
        sp.write(','.encode())
    else:
        pass