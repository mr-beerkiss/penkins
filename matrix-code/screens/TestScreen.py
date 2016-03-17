import time
from MatrixPanel import MatrixPanel

class TestScreen(MatrixPanel):
	def startLoop(self):
		self.matrix.Fill(0x0000FF)
		time.sleep(2.0)
		self.matrix.Clear()

		for y in range(32):
			for x in range(32):
				self.matrix.SetPixel(x, y, 0, 0, 255)
				time.sleep(0.025)

		self.matrix.Clear()
		return

