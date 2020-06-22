import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup GPIO OUT
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

#Setup GPIO IN
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Speed
speed = .05

for i in range(5):
	GPIO.output(17, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(17, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(18, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(18, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(27, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(27, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(22, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(22, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(23, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(23, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(24, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(24, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(25, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(25, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(5, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(5, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(6, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(6, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(12, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(12, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(13, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(13, GPIO.LOW)
	time.sleep(speed)

	GPIO.output(19, GPIO.HIGH)
	time.sleep(speed)
	GPIO.output(19, GPIO.LOW)
	time.sleep(speed)

led_on = False
def switch(ev=None):
	global led_on
	led_on = not led_on
	GPIO.output(17, GPIO.HIGH if led_on else GPIO.LOW)

GPIO.add_event_detect(16, GPIO.FALLING, callback=switch, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=switch, bouncetime=300)

while True:
	time.sleep(1)

