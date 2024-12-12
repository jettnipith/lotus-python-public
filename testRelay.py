import actuators as act
import time

while True:
  act.relayOn(1)
  act.relayOff(2)
  time.sleep(1)
  act.relayOn(2)
  act.relayOff(1)
  time.sleep(1)
