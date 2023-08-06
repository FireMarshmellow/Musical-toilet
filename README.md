# Musical Toilet: A MellowLabs Project

This repository contains the code and instructions for a unique MellowLabs project: turning a toilet into a musical instrument. This project was made possible by the support of our Patreon community and showcases the use of an ESP32 microcontroller, capacitive touch sensor, and an audio board to create a unique and humorous bathroom experience.

## Project Overview

The project uses an ESP32 microcontroller, chosen for its touch pin feature, which allows it to sense capacitance and function like a button with a single wire. The project also utilizes breadboards, jumper wires, and a copper strip with adhesive backing.

An amplifier and speaker, as well as an audio board, are repurposed to complete the setup. The audio board is connected to a power supply, with each pin corresponding to a different sound effect.

## Code

The code triggers sound effects based on the touch sensor's readings. The sensor normally outputs a value around 500, but when touched, it drops to around 80 or 70. The code is programmed to trigger when the number goes below 100, effectively turning it into a digital on and off switch.

The toilet is programmed to play soothing music for about 10 minutes when someone sits on it. After this period, it plays a passive-aggressive message suggesting that the person has been sitting for too long and should probably get up. After another 10 minutes, it sends an even more passive-aggressive message.

## Challenges

The setup process was not without its challenges. The length of the wire used for the capacitive touch sensor proved to be crucial. If it was too long, touching it would send the value down to lower than zero, causing the code to crash. Also, touching a grounded object, like a radiator, would also crash the code. Therefore, to use the toilet properly, one needed to be isolated from the ground.

## Humorous Twist

The toilet is programmed to randomly decide whether it "wants" or "doesn't want" to be used when the seat is lifted, using an IR sensor to detect the seat's position.

## Conclusion

This project showcases creativity, technical skills, and a good dose of humor. It may not be practical for everyday use, but it certainly makes for an entertaining bathroom experience. Enjoy exploring the code and instructions, and stay tuned for more innovative and