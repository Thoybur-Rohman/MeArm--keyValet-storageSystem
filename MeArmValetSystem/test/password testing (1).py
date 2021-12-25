import serial #  Allows you to talk to the Arduino board

#  Select port, yours may be different so check the port for your board 
usbport = 'COM4'

#  create a serial object
ser = serial.Serial(usbport, 9600, timeout=1)

while True:
    servo = raw_input("enter servo Nbr (0-3)")
    position = raw_input("enter angle between 10 and 170:")
    cmd = servo + "," + position + "\n"
    ser.write(cmd)



    
def move(s,p):
    cmd = s + "," + p + "\n"
    ser.write(cmd)


