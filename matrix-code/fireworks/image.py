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
	
	animation = "fireworks"

	for x in range(0, 42):
		image = Image.open(str(x) + ".png")
		image.load()
		matrix.SetImage(image.im.id, 0, 0)
		time.sleep(0.02)

def kill():
	matrix.Clear()

if (emulation):
	matrix.start(run, kill)
else:
	run()

