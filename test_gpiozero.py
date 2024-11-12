from gpiozero import LED, Button, DigitalInputDevice
import time

switch_even = DigitalInputDevice(4)

while True:
    if switch_even.when_activated:  # Replace with actual logic
        print("Even switch activated")
    time.sleep(0.1)

    