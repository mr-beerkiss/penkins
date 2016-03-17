import time
import sys

emulation = False

if ( len(sys.argv) == 2 ):
	emulation = True


if (emulation):
	from display import display as Adafruit_RBGMatrix
else:
	from rgbmatrix import Adafruit_RBGMatrix

matrix = Adafruit_RBGMatrix(32, 1)

def run():
	matrix.Fill(0x00FF00)
	time.sleep(2.0)
	matrix.Clear()

	for y in range(32):
		for x in range(32):
			matrix.SetPixel(x, y, 0, 255, 0)
			time.sleep(0.1)

def kill():
	matrix.Clear()

if ( emulation ):
	matrix.start(run, kill)
else:
	run()

