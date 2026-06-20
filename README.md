# Pokemon Hackpad!
<!---
![picture of pokemon hackpad](assets/photo.png)
picture to come!
-->
[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2Fsahilchess%2FPokemon-Hackpad%2Ftree%2Fmain%2FPCB)


<img width="auto" height="50" alt="kicad" src="icons/kicad_icon.png" /> <img width="auto" height="50" alt="onshape" src="icons/onshape_icon.png" /> [![things used](https://skillicons.dev/icons?i=py,github,vscode,windows)](https://skillicons.dev)

Pokemon Hackpad is a 5 key macropad with a rotary encoder, and 4 SK6812 MINI E RGB LEDs. It uses KMK firmware
I designed this as my own macropad through [hackpad](https://hackclub.hackpad.com), a Hack Club program where you learn to design your own macropad and get it for free

## Features:
- An EC11 rotary encoder, controls volume, click to mute
- 4 SK6812 MINI E RGB LEDs, swirl and static modes
- 5 Cherry MX style keys, encoder click counts as the 5th
- Pokemon themed design

## CAD Model:
Here is the case, made in onshape. I used onshape because Fusion basically blew my computer up. 


<img width="1200" height="auto" alt="Screenshot 2026-06-19 203712" src="https://github.com/user-attachments/assets/fb6f2749-015e-42a0-bc19-9505587f072d" />
<img width="1200" height="auto" alt="Screenshot 2026-06-19 203446" src="https://github.com/user-attachments/assets/1766e97e-77c3-48db-8a26-7c8a7ceed4cf" />



## PCB
Here's the PCB, made in KiCad.


<img width="1200" height="auto" alt="Screenshot 2026-06-19 202901" src="https://github.com/user-attachments/assets/977bb936-ffad-4c0d-ba2f-5762bcd1ee64" />
<img width="1200" height="auto" alt="Screenshot 2026-06-19 202941" src="https://github.com/user-attachments/assets/6c2b435f-7777-4178-bf75-753200a51a80" />


## Firmware Overview
This hackpad uses [KMK](https://github.com/KMKfw/kmk_firmware) firmware for everything.
- the rotary encoder changes volume, press to mute
- the 4 regular keys are copy, paste, undo, redo
- rgb leds swirl by default, static color available


## BOM:
Here should be everything you need to make this amazing hackpad
- 5x Cherry MX Switches
- 5x DSA Keycaps
- 6x 1N4148 DO-35 Diodes
- 4x SK6812 MINI E RGB LEDs
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
<img width="1200" height="auto" alt="Screenshot 2026-06-19 205248" src="https://github.com/user-attachments/assets/7de9fb8e-3e22-494f-b4e1-6dfbed8f962a" />
