import sensorsLib as sen
import time

while True:
  soil = sen.moisture()
  print(f'Moisture: {soil['percent']}')
  time.sleep(1)
