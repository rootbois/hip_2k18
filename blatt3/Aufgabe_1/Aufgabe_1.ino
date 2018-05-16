void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
}

// Aufgabe 1
void setPin11(bool high) {
  if (high) {
    PORTB |= (1 << 3);
  }
  else {
    PORTB &= ~(1 << 3);
  }
}

// Aufgabe 2
void setPin11Asm(bool high) {
  
}

void loop() {
  // put your main code here, to run repeatedly:

}
