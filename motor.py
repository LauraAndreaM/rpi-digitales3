#Control de los motores...

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

pwm1 = GPIO.PWM(23, 50)
pwm2 = GPIO.PWM(24, 50)

while(True):
	teclado= input("Ingrese = '1' adelante, '2' atras, '3' derecha, '4' izquierda, 'c' parar:")

	if teclado == 1:
		GPIO.output(4,True)
		GPIO.output(27,True)
		GPIO.output(17,False)
		GPIO.output(22,False)
		pwm1.start(100)
		pwm2.start(100)

	if teclado == 2:
		GPIO.output(4,False)
		GPIO.output(27,False)
		GPIO.output(17,True)
		GPIO.output(22,True)
		pwm1.start(50)
		pwm2.start(50)

	if teclado == 3:
		GPIO.output(4,True)
		GPIO.output(27,False)
		GPIO.output(17,False)
		GPIO.output(22,True)

	if teclado == 4:
		GPIO.output(4,False)
		GPIO.output(27,True)
		GPIO.output(17,True)
		GPIO.output(22,False)

	if teclado == "c":
		GPIO.output(4,False)
		GPIO.output(27,False)
		GPIO.output(17,False)
		GPIO.output(22,False)
GPIO.cleanup()
