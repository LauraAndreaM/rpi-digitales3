import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)

ipAddress = '192.168.43.46'
response = 0

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
# and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    #if pingstatus == "Network Error":  
     # while(True):
        GPIO.output(7,True)
        time.sleep(1)
        GPIO.output(7,False)
        time.sleep(1)
       # break
   

    return pingstatus


if __name__ == "__main__":
	while(True):   
		pingstatus = check_ping(ipAddress)
		print pingstatus
