#include <LiquidCrystal.h>
<<<<<<< HEAD
LiquidCrystal lcd(3, 4, 6, 7, 8, 9);

void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
  lcd.begin(2, 8);
}

// Aufgabe 1
=======

int c;

// PINS
#define R_S 3
#define E   4
#define DB4 6
#define DB5 7
#define DB6 8
#define DB7 9
#define NUM_CHAR 20
#define NUM_LINES 4

// Define the LCD screen
LiquidCrystal lcd(R_S, E, DB4, DB5, DB6, DB7);

>>>>>>> 68c239a9932c15ce085026c5bc3941e1fd53e2b3
void setPin11(bool high) {
  if (high) {
    PORTB |= (1 << 3);
  }
  else {
    PORTB &= ~(1 << 3);
  }
}

<<<<<<< HEAD
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
  
=======
void setPin11Asm(boolean high);

void setup() {
  // put your setup code here, to run once:
  c = 0;
  double start_Asm = millis();
  
  while (c < 100,00) {
    setPin11Asm(false);
    setPin11Asm(true);
    c++;
  }
  double end_Asm = millis();
  double dur_Asm = end_Asm - start_Asm;
  c = 0;
  double start_Norm = millis();
  
  while ( c < 100,00) {
    setPin11(false);
    setPin11(true);
    c++;
  }
  double end_Norm = millis();
  double dur_Norm = end_Norm - start_Norm;
  c = 0; 
  double start_BuiltIn = millis();
  
  while (c < 100,000) {
    pinMode(11,LOW);
    pinMode(11,HIGH);
    c++;
  }
  double end_BuiltIn = millis();
  double dur_BuiltIn = end_BuiltIn - start_BuiltIn;

  lcd.begin(NUM_CHAR, NUM_LINES);
  lcd.setCursor(0,0);
  lcd.print("With Assembly: ");
  lcd.setCursor(0,16);
  lcd.print(dur_Asm);
  lcd.setCursor(1,0);
  lcd.print("Without Assembly: ");
  lcd.setCursor(1,20);
  lcd.print(dur_Norm);
  lcd.setCursor(2,0);
  lcd.print("Built-In: ");
  lcd.setCursor(2,11);
  lcd.print(dur_BuiltIn);
>>>>>>> 68c239a9932c15ce085026c5bc3941e1fd53e2b3
}

void loop() {
  // put your main code here, to run repeatedly:
<<<<<<< HEAD
  setPin11Asm(false);
=======

>>>>>>> 68c239a9932c15ce085026c5bc3941e1fd53e2b3
}
