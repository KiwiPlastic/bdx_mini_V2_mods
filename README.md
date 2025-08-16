BDX-Mini V2 LCD EYES mods and Assembly Notes

This mod uses LCDs as eyes. Allowing the Xbox controller to convae expressions 
It also uses a lipo battery 3S-4S and BEC. No BMS

Parts
2 x LCD displays
1 x ESP32C
1 x 25/50amp BEC

The Pi Zero connects to the ESP32C via a 5 bit bus. This allows a range of 0-31 decamal. LCD Commands(Expresions)

Four file have been modified to make this work

- eyes.pi
- buttons.py
- xboxcontroler.py
- head_puppet.py

xboxcontroler.py now reads all xbox button and the dpad. It will print out any button presses. combos can be 

- Michel Aractingi
- Mankaran Singh
- Steve N'Guyen
- Pierre Rouanet
- Thomas Wolf
