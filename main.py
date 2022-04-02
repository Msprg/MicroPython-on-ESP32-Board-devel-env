import machine
from machine import Pin, ADC, PWM, Signal
import time

#===========SAFETY_DELAY===========#
if (machine.reset_cause() == 1):
  print("You have time to halt NOW!")
  print("       (use ctrl+c)")
  time.sleep_ms(4000)
#===========SAFETY_DELAY===========#


#LED-ky a tlačidlá inicializované pomocou abstrakčnej vrstvy "Signal"
# Vďaka nej je možné bool invertovať v SW.
# To znamená, že ak si ich zadefinujete nasledovne, 
# tak vám ledky budú svietiť pri logickej "1", a na tlačidlách prečítate logickú "1" v čase keď budú stlačené.
# (Čiže tak ako to intuitívne dáva zmysel)

#Nevýhoda Signal-u je, že neumožňuje PWM, takže pre ledky ho budete používať len ak ich nebudete chcieť stmievať.


#BLUEIO = Signal(Pin(26, Pin.OUT, value=1, drive=Pin.DRIVE_0), invert=True) // drive=Pin.DRIVE_0 neexistuje(?)
BLUEIO = Signal(Pin(26, Pin.OUT, value=1), invert=True)
GREENIO = Signal(Pin(14, Pin.OUT, value=1), invert=True)
REDIO = Signal(Pin(27, Pin.OUT, value=1), invert=True)
USRBTNIO = Signal(Pin(13, Pin.IN, Pin.PULL_UP), invert=True)
BOOTBTNIO = Signal(Pin(0, Pin.IN, Pin.PULL_UP), invert=True)


#Header 4
# Tu sú základné definície pinov z headeru.
# (tie veci čo trčia z PCB - označené myslím K2 - "tie dole / na spodnej časti")

PWM1A = Pin(16, Pin.OUT)
PWM1B = Pin(19, Pin.OUT)
PWM2A = Pin(17, Pin.OUT)
PWM2B = Pin(18, Pin.OUT)
OPT2 = Pin(34, Pin.IN)
OPT3 = Pin(35, Pin.IN)
SLEEPIO = Pin(21, Pin.IN)


#Akustika
# PWM definíca pre akustickú signalizáciu (bzučiak).
# Na začiatku je PWM nastavené na 50% duty takže ho hneď po definícií dáme na nulu.
# To sa síce dá aj rovno v konštruktore, ale to v minulosti spôsobovalo problémy (duty sa nedal prestaviť na inú hodnotu).
# To občas napriek tomu spôsobí nejaký zvuk, ale to už nemá zmysel riešiť.

AKUPWM = PWM(Pin(5))
AKUPWM.duty(0)


#Fotorezistor
# Fotorezistor je pripojený cez LNA ku špečiálnym pinom ktoré sú schopné merať analógové napätia (až do MAXabs 3,6V)
# Preto ideálne použijeme konštruktor ADC - Analógovo-Digitálneho prevodníka. 
# Tento je nám schopný vracať nie len digitálne hodnoty ("1"/"0") ale naozaj analógové napätie, 
# respektíve celú škálu od ~0V do (ideálne) ~3v3. Aleaspoň v rámci možností presnosti a rozlíšenia.

FOTORES = ADC(Pin(39)) #sensVN is LNA as INPUT-ONLY GPIO39
OPT1 = ADC(Pin(36)) #sensVP is LNA as INPUT-ONLY GPIO36  #ADC Block1 ranges from IO32 to IO39. Don't use other block. See: https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=analog#adc-analog-to-digital-conversion


#(Otestuje si tlačidlá a fotorezistor)
while True:
  print("USRBTN:", str(USRBTNIO.value()))                       # Výstup tlačítka USER - invertovaný
  print("BOOTBTN:", str(BOOTBTNIO.value()))                     # Výstup tlačítka BOOT
                                                                # (Počas behu programu ho môžeme normálne používať) - invertovaný 
  GREENIO.value(USRBTNIO.value())                               # Zelená!  - SVIETI PRI STLAČENÍ USRBTN  - POZOR NA OČI!
  REDIO.value(BOOTBTNIO.value())                                # Červená! - SVIETI PRI STLAČENÍ BOOTBTN - POZOR NA OČI!
  # print("Fotorezistor - mikroVolty:", str(FOTORES.read_uv())) # Hodnota LNA ADC fotorezistora v uV / mikroVoltoch - KALIBROVANÁ
                                                                # Bohužiaľ read_uv() nemôžeme použiť - máme na to príliš starú verziu FW.
  print("Fotorezistor - RAW:", str(FOTORES.read_u16()))         # Hodnota LNA ADC fotorezistora RAW  -  0 až 65 535 - NEKALIBROVANÁ!
                                                                # (~65 535 = tma; ~10 000 = je deň; ~0 = čas na slečné okuliare 😎)
  time.sleep_ms(100)                                            # Cut the CPU some slack, will ya?