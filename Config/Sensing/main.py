# standard imports
from time import sleep

# local imports
from utilities.mqtt_out import publish
from hardware.ICs.ens160 import ENS160

# setup sensors and models
myens160 = ENS160()

# sensing loop
while True:
    sleep(1)
    publish( {"machine": "MachineNameHere"} | myens160.sample() )