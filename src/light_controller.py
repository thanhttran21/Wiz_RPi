from external.forked_repo import wiz
from src.gpio_setup import SWITCH_EVEN_PIN, SWITCH_ODD_PIN

SCENES = ['Warm white', 'Cozy', 'TV time', 'Party']

# TODO: Assign static IP addresses
BULB_0_IP = '192.168.xx.xxx'
BULB_1_IP = '192.168.xx.xxx'
BULB_2_IP = '192.168.xx.xxx'
BULB_3_IP = '192.168.xx.xxx'

LIGHTS_EVEN = [wiz.Light(BULB_0_IP), wiz.Light(BULB_2_IP)]
LIGHTS_ODD = [wiz.Light(BULB_1_IP), wiz.Light(BULB_3_IP)]

def control_lights(state, switch_even_state, switch_odd_state):
    control_individual_lights(state, switch_even_state, LIGHTS_EVEN)
    control_individual_lights(state, switch_odd_state, LIGHTS_ODD)

def control_individual_lights(state, switch_state, lights):
    if switch_state:
        for light in lights:
            light.scene(SCENES[state])
            light.on()
    else:
        for light in lights:
            light.off()

