# Tesseract OCR with the PiCamera
How to take a photo with the Raspberry Pi Camera V2.1 and use pytesseract OCR to read that picture.

## Dowloads and Libraries
You will need to install 3 things:
- Tesseract OCR
- pytesseract the Python Library 
- picamera antother Python Library.
- OpenCV

### Tesseract
Tesseract is the heavy lifter of this program.
It performs the Optical Character Recognition on images.
In order to work it needs to be installed.
Further more to get it to run in Python it also requires a library.
To install it run the command:
`sudo apt-get install tesseract-ocr`

### PIP
In order to install the pytesseract library I used pip, the python package installer.
`sudo apt install python3-pip`

### pytesseract
Now to install the pytesseract I used pip3 and rand the command:
`pip3 install pytesseract`
From here you can run OCR on locally saved images.

### picamera
In order to use the camera in python (just the picamera, no other camera)
You need to install the picamera library with:
`sudo apt-get install python3-picamera`

### Nice to have photo viewer in PI OS Lite:
I also found a command line program that can view images.
To install it you can use the command:
`sudo apt-get -y install fbi`
To use the program you can use the command:
`fbi example.jpg`
The photo's path can be entered if you are not in the correct directory.
There is also zoom commands inside the viewr and you can press h for help and q for exit.

### OpenCV
In order to perform pre-procceing on the images before they are given to the Tesseract I used OpenCV.
This can be install with the command:
`sudo apt install python3-opencv`
