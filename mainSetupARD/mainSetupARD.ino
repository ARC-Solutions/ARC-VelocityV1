// arduino code
// read the string from the serial port and turn on/off the associated pin
int x;
String str;

void setup()
{
  Serial.begin(9600);
  pinMode(8, OUTPUT); // backward - black
  pinMode(9, OUTPUT); // forward - red
  pinMode(10, OUTPUT); // left - orange
  pinMode(11, OUTPUT); // right - yellow
}

void loop()
{
  if(Serial.available() >= 0)
  {
    str = Serial.readStringUntil('\n');
    if (str.equals("left_on")) {
      digitalWrite(11, LOW);
      digitalWrite(10, HIGH);
    }
    if (str.equals("left_off")) {
      digitalWrite(10, LOW);
    }
    if (str.equals("right_on")) {
      digitalWrite(10, LOW);
      digitalWrite(11, HIGH);
    }
    if (str.equals("right_off")) {
      digitalWrite(11, LOW);
    }
    if (str.equals("backward_on")) {
      digitalWrite(9, LOW);
      digitalWrite(8, HIGH);
    }
    if (str.equals("backward_off")) {
      digitalWrite(8, LOW);
    }
    if (str.equals("forward_on")) {
      digitalWrite(8, LOW);
      digitalWrite(9, HIGH);
    }
    if (str.equals("forward_off")) {
      digitalWrite(9, LOW);
    }
  }
}