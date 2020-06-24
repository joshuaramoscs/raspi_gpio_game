import RPi.GPIO as GPIO
import time

# **** SETUP GPIO ****
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Save LEDs and BUTTONs pin nums in an array for easy manipulation
leds = [17, 18, 27, 22, 23,24, 25, 5, 6, 12, 13, 19]
buttons = [16, 26]

# Setup GPIO OUT (LEDs)
for i in leds:
        GPIO.setup(i, GPIO.OUT, initial=0)

# Setup GPIO IN (BUTTONs)
for i in buttons:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# **** SINGLE LED METHODS ****
# Turns off given LED
def led_off(num):
    GPIO.output(num, 0)

# Turns on given LED
def led_on(num):
    GPIO.output(num, 1)

# Flashes given LED in given seconds and takes bool to toggle last sleep
def led_flash(num, sec, sleep_on):
    led_on(num)
    time.sleep(sec)
    led_off(num)
    if(sleep_on):
        time.sleep(sec)


# **** ALL LEDS METHODS ****
# Turns off all LEDs
def all_led_off(ev=None):
    for i in leds:
        led_off(i)

# Turns on all LEDs
def all_led_on(ev=None):
    for i in leds:
        led_on(i)

# Flashes all LEDs in given seconds and takes bool to toggle last sleep
def all_leds_flash(sec, sleep_on):
    all_led_on()
    time.sleep(sec)
    all_led_off()
    if(sleep_on):
        time.sleep(sec)
    

# Traverses and flashes the LEDs individualy forward
def traverse_led_f(sec):
    for i in leds[1:]:
        GPIO.output(i, 1)
        time.sleep(sec)
        GPIO.output(i, 0)

# Traverses and flashes the LEDs individualy backward
def traverse_led_b(sec):
    for i in reversed(leds[:-1]):
        GPIO.output(i, 1)
        time.sleep(sec)
        GPIO.output(i, 0)


# **** GAME ****
# Start game: True= Blue start, False= Red start
def start_game(blue_start):
    init_speed = .25
    HOLD = .5
    score = False
    # Flash lights to indicate start
    for i in range(4):
        all_leds_flash(speed, True)
    # Hold first led for HOLD seconds, then start
    led_flash(leds[:1], HOLD, False)
    while not score:
        traverse_led_f(speed)
        traverse_led_b(speed)
        #time.sleep(1)
    
    
# **** Main ****
# Detect input events
GPIO.add_event_detect(16, GPIO.FALLING, callback=all_led_on, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=all_led_off, bouncetime=300)

# Start game, Red always starts on first match
blue_start = False
while True:
    start_game(blue_start)
    