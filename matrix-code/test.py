#import Image
#import ImageDraw
from PIL import Image, ImageDraw

from display import display as Adadruit_RBGMatrix
import time

width = 64
height = 32
matrix = Adadruit_RBGMatrix(32, 2)
fps = 20

currentTime = 0.0
prevTime = 0.0

print "Width: ", width
print "Height: ", height


image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)

def run():
	while True:

		global prevTime

		draw.rectangle((0, 0, width, height), fill=(255, 0, 0))

		
		currentTime = time.time()
		timeDelta = (1.0/fps) - (currentTime - prevTime)

		if(timeDelta > 0.0):
			time.sleep(timeDelta)
		prevTime = currentTime

		matrix.SetImage(image, 0, 0)


def kill():
	print "Kill command"
	matrix.Clear()

time.sleep(5)
matrix.start(run, kill)