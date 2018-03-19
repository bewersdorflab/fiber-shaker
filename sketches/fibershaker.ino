int receivedMessage = 0;
boolean newData = false;
const int ledPin =  12;      // the number of the motor pin

void setup() {
 Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
 recvMessage();
 interpretMessage();
 showNewData();
}

void recvMessage() {
 if (Serial.available() > 0) {
 receivedMessage = Serial.parseInt();
}
 }

void interpretMessage() {
  if (receivedMessage == 1) {
    newData = true;
  }
  else if (receivedMessage == 0) {
    newData = false;
  }
}

void showNewData() {
 if (newData == true) {
 digitalWrite(ledPin, HIGH);
 }
 else if (newData == false) {
 digitalWrite(ledPin, LOW);
 }
}
