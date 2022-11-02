#include <Servo.h>

// Arduino pin assignment

//#define PIN_POTENTIOMETER 3 // Potentiometer at Pin A3
// Add IR Sensor Definition Here !!!
#define PIN_SENSOR 0
#define PIN_LED 9
#define PIN_SERVO 10

#define _DUTY_MIN 553  // servo full clock-wise position (0 degree)
#define _DUTY_NEU 1476 // servo neutral position (90 degree)
#define _DUTY_MAX 2399 // servo full counter-clockwise position (180 degree)

#define _DIST_MIN 100.0
#define _DIST_MAX 250.0

#define LOOP_INTERVAL 50   // Loop Interval (unit: msec)
#define ALPHA 0.5 

Servo myservo;
unsigned long last_loop_time;   // unit: msec
float dist_ema, dist_prev = _DIST_MAX;

void setup()
{
  pinMode(PIN_LED, OUTPUT);

  myservo.attach(PIN_SERVO); 
  myservo.writeMicroseconds(_DUTY_NEU);
  
  Serial.begin(1000000); //Set MAX
}

void loop()
{
  unsigned long time_curr = millis();
  int a_value, duty;
  float dist, dist_prev;

  // wait until next event time
  if (time_curr < (last_loop_time + LOOP_INTERVAL))
    return;
  last_loop_time += LOOP_INTERVAL;

  // Remove Next line !!!
  // a_value = analogRead(PIN_POTENTIOMETER);
  // Read IR Sensor value !!!
  a_value = analogRead(PIN_SENSOR);
  // Convert IR sensor value into distance !!!
  dist = 6762.0/((a_value-9)-4.0)*10.0 - 60.0;
  // we need distance range filter here !!!
  if (dist < _DIST_MIN) {
    dist = dist_prev;           // cut lower than minimum
    digitalWrite(PIN_LED, 1);       // LED OFF
  } else if (dist > _DIST_MAX) {
    dist = dist_prev;           // Cut higher than maximum
    digitalWrite(PIN_LED, 1);       // LED OFF
  } else {    // In desired Range
    digitalWrite(PIN_LED, 0);       // LED ON      
    dist_prev = dist;
  }
  // we need EMA filter here !!!
  dist_ema = ALPHA * dist + (1 - ALPHA) * dist_ema;
  duty = (float)(dist_ema-100)*(_DUTY_MAX-_DUTY_MIN)/150.0+_DUTY_MIN;

  // map distance into duty
  // duty = map(a_value, 0, 1023, _DUTY_MIN, _DUTY_MAX);
  
  // myservo.writeMicroseconds(duty);
  if (dist_ema <= _DIST_MIN) {
    myservo.writeMicroseconds(_DUTY_MIN);
  } else if (dist_ema >= _DIST_MAX) {
    myservo.writeMicroseconds(_DUTY_MAX);
  } else {
    myservo.writeMicroseconds(duty);
  }

  // print IR sensor value, distnace, duty !!!
  Serial.print("MIN:");      Serial.print(_DIST_MIN);
  Serial.print(",IR:");      Serial.print(a_value);
  Serial.print(",dist:");    Serial.print(dist);
  Serial.print(",ema");      Serial.print(dist_ema);
  Serial.print(",servo:");   Serial.print(duty);
  Serial.print(",MAX:");     Serial.print(_DIST_MAX);
  Serial.println("");
  // Serial.print("ADC Read: "); Serial.print(a_value);
  // Serial.print(" = ");
  // Serial.print((a_value / 1024.0) * 5.0);
  // Serial.print(" Volt => Duty : ");
  // Serial.print(duty);
  // Serial.println("usec");
}
