import sensorsLib as sen
import motorsLib as mot
import time
from machine import SoftI2C, Pin
import ssd1306
# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

splitterL = (2200+4095)/2
splitterR = (1000+4095)/2

while True:
    
    oled.clear_display()
    sensors = sen.read_two_sensors()
    oled.text('Left:', 0, 0)
    oled.text(str(sensors["sensorL"]), 50, 0)
    oled.text('Right:', 0, 10)
    oled.text(str(sensors["sensorR"]), 50, 10)
    oled.text('Action:', 0, 30)
    l = 2200
    r = 1000
    if sensors["sensorL"] > splitterL and sensors["sensorR"] > splitterR:
        oled.text('Go', 50, 30)
        mot.run(50,50)
        
    elif sensors["sensorL"] <= splitterL and sensors["sensorR"] > splitterR:
        oled.text('Left', 50, 30)
        mot.run(-40,40)
        time.sleep(0.1)
    elif sensors["sensorL"] > splitterL and sensors["sensorR"] <= splitterR:
        oled.text('Right', 50, 30)
        mot.run(40,-40)
        time.sleep(0.1)
    else:
        oled.text('Stop', 50, 30)
        mot.run(0,0)
    oled.show()
    
    
    
