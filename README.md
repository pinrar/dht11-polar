# dht11-polar

The Python code plots live data from a DHT11 temperature/humidity sensor. Uses polar coordinates where theta = time, radius 1 & 2 = temperature and humidity that are scaled to 0-1. The aim is to draw a flower on the plot by blowing on the sensor and increasing humidity at regular intervals.

![Figure](https://github.com/pinrar/dht11-polar/blob/master/Figure_3.png)

## Hardware:
* Arduino Uno
* DHT-11
* 1 x 4.7 kOhm resistor

## Libraries:
### Arduino:
* DHT.h

### Python:
* pySerial
