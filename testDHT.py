import time
import sensorsLib as sen

while True:
  air = sen.dht11()
  print(f'Temperature: {air['temperature']} celsius')
  time.sleep(1)
  
