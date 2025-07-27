  ## **Sentry Safe Bypass Tool for Cardputer**

Credit to echo-lalia for MicroHydra and H4ckdaddy for Sentry Safe research.

SentrySafeCardputer.py is intended to be run in MicroHydra on the M5Stack Cardputer. This program is intended for use in legal, and research situations. I am not responsible for you using this improperly. 

I analyzed the vulnerability info and code by H4ckd4ddy ( [Link](https://github.com/H4ckd4ddy/bypass-sentry-safe "Sentry Safe Bypass by H4ckd4ddy") ), and decided to try writing this attack to the Cardputer using MicroPython.

This program uses the GPIO pins on the left side of the Cardputer, to send UART signals, plus some specially-timed pulses, to reset the PIN on [many] Sentry Safe and Master Lock safes that have digital pin pads on the front. Once the PIN has been reset, the program sends the new PIN to open the safe. Note: I've read that the newer models are not longer vulnerable to this. Your mileage may vary.

This program is intended to help you open your old safe(s) that you lost the PIN to, or other legal 
activities, such as learning and experimenting with your own gear. 

#### Install steps:

> 1. Download MicroHydra for the Cardputer. Makes sure it works in either M5 Launcher, or flash it directly with something like Esptool.

> 2. Download SentrySafeCardputer.py from this Github page.

> 3. Put the .py file into a folder called "apps" on your Cardputer SD card. If an "apps" folder doesn't exist yet, create one. (It should be automatically created the first time you run MicroHydra.)

> 4. Turn on the Cardputer and launch MicroHydra.

> 5. Find SentrySafeCardputer.py on the main menu. Use the arrow keys to find it. Once you've found it, press OK or G0 to launch.

> 6. Follow the on screen instructions (see below).

#### Usage instructions:

> 1. Unscrew any screws found around or under the PIN pad of the safe. Then, twist off the pin pad and pull it back toward you.(If this doesn't work, then try to figure something out on your own.)

> 2. Using GPIO (Dupont) jumper cables, or whatever works, connect the black wire behind the safe's pin pad, to the GND pin on the Cardputer. Connect the green wire behind the safe's pin pad, to the G1 pin on the cardputer. Instructions are also on screen.

> 3. Once everything is connected, press any key on the Cardputer to send the signals. Make sure nothing gets disconnected while it's running. It only takes a few moments for the signal to fully send. It will tell you when it's done on screen.

> 4. Hopefully the safe has been opened. 

 
The Cardputer seems like the ultimate tool, to me, for something like this, due to its screen, internal batteries, and keyboard, allowing it to work as a standalone device. Other microcontroller products may require external power, and have other barriers to utilizing this program effectively.

I used my logic analyzer to make sure the signals being output to the G1 pin of the Cardputer, matched the intended UART signals (and special initial wake up HIGH/LOW timings).

Written by Spaceherb.