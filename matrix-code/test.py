import time
from multiprocessing import Process
from MatrixPanel import MatrixPanel

class TestImpl(MatrixPanel):
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


def test2():
	myTest = TestImpl(False)
	myTest.start()

#test2()

p1 = Process(target=test2)
p1.start()

time.sleep(8)

p1.terminate()
