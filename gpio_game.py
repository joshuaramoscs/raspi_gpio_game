import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(5):
	GPIO.output(17, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(17, GPIO.LOW)
	time.sleep(.1)

led_on = False
def switch(ev=None):
	global led_on
	led_on = not led_on
	GPIO.output(17, GPIO.HIGH if led_on else GPIO.LOW)

GPIO.add_event_detect(18, GPIO.FALLING, callback=switch, bouncetime=300)

while True:
	time.sleep(1)
