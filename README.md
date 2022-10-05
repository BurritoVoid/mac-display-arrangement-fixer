# Mac Display Arrangement Fixer

*A ridiculous solution to a stupid problem*

A set of scripts and a Keyboard Maestro automation to check if external displays for my Macbook need to be swapped.

## Requirements
- Raspberry Pi
    - [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/) (I used Lite/64 bit)
    - Configure passwordless SSH between the Pi and Macbook
- [Raspberry Pi Camera Module](https://www.amazon.com/dp/B012QRGUCQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Keyboard Maestro](https://www.keyboardmaestro.com)
    - ["Execute a script in terminal" action](https://forum.keyboardmaestro.com/t/execute-a-script-in-terminal/4853/6)
- [DisplayPlacer](https://github.com/jakehilborn/displayplacer)

## Remote script
- Deploy remote directory to a raspberry pi with camera module attached
- Install OpenCV2 (Instructions [here](https://raspberrytips.com/install-opencv-on-raspberry-pi/))
- Install Picamera2 (Still in beta, instructions [here](https://pypi.org/project/picamera2/))
- Install dependencies `pip install -r ./requirements.txt`

## Local script
- Put `blue.png` and `swapDisplays.py` anywhere, make sure the script is executable

## Keyboard Maestro script
- Import macro into KM `File -> Import -> Import Macros Safely`
- Configure all values in actions highlighted in orange
- Enable and configure however you want to trigger it

## Camera Mount
Included STL file is for a basic mounting strip that can hold the linked Pi camera. I have mine taped to the monitor.