#!/usr/bin/python

# Internet de las Cosas - http://internetdelascosas.cl
#
# Descripcion  : Programa que permite obtener la lectura de un sensor DHT11
# Lenguaje     : Python
# Autor        : Jose Zorrilla <jzorrilla@iot.cl>
# Dependencias : Libreria de Adafruit https://github.com/adafruit/Adafruit_Python_DHT
# Web          : http://internetdelascosas.cl/

# Importa las librerias necesarias
import subprocess
import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)

# Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 23

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:
    # Ciclo principal infinito
    # Obtiene la humedad y la temperatura desde el sensor
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    #Imprime en la consola las variables temperatura y humedad con un decimal
    print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))
    if humedad > 30:
        print("Hoy va a llover asi que lleva paraguas")
    else:
        print("Hoy lo mas probable es que no llueva. Tenga un buen dia")
    
    if temperatura >= 21:
        print("Hoy va a hacer calor, no hace falta que lleves chaqueta.")
    elif temperatura < 21 and temperatura > 10:
        print("Hoy hara un poco de fresco, considere llevar un jersey.")
    else:
        print("Hoy hara bastante frio asi que mejor si se lleva una chaqueta que abrigue")
    bash = "curl -i -XPOST 'https://corlysis.com:8086/write?db=raspberrypi2' -u token:693542bf37490ccfef5f1f33fd9827f0 --data \"temp_hum,Temp={0:0.1f} Hum={1:0.1f}\""
    subprocess.call(bash.format(temperatura, humedad), shell=True)

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
	# Imprime en pantalla el error e
	print str(e)
except KeyboardInterrupt:
    print "quit"
    GPIO.cleanup()
