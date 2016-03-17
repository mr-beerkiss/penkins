emulation = False

if (emulation):
	from display import display as Adafruit_RBGmatrix
else:
	from rgbmatrix import Adafruit_RGBmatrix

import time
import Image

matrix = Adafruit_RGBmatrix(32, 1)

def run():
	matrix.Fill(0x00FF00)
	time.sleep(2.0)
	matrix.Clear()
	
	image = Image.open("jenkins.png")
	image.load()
	for n in range(32, -image.size[0], -1):
		matrix.SetImage(image, n, 1)
		time.sleep(0.1)

def kill():
	matrix.Clear()

if (emulation):
	matrix.start(run, kill)
else:
	run()

