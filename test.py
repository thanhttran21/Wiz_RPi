"""
    Test if UDP communication is one-way or two-way. If one-way, we're good. If two-way. scrap the project.

    Procedure:
    1. Run script to turn on light
    2. Turn off light using phone app
    3. See if light turns on again from script
    4. Try with other commands
"""
import time
from wiz_api.wiz import Light

IP = '192.168.1.10'  # replace with your Wiz's IP address

print("Testing...")

light = Light(IP)
while True:
    print("Off")
    light.off()
    time.sleep(2)
    print("On")
    light.on()
    light.scene(4)
    time.sleep(2)
    