import serial, time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


pwm1 = GPIO.PWM(23,100)
pwm2 = GPIO.PWM(24,100)
pwm1.start(100)
pwm2.start(100)

error_1=0
ui_1=0
#Arduino
Arduino=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=5) 
Arduino.flushInput()

def separar(data):
    if "distancia" in data:
	label = data.split(":")
	dist = float(label[1])
	print "distancia US: " + str(dist)
    	global error_1, ui_1
	kp=3
	kd=0.2
	ki=0.2
	ref=25
	Ts=0.020
	error=(ref - dist)
	up=(kp*error)
	ui=ki*(error)+ui_1*Ts
	ud=(kd/Ts)*(error- (error_1))
	u=up+ui+ud
	print "error:" + str(error)
	print "velocidad" + str(u)
	error_1=error
	ui_1=ui	
	if u >100:
		u=100
	if u <-100:
		u=-100
	if u <0:
		u=abs(u)
		GPIO.output(4,False)
		GPIO.output(27,False)
		GPIO.output(17,True)
		GPIO.output(22,True)
		pwm1.ChangeDutyCycle(u)
		pwm2.ChangeDutyCycle(u)
	elif u >0:
		u=abs(u)
                GPIO.output(4,True)
                GPIO.output(27,True)
                GPIO.output(17,False)
                GPIO.output(22,False)
                pwm1.ChangeDutyCycle(u)
                pwm2.ChangeDutyCycle(u)
	else:
                GPIO.output(4,False)
                GPIO.output(27,False)
                GPIO.output(17,True)
                GPIO.output(22,True)
#                pwm1.start(0)
#                pwm2.start(0)    
#-------------------------MAIN-----------------------------
if __name__ == "__main__":
    print('Inicializando Sensor...')
    while(True):
        try:
        	data_Arduino=Arduino.readline()
		separar(data_Arduino)
        except KeyboardInterrupt:
                print "Algo va mal :^("
                break