# Pokemon Hackpad!
<!---
![picture of pokemon hackpad](assets/photo.png)
picture to come!
-->
[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2Fsahilchess%2FPokemon-Hackpad%2Ftree%2Fmain%2FPCB)


<img width="auto" height="50" alt="kicad" src="assets/icons/kicad_icon.png" /> <img width="auto" height="50" alt="onshape" src="assets/icons/onshape_icon.png" /> [![things used](https://skillicons.dev/icons?i=py,github,vscode,windows)](https://skillicons.dev)

Pokemon Hackpad is a 5 key macropad with a rotary switch/encoder, and 4 SK6812 MINI E RGB LEDs. It uses KMK/QMK firmware
I designed this as my own macropad through [hackpad](https://hackclub.hackpad.com), a Hack Club program where you learn to design your own macropad and get it for free

## Features:
- An EC11 rotary encoder, controls volume, click to mute
- 3 SK6812 MINI E RGB LEDs, swirl and static modes
- 5 Cherry MX style keys
- 128x32 OLED Screen
- Pokemon themed design

## CAD Model:
Here is the case, made in onshape. I used onshape because Fusion basically blew my computer up. 


<img width="1250" height="auto" alt="image" src="https://github.com/user-attachments/assets/d66efd7f-062a-44ae-808a-4c25495436ef" />
<img width="1250" height="auto" alt="image" src="https://github.com/user-attachments/assets/79f80972-4f14-406a-a01a-ce2361633350" />
<img width="1250" height="auto" alt="image" src="https://github.com/user-attachments/assets/909ae86d-40e8-42d0-9a8a-7262f05f65ff" />




## PCB
Here's the PCB, made in KiCad.


<img width="1250" height="auto" alt="image" src="https://github.com/user-attachments/assets/e868651f-b0b2-4760-a1d3-5f7368389428" />
<img width="1250" height="auto" alt="image" src="https://github.com/user-attachments/assets/b562254a-c9d8-4f44-96f8-50fde488c712" />



## Firmware Overview
This hackpad uses [KMK](https://github.com/KMKfw/kmk_firmware) firmware for everything.
- the rotary encoder changes volume, press to mute
- the 5 regular keys are copy, paste, undo, redo
- rgb leds swirl by default, static color available


## BOM (more elaborate BOM [here](http://github.com/sahilchess/Pokemon-Hackpad/blob/main/production/BOM.md)):
Here should be everything you need to make this amazing hackpad
- 5x Cherry MX Switches
- 5x DSA Keycaps
- 6x 1N4148 DO-35 Diodes
- 3x SK6812 MINI E RGB LEDs
- 1x EC11 Rotary Encoder
- 1x 0.91 inch OLED display
- 4x M3x16mm screws
- 4x M3x5mx4mm heatset inserts
- 1x XIAO RP2040

> insert cart image of the cart iykyk
