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

