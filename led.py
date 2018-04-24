#Encender Leds por teclado

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)

while(True):

	teclado= input("'a' encendido, 'b' apagado:")

	if teclado == "a":
		GPIO.output(5,True)
	if teclado == "b":
		GPIO.output(5,False)

GPIO.cleanup()
