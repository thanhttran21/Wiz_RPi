import time
import RPi.GPIO as GPIO
from gpio_setup import setup_gpio, SWITCH_EVEN_PIN, SWITCH_ODD_PIN
from button_handler import check_button_press
from light_controller import control_lights
from potentiometer import analog_read

def main():
    setup_gpio()

    state = 0
    last_button_state = GPIO.HIGH
    last_press_time = time.time()

    try:
        print('Start...')

        while True:
            # Print potentiometer value. TODO: Add potentiometer control for light intensity
            pot_intensity = analog_read()
            print(pot_intensity)

            # Handle button press and update state
            state, last_button_state, last_press_time = check_button_press(state, last_button_state, last_press_time)

            # Check switch states
            switch_even_state = GPIO.input(SWITCH_EVEN_PIN)
            switch_odd_state = GPIO.input(SWITCH_ODD_PIN)

            # Control lights based on switch states and current state. TODO: Add potentiometer control for light intensity
            control_lights(state, switch_even_state, switch_odd_state)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print('Finish...')
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
