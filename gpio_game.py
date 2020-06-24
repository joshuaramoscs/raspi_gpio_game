import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup GPIO OUT
GPIO.setup(17, GPIO.OUT, initial=0) #Red LED
GPIO.setup(18, GPIO.OUT, initial=0)
GPIO.setup(27, GPIO.OUT, initial=0)
GPIO.setup(22, GPIO.OUT, initial=0)
GPIO.setup(23, GPIO.OUT, initial=0)
GPIO.setup(24, GPIO.OUT, initial=0)
GPIO.setup(25, GPIO.OUT, initial=0)
GPIO.setup(5, GPIO.OUT, initial=0)
GPIO.setup(6, GPIO.OUT, initial=0)
GPIO.setup(12, GPIO.OUT, initial=0)
GPIO.setup(13, GPIO.OUT, initial=0)
GPIO.setup(19, GPIO.OUT, initial=0) #Blue LED

# Setup GPIO IN
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Save LED numbers in an array
leds = [17, 18, 27, 22, 23,24, 25, 5, 6, 12, 13, 19]

# Flashes all LEDs on and off in "s" seconds
def all_leds_flash(s):
    all_led_on()
    time.sleep(s)
    all_led_off()
    time.sleep(s)

# Turns on all LEDs
def all_led_on(ev=None):
    GPIO.output(17, 1)
    GPIO.output(18, 1)
    GPIO.output(27, 1)
    GPIO.output(22, 1)
    GPIO.output(23, 1)
    GPIO.output(24, 1)
    GPIO.output(25, 1)
    GPIO.output(5, 1)
    GPIO.output(6, 1)
    GPIO.output(12, 1)
    GPIO.output(13, 1)
    GPIO.output(19, 1)

# Turns off all LEDs
def all_led_off(ev=None):
    GPIO.output(17, 0)
    GPIO.output(18, 0)
    GPIO.output(27, 0)
    GPIO.output(22, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    GPIO.output(25, 0)
    GPIO.output(5, 0)
    GPIO.output(6, 0)
    GPIO.output(12, 0)
    GPIO.output(13, 0)
    GPIO.output(19, 0)

# Detect input event
GPIO.add_event_detect(16, GPIO.FALLING, callback=all_led_on, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=all_led_off, bouncetime=300)

# Speed in seconds
speed = .25
for i in range(4):
    all_leds_flash(speed)

for i in leds:
    GPIO.output(i, 1)
    time.sleep(speed)
    GPIO.output(i, 0)
    
for i in reversed(leds):
    GPIO.output(i, 1)
    time.sleep(speed)
    GPIO.output(i, 0)

#while True:
    #time.sleep(1)

