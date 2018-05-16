void setup() {
  pinMode(12, OUTPUT);
  // Timer 1
  noInterrupts();           // Turn off all interrupts temporarily.
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0;                // Initialize with 0.
  OCR1A = 31250;            // Output Compare Register vorbelegen 
  TCCR1B |= (1 << CS12);    // prescale = 256
  TIMSK1 |= (1 << OCIE1A);  // ActivateTimer Compare Interrupt
}

volatile uint32_t sCount = 0;
volatile uint32_t index = 0;
uint32_t duration[10] = {500, 501, 502, 503, 504, 505, 506, 507, 508, 509};
uint32_t melody[] = {207.65, 164.81, 103.83, 116.54};

void configInterrupt() {
  volatile uint32_t tCount = 0;
  OCR1A = 31250;
  interrupts(); 
}

// Aufgabe 8 in 6
if (tCount >= sCount) {
  index++;
  sCount = tCount + duration[index];
  if (index == 10) {
    index = 0;
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
