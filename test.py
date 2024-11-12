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

async def toggle_bulbs(bulbs, turn_on, scene=None):
    """Turn on or off bulbs with optional scene setting."""
    tasks = []
    for bulb in bulbs:
        if turn_on:
            if scene is not None:
                task = bulb.turn_on(PilotBuilder(scene=scene))
            else:
                task = bulb.turn_on(PilotBuilder(warm_white=255))
        else:
            task = bulb.turn_off()
        tasks.append(asyncio.create_task(task))
    await asyncio.gather(*tasks)

async def main():
    # Discover WiZ lights on the network
    bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    if bulbs:
        for bulb in bulbs:
            print("Discovered bulb:", bulb.__dict__)

    scene = 0  # Initial scene
    while True:
        # Handle even switch
        if switch_even.is_pressed:
            print("Even switch activated")
            await toggle_bulbs(even_bulbs, turn_on=True)
        else:
            print("Even switch deactivated")
            await toggle_bulbs(even_bulbs, turn_on=False)

        # Handle odd switch
        if switch_odd.is_pressed:
            print("Odd switch activated")
            await toggle_bulbs(odd_bulbs, turn_on=True)
        else:
            print("Odd switch deactivated")
            await toggle_bulbs(odd_bulbs, turn_on=False)

        # Handle button press
        if button.is_pressed:
            print("Button pressed")
            scene = (scene + 1) % 4
            leds[0].value = scene & 1
            leds[1].value = (scene >> 1) & 1
            await toggle_bulbs(even_bulbs + odd_bulbs, turn_on=True, scene=SCENES[scene])
            await asyncio.sleep(0.1)  # Debounce delay

        await asyncio.sleep(0.1)  # Non-blocking polling interval for switch and button state

# Run the asyncio event loop
asyncio.run(main())