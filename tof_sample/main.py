#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.iodevices import I2CDevice

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
tof = I2CDevice(Port.S1,0x02>>1)

# Write your program here.
ev3.speaker.beep()

while True:
    results = tof.read(0x42, 2)
    distMM = results[0] + (results[1]<<8)

    print(distMM)
    wait(500)
