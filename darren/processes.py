from multiprocessing import Process

import time

def even():
	time.sleep(1)
	for x in range(15):
		if ( x % 2 == 0):
			print "Next even: " + str(x)
			time.sleep(0.02)

def odd():
	time.sleep(1)
	for x in range(15):
		if ( x % 2 > 0):
			print "Next odd: " + str(x)
			time.sleep(0.05)

p1 = Process(target=even)

p2 = Process(target=odd)

p1.start()
p2.start()

print "Processes starting soon"