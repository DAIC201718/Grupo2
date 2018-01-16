import RPi.GPIO as GPIO
import time                #Importamos time
from time import gmtime, strftime  #importamos gmtime y strftime

GPIO.setmode(GPIO.BCM)             #Configuramos los pines GPIO como BCM
PIR_PIN = 4                        #Usaremos el pin GPIO n7
GPIO.setup(PIR_PIN, GPIO.IN)       #Lo configuramos como entrada

#GPIO.setup(17, GPIO.OUT)          #Configuramos el pin 17 como salida (para un led)

try:
    while True:  #Iniciamos un bucle infinito
        if GPIO.input(PIR_PIN):  #Si hay senyal en el pin GPIO n7
            #GPIO.output(17,True) #Encendemos el led
            time.sleep(1)        #Pausa de 1 segundo
            timex = strftime("%d-%m-%Y %H:%M:%S", gmtime()) #Creamos una cadena de texto con la hora
            print timex + "MOVIMIENTO DETECTADO"  #La sacamos por pantalla
            time.sleep(1)  #Pausa de 1 segundo
            #GPIO.output(17, False)  #Apagamos el led
        time.sleep(1)              #Pausa de 1 segundo y vuelta a empezar
except KeyboardInterrupt:   #Si el usuario pulsa CONTROL + C...
    print "quit"            #Anunciamos que finalizamos el script
    GPIO.cleanup()
