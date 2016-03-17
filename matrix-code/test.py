import time
from multiprocessing import Process

from screens.TestScreen import TestScreen


def test2():
	myTest = TestScreen(True)
	myTest.start()

#test2()

p1 = Process(target=test2)
p1.start()

time.sleep(8)

p1.terminate()
