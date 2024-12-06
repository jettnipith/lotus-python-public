from machine import ADC, Pin
import time


# Setup analog pin
adcL = ADC(Pin(26))  # Replace with the actual analog pin you connected the sensor to
adcR = ADC(Pin(25))  # Replace with the actual analog pin you connected the sensor to
adc1 = ADC(Pin(14))


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

def moisture():
    try:
        # Read analog value from the photoresistor
        analog_value = adc1.read()
        # Map the analog value to a percentage (adjust the range if needed)
        percent_voltage = (analog_value / 4095) * 100
        moisture_percentage = 100-percent_voltage
        # Print the analog value
        #print(f'Analog Value: {analog_value}')
        return {"analogVal":analog_value, "percent": moisture_percentage}
        
    except Exception as e:
        #print(f'Error reading sensor data: {e}')
        return e


