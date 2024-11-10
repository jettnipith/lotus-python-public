from machine import Pin, PWM
import time
import utime

DR1 = 2
DR2 = 15
PWMR = 13

DL1 = 16
DL2 = 17
PWML = 4

button = 27

button_pin = Pin(button, Pin.IN)

dl1_pin = Pin(DL1, Pin.OUT)
dl2_pin = Pin(DL2, Pin.OUT)
pwml_pwm = PWM(Pin(PWML))

dr1_pin = Pin(DR1, Pin.OUT)
dr2_pin = Pin(DR2, Pin.OUT)
pwmr_pwm = PWM(Pin(PWMR))

def tone(pin, frequency, duration):
    p = PWM(Pin(pin))
    p.freq(frequency)
    p.duty(512)
    time.sleep_ms(duration)
    p.deinit()

def run(spl, spr):
    max_duty = 1023  # กำหนดค่า max_duty เท่ากับค่าใน DCMotor ในตัวอย่างที่สอง
    if spl > 0:
        dl1_pin.off()
        dl2_pin.on()
        pwml_pwm.duty(int((spl / 100) * max_duty))  # ปรับค่า PWM ให้สอดคล้องกับความเร็ว
    elif spl < 0:
        dl1_pin.on()
        dl2_pin.off()
        pwml_pwm.duty(int((-spl / 100) * max_duty))  # ปรับค่า PWM ให้สอดคล้องกับความเร็ว
    else:
        dl1_pin.on()
        dl2_pin.on()
        pwml_pwm.duty(0)

    if spr > 0:
        dr1_pin.off()
        dr2_pin.on()
        pwmr_pwm.duty(int((spr / 100) * max_duty))  # ปรับค่า PWM ให้สอดคล้องกับความเร็ว
    elif spr < 0:
        dr1_pin.on()
        dr2_pin.off()
        pwmr_pwm.duty(int((-spr / 100) * max_duty))  # ปรับค่า PWM ให้สอดคล้องกับความเร็ว
    else:
        dr1_pin.on()
        dr2_pin.on()
        pwmr_pwm.duty(0)

