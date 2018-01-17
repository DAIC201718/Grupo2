#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import subprocess
import sys


GPIO.setmode(GPIO.BCM)
P_PIN = 27                        
GPIO.setup(P_PIN, GPIO.IN)      
GPIO.setwarnings(False)
try:
    while True:
        if(GPIO.input(P_PIN) == True):
            os.system("python dht_consola.py")

except KeyboardInterrupt:
    print "quit"
    GPIO.cleanup()

