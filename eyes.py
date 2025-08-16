# V2 modified for LCD eyes on 5 bit bus
import RPi.GPIO as GPIO
import numpy as np
import time
from threading import Thread

BIT_1_GPIO = 24
BIT_2_GPIO = 23
BIT_3_GPIO = 4
BIT_4_GPIO = 5
BIT_5_GPIO = 6


class Eyes:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(BIT_1_GPIO, GPIO.OUT)
        GPIO.setup(BIT_2_GPIO, GPIO.OUT)
        GPIO.setup(BIT_3_GPIO, GPIO.OUT)
        GPIO.setup(BIT_4_GPIO, GPIO.OUT)
        GPIO.setup(BIT_5_GPIO, GPIO.OUT)

        GPIO.output(BIT_1_GPIO, GPIO.LOW)
        GPIO.output(BIT_2_GPIO, GPIO.LOW)
        GPIO.output(BIT_3_GPIO, GPIO.LOW)
        GPIO.output(BIT_4_GPIO, GPIO.LOW)
        GPIO.output(BIT_5_GPIO, GPIO.LOW)

        self.pi_bit_1 = 0
        self.pi_bit_2 = 0
        self.pi_bit_3 = 0
        self.pi_bit_4 = 0
        self.pi_bit_5 = 0

        self.decimal_number = 0

    def run(self, lcd_command=0):
        self.decimal_number = lcd_command            #____________INPUT
        #print (f"LCD Eyes Command = {self.decimal_number}")
        binary_string = bin(self.decimal_number)
        binary_string = binary_string[2:]            # remove the "0b" prefix:
        #print(f"5 Bit Bus : {binary_string}")        # Output:  binary string
        temp = len(binary_string)                    # get number of bits

        #bits   5 4 3 2 1
        #Bin:  16 8 4 2 1
        #temp:  4 3 2 1 0

        self.pi_bit_1 = 0                       #reset bits, cos we only set high bits
        self.pi_bit_2 = 0
        self.pi_bit_3 = 0
        self.pi_bit_4 = 0
        self.pi_bit_5 = 0
        if temp >= 1:
            self.pi_bit_1 = int(binary_string[temp -1 ])
        if temp >= 2:
            self.pi_bit_2 = int(binary_string[temp - 2])
        if temp >= 3:
            self.pi_bit_3 = int(binary_string [temp - 3]) 
        if temp >= 4:
            self.pi_bit_4 = int(binary_string [temp - 4])
        if temp >= 5:
            self.pi_bit_5 = int(binary_string [temp - 5])
        #print (self.pi_bit_1)
        #print (self.pi_bit_2)
        #print (self.pi_bit_3)
        #print (self.pi_bit_4)
        #print (self.pi_bit_5)
        if self.pi_bit_1:
            GPIO.output(BIT_1_GPIO, GPIO.HIGH)
        if not self.pi_bit_1:
            GPIO.output(BIT_1_GPIO, GPIO.LOW)
        if self.pi_bit_2:
            GPIO.output(BIT_2_GPIO, GPIO.HIGH)
        if not self.pi_bit_2:
            GPIO.output(BIT_2_GPIO, GPIO.LOW)
        if self.pi_bit_3:
            GPIO.output(BIT_3_GPIO, GPIO.HIGH)
        if not self.pi_bit_3:
            GPIO.output(BIT_3_GPIO, GPIO.LOW)
        if self.pi_bit_4:
            GPIO.output(BIT_4_GPIO, GPIO.HIGH)
        if not self.pi_bit_4:
            GPIO.output(BIT_4_GPIO, GPIO.LOW)
        if self.pi_bit_5:
            GPIO.output(BIT_5_GPIO, GPIO.HIGH)
        if not self.pi_bit_5:
            GPIO.output(BIT_5_GPIO, GPIO.LOW)


if __name__ == "__main__":
    e = Eyes()

    while True:    
        e.run()
        time.sleep(1)
        