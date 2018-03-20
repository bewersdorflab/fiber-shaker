int receivedMessage = 0;
boolean newData = false;
int motor_pin1 = 3;
int motor_pin2 = 5;
float target_voltage = 3;

void setup() {
 Serial.begin(9600);
   pinMode(motor_pin1, OUTPUT);
   pinMode(motor_pin2, OUTPUT);
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
  analogWrite(motor_pin1, 255 * target_voltage / 5);
  analogWrite(motor_pin2, 255 * target_voltage / 5);
 }
 else if (newData == false) {
 digitalWrite(motor_pin1, LOW);
 digitalWrite(motor_pin2, LOW);
 }
}
