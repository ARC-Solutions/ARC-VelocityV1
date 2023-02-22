void setup() {
  Serial.begin(250000);
  pinMode(8,OUTPUT); //backward - black
  pinMode(9,OUTPUT); // forward - red
  pinMode(10,OUTPUT); //left - orange
  pinMode(11,OUTPUT); //right - yellow
}

void loop() {
  digitalWrite(11, HIGH);
  delay(400);
  digitalWrite(11,LOW);
  delay(600);
  //DIRECTION TEST
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  delay(300);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  delay(850);

  //DRIVE FORWARDS TO THE RIGHT TEST
  digitalWrite(9,HIGH);
  digitalWrite(10,HIGH);
  delay(350);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  delay(999);

  //DRIVE BACKWARDS TO THE LEFT TEST !!DO NOT RUN
  // digitalWrite(8,HIGH);
  // digitalWrite(10,HIGH);
  // delay(350);
  // digitalWrite(8,LOW);
  // digitalWrite(10,LOW);
  // delay(999);

  // digitalWrite(11, HIGH);
  // delay(500);
  // digitalWrite(11, LOW);
  // delay(200);
}