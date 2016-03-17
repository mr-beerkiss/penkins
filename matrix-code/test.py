import time
import sys

from multiprocessing import Process

from screens.TestScreen import TestScreen

emulation = False

if (len(sys.argv) > 1):
	emulation = True


def test2():
	myTest = TestScreen(emulation)
	myTest.start()

#test2()

p1 = Process(target=test2)
p1.start()

time.sleep(8)

p1.terminate()
