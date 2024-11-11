import asyncio
import time
import RPi.GPIO as GPIO
from pywizlight import wizlight, PilotBuilder, discovery
from gpio_setup import setup_gpio, SWITCH_EVEN_PIN, SWITCH_ODD_PIN
from button_handler import check_button_press
from light_controller import control_lights
from potentiometer import analog_read

async def read_gpio_input(pin):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, GPIO.input, pin)

async def main():
    setup_gpio()

    scene = 0
    last_button_state = GPIO.HIGH
    last_press_time = time.time()
    
    # Discover all bulbs in the network via broadcast datagram (UDP)
    bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    
    # Check if any bulbs are found
    if bulbs:
        # Iterate over all returned bulbs
        for bulb in bulbs:
            print(bulb.__dict__)
            # Uncomment if you want to turn off all bulbs
            # await bulb.turn_off()

    while True:
        # Handle button press and update state
        # scene, last_button_state, last_press_time = check_button_press(scene, last_button_state, last_press_time)

        # Check switch states
        print("before")
        switch_even_state = await read_gpio_input(SWITCH_EVEN_PIN)
        switch_odd_state = await read_gpio_input(SWITCH_ODD_PIN)
        print("after")

        print(f'Scene: {scene}')
        print(f'Switch even state: {switch_even_state}')
        print(f'Switch odd state: {switch_odd_state}')

        scene = 0

        # Control lights based on current scene and switch states. TODO: Add potentiometer control for light intensity
        await control_lights(scene, switch_even_state, switch_odd_state)

        await asyncio.sleep(0.2)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
