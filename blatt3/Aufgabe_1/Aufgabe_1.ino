#include <LiquidCrystal.h>
LiquidCrystal lcd(3, 4, 6, 7, 8, 9);

void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
  lcd.begin(2, 8);
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
void setPin11Asm( const bool high) {
   asm volatile (
    "start:"
    "cp %2, %3\n\t"
    "rjmp %3\n\t"
    "sbi %0, %1\n\t"
    "cbi %0, %1\n\t"
    "rjmp start\n\t"
    :: "I" (_SFR_IO_ADDR(PORTB)), "I" (PORTB3), "I" (high), "I" (1)
   );
  
}

void loop() {
  // put your main code here, to run repeatedly:
  setPin11Asm(false);
}
