int MAX = 255;

int pins   [7] = {3, 5, 6, 9, 10 , 11, 13};
int brites [7] = {0, 0, 0, 0, 0,  0,  0 };

void setup() {
  for (int i; i < 7; i++) {
    pinMode(pins[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  // check if data has been sent from the computer:
  if (Serial.available()) {
    byte serial = Serial.read();
    if (serial > 0 && serial < 70) {
      int i = (serial-1)/10;
      int vel = serial % 10 ? serial % 10 * 25 : MAX;
      brites[i] = vel;
    }
    else {
        for (int i; i<3; i++) {
          brites[i] = 42 * (i+1);
          brites[5-i] = 42 * (i+1);
        }
    }
  }

  for (int i; i<6; i++) {
    analogWrite(pins[i], brites[i]);
    brites[i] -= brites[i] > 0 ? 1 : 0; 
  }
  int i = 6;
  digitalWrite(pins[i], brites[i]);
  delay(4);
  brites[i] = LOW;
  digitalWrite(pins[i], brites[i]);
  

}  
