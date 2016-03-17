import time, sys

from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import UnknownJob
from rgbmatrix import Adafruit_RGBmatrix

import Image

matrix = Adafruit_RGBmatrix(32, 1)

last_status = 'None'

def runSuccess():
	matrix.Clear()
	animation = "fireworks"
	for x in range(0, 42):
		image = Image.open(str(x) + ".png")
		image.load()
		matrix.SetImage(image.im.id, 0, 0)
		time.sleep(0.05)

def runFailure():
	matrix.Clear()
	image = Image.open("failure.png")
	image.load()
	matrix.SetImage(image.im.id, 0, 0)
	time.sleep(0.05)

def runAborted():
	matrix.Clear()
	image = Image.open("aborted.png")
	image.load()
	matrix.SetImage(image.im.id, 0, 0)
	time.sleep(0.05)

def runRunning():
	matrix.Clear()
	image = Image.open("running.png")
	image.load()
	matrix.SetImage(image.im.id, 0, 0)
	time.sleep(0.05)

def get_dummy_build_info(jenkins, job_name):
	try:
		job = jenkins.get_job(job_name)
	except UnknownJob:
		print 'Job does not exist: ', job_name
		sys.exit(2)

	build = job.get_last_build()
	if build == None:
		print 'Cannot retrieve build information'
	else:
		status = build.get_status()
		if status != last_status:
			if status == 'SUCCESS':
				print 'SUCCESS'
				runSuccess()
			elif status == 'ABORTED':
				print 'Aborted'
				runAborted()
			elif status == 'FAILURE':
				print 'Failure'
				runFailure()
			elif status == None and build.is_running():
				print 'Running'
				runRunning()
			else:
				print 'Unknown status'
			last_status = status

if __name__ == '__main__':
	if len(sys.argv) != 9 :
		print 'Error. Usage: '
		print ' python jenkins.py -u <username> -t <token> -j <job_name> -r <refresh_interval_in_seconds>'
		sys.exit(2)
	else:
		username = str(sys.argv[2])
		token = str(sys.argv[4])
		job_name = str(sys.argv[6])
		refresh_interval_in_seconds = str(sys.argv[8])

	jenkins_url = 'http://ci.boxtop.photobox.com'
	jenkins = Jenkins(jenkins_url, username = username, password = token)

	while 1==1:
		get_dummy_build_info(jenkins, job_name)
		time.sleep(float(refresh_interval_in_seconds))
