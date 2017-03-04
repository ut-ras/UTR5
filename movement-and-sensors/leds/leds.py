#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# echo 11 > /sys/class/gpio/unexport
ON = int(sys.argv[1]) # 1 = ON, 0 = OFF

GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)

if ON == 1:
	GPIO.output(25, GPIO.LOW)
else:
	GPIO.output(25, GPIO.HIGH)

#GPIO.cleanup()
