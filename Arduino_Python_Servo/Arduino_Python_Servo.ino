#include <Servo.h>
Servo myServo;
int servoPin = 9;
String servoPos;
int pos;

void setup() {
  // put your setup code here, to run once:
Serial.begin(19200);
myServo.attach(servoPin);
myServo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available() == 0){
}
  servoPos = Serial.readStringUntil('\r');
  pos = servoPos.toInt();
  myServo.write(pos);
  delay(50);
}
