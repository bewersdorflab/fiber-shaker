int motor_pin = 2;
float target_voltage = 3;

void setup() {
  pinMode(motor_pin, OUTPUT);
}

void loop() {
  analogWrite(motor_pin, 255 * target_voltage / 5);
}
