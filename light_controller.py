import asyncio
from pywizlight import wizlight, PilotBuilder, discovery
from gpio_setup import SWITCH_EVEN_PIN, SWITCH_ODD_PIN

SCENES = {
    0: 11,  # 'Warm white'
    1: 6,   # 'Cozy'
    2: 18,  # 'TV time'
    3: 4    # 'Party'
}

# TODO: Assign static IP addresses
BULB_0_IP = '192.168.1.10'
BULB_1_IP = '192.168.1.11'
BULB_2_IP = '192.168.1.12'
BULB_3_IP = '192.168.1.13'

# LIGHTS_EVEN = [wizlight(BULB_0_IP), wizlight(BULB_2_IP)]

LIGHTS_EVEN = [wizlight(BULB_0_IP)]
LIGHTS_ODD = [wizlight(BULB_1_IP), wizlight(BULB_3_IP)]

# TODO: Add potentiometer control for light intensity
async def control_lights(scene, switch_even_state, switch_odd_state):
    tasks = []
    if switch_even_state:
        tasks += [bulb.turn_on(PilotBuilder(scene=SCENES[scene])) for bulb in LIGHTS_EVEN]
    else:
        tasks += [bulb.turn_off() for bulb in LIGHTS_EVEN]

    if switch_odd_state:
        tasks += [bulb.turn_on(PilotBuilder(scene=SCENES[scene])) for bulb in LIGHTS_ODD]
    else:
        tasks += [bulb.turn_off() for bulb in LIGHTS_ODD]

    # Run all turn_on coroutines concurrently
    await asyncio.gather(*tasks)
