import RPi.GPIO as GPIO

# Pin definitions
BUTTON_PIN = 0
LED_0_PIN = 2
LED_1_PIN = 3
SWITCH_EVEN_PIN = 4
SWITCH_ODD_PIN = 5
POT_PIN = 20    # TODO: For future potentiometer control

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_0_PIN, GPIO.OUT)
    GPIO.setup(LED_1_PIN, GPIO.OUT)
    GPIO.setup(SWITCH_EVEN_PIN, GPIO.IN)
    GPIO.setup(SWITCH_ODD_PIN, GPIO.IN)
    GPIO.setup(POT_PIN, GPIO.IN)  # TODO: For future potentiometer control
