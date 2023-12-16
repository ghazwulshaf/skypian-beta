import RPi.GPIO as GPIO

class GPIOCtrl():
    def __init__(self):
        self.pin_ac1 = 17
        self.pin_ac2 = 27
        self.pin_fert = 22

    def InitPin(self):
        GPIO.setup(self.pin_ac1, GPIO.OUT)
        GPIO.setup(self.pin_ac2, GPIO.OUT)
        GPIO.setup(self.pin_fert, GPIO.OUT)
        GPIO.output(self.pin_ac1, GPIO.HIGH)
        GPIO.output(self.pin_ac2, GPIO.HIGH)
        GPIO.output(self.pin_fert, GPIO.HIGH)

    def TurnAcOff(self):
        GPIO.output(self.pin_ac1, GPIO.HIGH)
        GPIO.output(self.pin_ac2, GPIO.HIGH)
        GPIO.output(self.pin_fert, GPIO.HIGH)

    def TurnAc1(self):
        GPIO.output(self.pin_ac1, GPIO.LOW)
        GPIO.output(self.pin_ac2, GPIO.HIGH)
        GPIO.output(self.pin_fert, GPIO.HIGH)

    def TurnAc2(self):
        GPIO.output(self.pin_ac1, GPIO.HIGH)
        GPIO.output(self.pin_ac2, GPIO.LOW)
        GPIO.output(self.pin_fert, GPIO.HIGH)

    def TurnFert(self):
        GPIO.output(self.pin_ac1, GPIO.HIGH)
        GPIO.output(self.pin_ac2, GPIO.HIGH)
        GPIO.output(self.pin_fert, GPIO.LOW)

if __name__ == "__main__":
    GPIOCtrl()