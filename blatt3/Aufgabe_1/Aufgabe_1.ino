void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
}

// Aufgabe 1
void setPin11(bool high) {
  // pin 11 = PB3
  if (high) {
    PORTB |= (1 << 3);
  }
  else {
    PORTB &= ~(1 << 3);
  }
}
//////////////////////////////////////////////////////////////////////////////
// Aufgabe 4
//////////////////////////////////////////////////////////////////////////////
void __attribute__(optimize("O0")) setPin11(bool high) {
  // pin 11 = PB3
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
