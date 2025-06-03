#include <SoftwareSerial.h>
SoftwareSerial scaleSerial(D7, D8); // RX, TX

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  scaleSerial.begin(9600);
}

void loop() {
  if (scaleSerial.available()) {
    digitalWrite(LED_BUILTIN, LOW); // Turn on LED
    String data = scaleSerial.readStringUntil('\n');
    Serial.println(">> " + data);
    delay(100);
    digitalWrite(LED_BUILTIN, HIGH); // Turn off LED
  }
}
