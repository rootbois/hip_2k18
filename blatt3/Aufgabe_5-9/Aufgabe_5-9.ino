// Made with contributions by Jan Burchard's example 
// code for low-level Arduino programming

/////////////////// Aufgabe 5 /////////////////////////////

void timer2pin12Interrupt() {
  
  // 100 Hz- Signal
  // --> 200x\second
  // divider at 64
  // --> counter incr at 125000 Hz
  // --> count to 625

  //Disabling interrupts, and resetting contr. registers
  cli();
  TCCR2A = 0;     
  TCCR2B = 0;  
  
  // setting ck prescaler and CTC mode
  TCCR2B |= (1 << CS22);
  TCCR2A |= (1 << WGM21);
    
  // Setting OCR2A, it will count to 625, 
  // then overflow and TOV2 is TOV2 + 1
  // if TOV2 = 1 with an addition of 1, 
  // it will be 0. Therefore 200x \second
  
  OCR2A = 625;
  TIMSK2 |= (1 << OCIE2A);    

  // enabling interrupts
  sei();
}

// ISRfunction to toggle Pin 12
ISR(TIMER2_COMPA_vect) {
  PINB |= (1 << 4);
}

///////// Aufgabe 6 ///////////
void setFreqToPin12(int freq){
  OCR2A = (int)(125000/(freq*2));
}

void timer2interruptSetup() {
  cli();
  TCCR2A = 0;     
  TCCR2B = 0;  
  
  // setting ck prescaler and CTC mode
  TCCR2B |= (1 << CS22);
  TCCR2A |= (1 << WGM21);
  OCR2A = 255;
  TIMSK2 |= (1 << OCIE2A);    

  // enabling interrupts
  sei();
}

void setup() {
  timer2interruptSetup();
  pinMode(13, OUTPUT);
}

void loop() {

}
