import RPi.GPIO as GPIO
import time
from gpio_setup import POT_A_PIN, POT_B_PIN

def discharge():
    GPIO.setup(POT_A_PIN, GPIO.IN)
    GPIO.setup(POT_A_PIN, GPIO.OUT)
    GPIO.output(POT_B_PIN, False)
    time.sleep(0.004)

def charge_time():
    GPIO.setup(POT_B_PIN, GPIO.IN)
    GPIO.setup(POT_A_PIN, GPIO.OUT)
    count = 0
    GPIO.output(POT_A_PIN, True)
    while not GPIO.input(POT_B_PIN):
        count = count + 1
    return count

def analog_read():
    discharge()
    return charge_time()