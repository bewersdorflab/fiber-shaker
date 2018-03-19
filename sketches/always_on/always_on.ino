int motor_pin1 = 3;
int motor_pin2 = 5;

float target_voltage = 3;

void setup() {
  pinMode(motor_pin1, OUTPUT);
  pinMode(motor_pin2, OUTPUT);
}

void loop() {
  analogWrite(motor_pin1, 255 * target_voltage / 5);
  analogWrite(motor_pin2, 255 * target_voltage / 5);
}
