from machine import ADC, Pin
import time


# Setup analog pin
adcL = ADC(Pin(26))  # Replace with the actual analog pin you connected the sensor to
adcR = ADC(Pin(36))  # Replace with the actual analog pin you connected the sensor to


def read_two_sensors():
    try:
        # Read analog value from the photoresistor
        analog_value_l = adcL.read()
        analog_value_r = adcR.read()

        # Print the analog value
        #print(f'Analog Value: {analog_value}')
        return {"sensorL":analog_value_l, "sensorR": analog_value_r}
        
    except Exception as e:
        #print(f'Error reading sensor data: {e}')
        return e


