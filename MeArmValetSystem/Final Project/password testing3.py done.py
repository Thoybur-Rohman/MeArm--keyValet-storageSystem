import serial #  Allows you to talk to the Arduino board
import time

#  Select port, yours may be different so check the port for your board 
usbport = 'COM4'

#  create a serial object
ser = serial.Serial(usbport, 9600, timeout=1)

#while True:
   #servo = raw_input("enter servo Nbr (0-4)")
   # position = raw_input("enter angle between 10 and 170:")
   # md = servo + "," + position + "\n"
   # ser.write(cmd)

def askpass():
    password = raw_input("enter password: ")
    return password
    
def checkpass(password):
    entry = raw_input("Enter your password")
    if entry == password:
        print("Correct password")
    else:
        print("Incorrect Password")

def collecting(password1, password2):
    while(True):
        selection = raw_input("Enter key holder:")
        if selection == "1":
            checkpass(password1)
            print 'Thank You'
        elif selection == "2":
            checkpass(password2)
def store():
    password  = askpass()
    return password
def move(s,p,):
    cmd = str(s) + "," +str(p) + "\n"
    ser.write(cmd)

password = 0
password2 = 0
while(True):
    Choice = raw_input("Are you collection or Inputting ?")
    
    if Choice == "inputting":
        holder = raw_input("Enter holder")
        if holder == "1":
            password = store()
            move(0,78)
            time.sleep(1)
            move(2,140)
            time.sleep(1)
            move(1,20)
            time.sleep(1)
            move(3,40)
            time.sleep(1)
            move(3,10)
            time.sleep(1)
            move(0,78)
            time.sleep(1)
            move(1,90)
            time.sleep(1)
            move(2,90)
            time.sleep(1)
            move(0,150)
            time.sleep(1)
            move(2,100)
            time.sleep(1)
            move(0,165)
            time.sleep(1)
            move(3,40)
            time.sleep(1)
            move(2,70)
            time.sleep(1)
            move(1,70)
            time.sleep(1)
            move(0,78)
            time.sleep(1)
           
            

        elif holder == "2":
            password2 = store()
             move(0,78)
            time.sleep(1)
            move(2,140)
            time.sleep(1)
            move(1,20)
            time.sleep(1)
            move(3,40)
            time.sleep(1)
            move(3,10)
            time.sleep(1)
            move(0,78)
            time.sleep(1)
            move(1,90)
            time.sleep(1)
            move(2,90)
            time.sleep(1)
            move(0,150)
            time.sleep(1)
            move(2,100)
            time.sleep(1)
            move(0,145)
            time.sleep(1)
            move(3,40)
            time.sleep(1)
            move(2,70)
            time.sleep(1)
            move(1,70)
            time.sleep(1)
            move(0,78)
            time.sleep(1)
           
            
            
            
            
        
            

        
            

            
    elif Choice == "collecting":
        collecting(password,password2)





        



