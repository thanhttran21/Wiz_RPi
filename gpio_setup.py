import RPi.GPIO as GPIO

# Pin definitions
LED_0_PIN = 2
LED_1_PIN = 3
BUTTON_PIN = 0
SWITCH_EVEN_PIN = 4
SWITCH_ODD_PIN = 5
POT_A_PIN = 25      # TODO: For future potentiometer control
POT_B_PIN = 27      # TODO: For future potentiometer control

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_0_PIN, GPIO.OUT)
    GPIO.setup(LED_1_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_EVEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_ODD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(POT_A_PIN, GPIO.IN)      # TODO: For future potentiometer control
    GPIO.setup(POT_B_PIN, GPIO.OUT)     # TODO: For future potentiometer control
