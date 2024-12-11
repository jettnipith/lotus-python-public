import time
import sensorsLib as sen

while True:
  air = sen.dht22()
  if air['temperature']:
      print(f'Temperature: {air['temperature']} celsius')
  else:
      print(air)
  time.sleep(1)
  
