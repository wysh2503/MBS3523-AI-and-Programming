String Command;

void setup() {
  // put your setup code here, to run once:
Serial.begin(19200);
pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available()==0){
}
Command = Serial.readStringUntil('\r');
if (Command == "ON"){
  digitalWrite(13, HIGH);
 }
if (Command == "OFF"){
  digitalWrite(13, LOW);
 }
}
