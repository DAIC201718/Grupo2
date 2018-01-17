#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import time
import subprocess
import sys

GPIO.setmode(GPIO.BCM)
P_PIN = 22                        
GPIO.setup(P_PIN, GPIO.IN)      
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
PIR_PIN = 4                        #Usaremos el pin GPIO n7
GPIO.setup(PIR_PIN, GPIO.IN)       #Lo configuramos como entrada
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
segundos_d=int(10)
tiempo_sonido=float(0.5)
tiempo_silencio=float(0.5)
 
try:
    while True:
        if(GPIO.input(P_PIN) == True):
            time.sleep(10)
            inicio=time.time()+10
            final=inicio+segundos_d
            while inicio<final:
                GPIO.output(18, True)
                time.sleep(tiempo_sonido)
                GPIO.output(18, False)
                time.sleep(tiempo_silencio)
                inicio=time.time()
                if(GPIO.input(17) == True and GPIO.input(PIR_PIN) == True) :
                    GPIO.output(18, False)
                    print("Alarma apagada")
                    break
                else:
                    GPIO.output(18, False)


except KeyboardInterrupt:
    print "quit"
    GPIO.cleanup()

