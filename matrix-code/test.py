import Image
import ImageDraw

from display import display as Adadruit_RBGMatrix

width = 64
height = 32
matrix = Adadruit_RBGMatrix(32, 2)
fps = 20

image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)

print image

def run():
	while True:

		draw.rectangle((0, 0, width, height), fill=(255, 0, 0))
		matrix.SetImage(image, 0, 0)

		time.sleep(1)

def kill():
	print "Kill command"
	matrix.Clear()

matrix.start(run, kill)