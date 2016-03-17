from display import display as Adadruit_RBGMatrix
import time
import Image

matrix = Adadruit_RBGMatrix(32, 1)

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

matrix.start(run, kill)
