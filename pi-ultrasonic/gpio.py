#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 22

GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)
