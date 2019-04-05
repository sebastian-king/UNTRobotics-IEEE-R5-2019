import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)

while True:
	status = GPIO.input(21)
	print("STATUS", status)
	time.sleep(0.1)

GPIO.cleanup()
