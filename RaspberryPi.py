"""In RaspberryPi.py, we control the switch on/off of three thermocouples and RTD"""

from gpiozero import LED
from time import sleep
import threading 

"""
Convention:
Relay 1: GPIO14
Relay 2: GPIO15
Relay 3: GPIO18
Relay 4: GPIO23
Relay 5: GPIO24
Relay 6: GPIO25
Relay 7: GPIO8
Relay 8: GPIO7

"""

# Thermocouple 1
relay1 = LED(14)
relay2 = LED(15)

# Thermocouple 2
relay3 = LED(18)
relay4 = LED(23)

# Thermocouple 3
relay5 = LED(24)
relay6 = LED(25)

# RTD
relay7 = LED(8)
relay8 = LED(7) 

"""
We need to build two threads for three-thermocouples and RTD respectively

"""

def Thermocouple_control(t):
    while True:
        relay1.on()
        relay2.on() 
        sleep(t)

        relay1.off()
        relay2.off()
        relay3.on()
        relay4.on()
        sleep(t)

        relay3.off()
        relay4.off() 
        relay5.on()
        relay6.on()
        sleep(t)

        relay5.off()
        relay6.off()


def RTD_control(T):
    while True:
        relay7.on()
        relay8.on()
        sleep(T)

        relay7.off()
        relay8.off()
        sleep(T) 

Threading1 = threading.Thread(target = Thermocouple_control,args = (1,)) # choose t = 1(second) 
Threading2 = threading.Thread(target = RTD_control,args = (1,)) # choose T = 1(second)

Threading1.start()
Threading2.start() 