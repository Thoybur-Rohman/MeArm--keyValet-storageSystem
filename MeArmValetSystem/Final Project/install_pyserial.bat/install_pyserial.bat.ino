/*SerialServo*/

#include <Servo.h>

const int servos = 4;
Servo myservo [servos];
int middle=11;
int right=10;
int claw=9;
int left=8;
 
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   myservo[0].attach(middle);
   myservo[1].attach(left);
   myservo[2].attach(right);
   myservo[3].attach(claw);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    int selectedServo = Serial.parseInt();
    if(selectedServo>=0 && selectedServo < servos){
       int pos = Serial.parseInt();
       if(pos >= 10 && pos <= 170){
          myservo[selectedServo].write(pos);
       }
    }
    
  }

}
