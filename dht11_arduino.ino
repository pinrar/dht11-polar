#include "DHT.h"
#define DHT11_PIN 4 

float temp;
float hum;

DHT dht(4, 11);

void setup()
{
  Serial.begin(9600);  

    dht.begin();
}

void loop()
{
    //int chk = DHT.read11(DHT11_PIN);
    
    hum = dht.readHumidity();
    temp = dht.readTemperature();
    Serial.print(temp);
    Serial.print("x");
    Serial.println(hum);
    delay(2000);  
}
