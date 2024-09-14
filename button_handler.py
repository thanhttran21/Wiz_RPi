import time
import RPi.GPIO as GPIO
from gpio_setup import BUTTON_PIN

def check_button_press(state, last_button_state, last_press_time):
    button_state = GPIO.input(BUTTON_PIN)
    current_time = time.time()

    if button_state == GPIO.LOW and last_button_state == GPIO.HIGH:
        if current_time - last_press_time > 0.2:  # Debounce check (200ms)
            state = (state + 1) % 4
            last_press_time = current_time

    return state, button_state, last_press_time
