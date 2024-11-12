import asyncio
from gpiozero import LED, Button, DigitalInputDevice
import socket
from pywizlight import wizlight, PilotBuilder, discovery

# GPIO setup for LEDs, button, and switches
led0 = LED(2)                           # LED 0 pin
led1 = LED(3)                           # LED 1 pin
button = Button(0)                      # Button pin
switch_even = Button(18)                # Switch even pin
switch_odd = Button(17)                 # Switch odd pin

# List of bit encoded indicator LEDs
leds = [led0, led1]

# Wiz lights static IP addresses
BULB_0_IP = "192.168.1.10" 
BULB_1_IP = '192.168.1.11'
BULB_2_IP = '192.168.1.12'
BULB_3_IP = '192.168.1.13'

# Initialize WiZ lights
bulb_0 = wizlight(BULB_0_IP)
# bulb_1 = wizlight(BULB_1_IP)
# bulb_2 = wizlight(BULB_2_IP)
# bulb_3 = wizlight(BULB_3_IP)

# List of bulbs for even and odd switches
# even_bulbs = [bulb_0, bulb_2]
# odd_bulbs = [bulb_1, bulb_3]

even_bulbs = [bulb_0]
odd_bulbs = []
# Scenes for WiZ lights. Matches bit encoded button state to corresponding scene number
SCENES = {
    0: 11,  # Warm white
    1: 6,   # Cozy
    2: 18,  # TV time
    3: 4    # Party
}

# Event handler functions for switch events
async def turn_on_even_bulbs():
    print("Even switch activated")
    for bulb in even_bulbs:
        await bulb.turn_on(PilotBuilder(warm_white=255))

async def turn_off_even_bulbs():
    print("Even switch deactivated")
    for bulb in even_bulbs:
        await bulb.turn_off()

async def turn_on_odd_bulbs():
    print("Odd switch activated")
    for bulb in odd_bulbs:
        await bulb.turn_on(PilotBuilder(warm_white=255))

async def turn_off_odd_bulbs():
    print("Odd switch deactivated")
    for bulb in odd_bulbs:
        await bulb.turn_off()

# Attach async functions to switch events
def setup_switch_callbacks():
    switch_even.when_pressed = lambda: asyncio.create_task(turn_on_even_bulbs())
    switch_even.when_released = lambda: asyncio.create_task(turn_off_even_bulbs())
    switch_odd.when_pressed = lambda: asyncio.create_task(turn_on_odd_bulbs())
    switch_odd.when_released = lambda: asyncio.create_task(turn_off_odd_bulbs())

async def handle_button_presses(button, leds, bulbs):
    scene = 0  # Initial scene
    while True:
        await button.wait_for_press()
        print("Button pressed")

        # Change LED state based on the button press
        scene = (scene + 1) % 4  # Cycle through scenes 0-3
        leds[0].value = scene & 1  # Binary state for LED 1
        leds[1].value = (scene >> 1) & 1  # Binary state for LED 2

        # Change scene on bulbs
        for bulb in bulbs:
            await bulb.turn_on(PilotBuilder(scene=SCENES[scene]))

        await asyncio.sleep(0.1)  # Debounce delay

# Main coroutine to discover lights and run tasks concurrently
async def main():
    # Discover WiZ lights on the network
    bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    if bulbs:
        for bulb in bulbs:
            print("Discovered bulb:", bulb.__dict__)

    setup_switch_callbacks()

    # Run button press handling task
    await handle_button_presses(button, leds, even_bulbs + odd_bulbs)

# Run the asyncio event loop
asyncio.run(main())