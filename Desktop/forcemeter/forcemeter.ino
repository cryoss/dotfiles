#include <HX711.h>
#define LOADCELL_DOUT_PIN 3
#define LOADCELL_SCK_PIN 2
HX711 loadcell;
void setup() {
Serial.begin(9600);
// 3. Initialize library
loadcell.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
loadcell.set_scale(85.731);
Serial.println("tare now");
loadcell.tare(10);
delay(1000);
Serial.println("tare done");


}
void loop() {
float a;
//Serial.print(loadcell.get_units(1));
//Serial.println("g");
a=loadcell.get_units(10);
Serial.print(a*0.00981);
Serial.print(",");
//Serial.print(" N ");
Serial.println(a);
//Serial.println(" g");
}
