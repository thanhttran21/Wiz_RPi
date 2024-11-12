from gpiozero import LED, Button, DigitalInputDevice
import time

switch_even = Button(18)

while True:
    print("Waiting...")
    if switch_even.is_pressed:  # Replace with actual logic
        print("Even switch activated")
    else:
        print("Even switch deactivated")
    time.sleep(0.1)

    
