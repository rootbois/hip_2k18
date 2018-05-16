int c;
void setPin11(bool high) {
  if (high) {
    PORTB |= (1 << 3);
  }
  else {
    PORTB &= ~(1 << 3);
  }
}

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

  
}

void loop() {
  // put your main code here, to run repeatedly:

}
