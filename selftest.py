#Run selftest by simply importing it! 
# It's reccomended to import it manually into RHEL. 
# It's advised against importing it into the main.py! 

import machine
from machine import Pin, PWM, Signal
import time
from utils import constrain

#LED-ky a tlačidlá
GREENIO = Signal(Pin(14, Pin.OUT, value=1), invert=True)
#BLUEIO = Signal(Pin(26, Pin.OUT, value=1, drive=Pin.DRIVE_0), invert=True) // drive=Pin.DRIVE_0 neexistuje(?)
BLUEIO = Signal(Pin(26, Pin.OUT, value=1), invert=True)
REDIO = Signal(Pin(27, Pin.OUT, value=1), invert=True)
USRBTNIO = Pin(13, Pin.IN, Pin.PULL_UP)
BOOTBTNIO = Pin(0, Pin.IN, Pin.PULL_UP)

#Header 4
PWM1A = Pin(16, Pin.OUT)
PWM1B = Pin(19, Pin.OUT)
PWM2A = Pin(17, Pin.OUT)
PWM2B = Pin(18, Pin.OUT)
OPT2 = Pin(34, Pin.IN)
OPT3 = Pin(35, Pin.IN)
SLEEPIO = Pin(21, Pin.IN)

#Akustika
AKUPWM = PWM(Pin(5))
AKUPWM.duty(0)

# time.sleep_ms(100)
# AKUPWM.duty(0)

#Test signal and sleep
print("Test signal, aku and sleep")
AKUPWM.duty(50)
AKUPWM.freq(800)
GREENIO.on()
time.sleep_ms(250)
GREENIO.off()
time.sleep_ms(50)

AKUPWM.freq(1000)
REDIO.on()
time.sleep_ms(250)
REDIO.off()
time.sleep_ms(50)

AKUPWM.freq(1200)
BLUEIO.on()
time.sleep_ms(250)
BLUEIO.off()
AKUPWM.duty(0)
time.sleep_ms(50)

#USE PWM
print("USE PWM")
redPWM = PWM(Pin(27))
redPWM.freq(1000)
redPWM.duty(1023)

#Test red
print("Test red")
for dutyCycle in range(1023,-1, -5):
  redPWM.duty(constrain(dutyCycle, 0, 1023))
  time.sleep_ms(5)



for dutyCycle in range(0,1026, 5):
  redPWM.duty(constrain(dutyCycle, 0, 1023))
  time.sleep_ms(5)



#Discontinue PWM usage and go back to signal
redPWM.deinit()
REDIO = Signal(Pin(27, Pin.OUT, value=1), invert=True)

#USE PWM
greenPWM = PWM(Pin(14))
greenPWM.freq(1000)
greenPWM.duty(1023)

#Test green
print("Test green")
for dutyCycle in range(1023,-1, -5):
  greenPWM.duty(constrain(dutyCycle, 0, 1023))
  time.sleep_ms(5)



for dutyCycle in range(0,1026, 5):
  greenPWM.duty(constrain(dutyCycle, 0, 1023))
  time.sleep_ms(5)



#Discontinue PWM usage and go back to signal
redPWM.deinit()
GREENIO = Signal(Pin(14, Pin.OUT, value=1), invert=True)

#USE PWM
bluePWM = PWM(Pin(26))
bluePWM.freq(1000)
bluePWM.duty(1023)

#Test blue
print("Test blue")
for dutyCycle in range(1023,-1, -5):
  bluePWM.duty(constrain(dutyCycle, 0, 1023))
  time.sleep_ms(5)



for dutyCycle in range(0,1026, 5):
  bluePWM.duty(constrain(dutyCycle, 0, 1023))
  time.sleep_ms(5)



#Discontinue PWM usage and go back to signal
redPWM.deinit()
BLUEIO = Signal(Pin(26, Pin.OUT, value=1), invert=True)


print("===============SELFTEST DONE!===============")
machine.reset()