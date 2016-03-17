# penkins
Photobox Hackathon 2016

The goal of Penkins is to control the output an Ada Fruit RGB Matrix via a Raspberry PI.  

The output will initially be based around Jenkins builds.  

We require:

-  Code to send display data to the RGB Matrix (Python/C)
-  Code to hook into Jenkins and relay the events to the subsystem powering the Matrix (Node, of course :p)

See [this link](https://dl.dropboxusercontent.com/u/1974667/storyboard.pdf) for an example Storyboard of how this might look.

If you wish to make some changes to the storyboard, please use [this link](https://drive.google.com/a/photobox.com/file/d/0B7geq-WIbw-2alJNMUtPdVRTZzQ/view?usp=sharing).  Note that you will need to link [Draw.io](https://www.draw.io/) your Google Account in order to edit.

## Resources

-  [Library](https://github.com/hzeller/rpi-rgb-led-matrix)
-  [Driving the Matrix](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices)
-  [Learn Python](http://www.learnpython.org/)
-  [Python on Code Academy](https://www.codecademy.com/learn/python)
-  [API client of Jenkins API written in Go](https://github.com/yosida95/golang-jenkins)

## How to start

- run commands:
`sudo apt-get install build-essential g++`
`sudo apt-get install python-dev`
`sudo apt-get install python-imaging`
`sudo apt-get install python-tk`
`sudo apt-get install python-imaging-tk`

- you are ready to go:
`python test.py`

## Script retrieving information from Jenkins
There is a Python script that we need to run in order to get real-time information from a jenkins build.

A pre-requisite is to install jenkinsapi for python (and obviously python binaries):

```
sudo easy_install jenkinsapi
```

Usage of the script is the following:

```
python jenkins.py -u <username> -t <token> -j <job_name> -r <refresh_interval_in_seconds>
```

Example:

```
python jenkins.py -u GITHUB_USERNAME -t YOUR_TOKEN -j hackathon-penkins -r 1
```

The API Token can be found in http://ci.boxtop.photobox.com/user/GITHUB_USERNAME/configure

Maybe in the future, we can configure the Jenkins job to be the one sending updates to a webservice running on the Raspberry Pi, instead of having a script querying jenkins every X seconds.
