import abc

class MatrixPanel:
	__metaclass__ = abc.ABCMeta

	def __init__(self, emulation):
		self.emulation = emulation

		if (self.emulation):
			from display import display as Adafruit_RGBmatrix
		else:
			from rgbmatrix import Adafruit_RGBmatrix

		self.matrix = Adafruit_RGBmatrix(32, 1)

	@abc.abstractmethod
	def startLoop(self):
		"""Provide some info"""
		return

	def exitLoop(self):
		self.matrix.Clear()
		return

	def start(self):
		if (self.emulation):
			#self.process = Process(target=self.matrix.start, args=(self.startLoop, self.exitLoop))
			self.matrix.start(self.startLoop, self.exitLoop)
		else:
			#self.process = Process(target=self.startLoop)
			self.startLoop();

		#self.process.start()
		#self.process.join()

		print "Returning from start"

		return

	def end(self):
		#self.process.terminate()
		self.exitLoop()



