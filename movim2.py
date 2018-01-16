import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
GPIO_PIR = 4

print "PIR Module basic test (CTRL-C to exit)"

GPIO.setwarnings(False)

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

try:

    print "Waiting for PIR to settle ..."
    time.sleep(1)
    print "  Ready"

  # Loop until users quits with CTRL-C
    while True :
	print(GPIO.input(GPIO_PIR))

#      if GPIO.input(GPIO_PIR):
#        print("Se detecta presencia")
#        time.sleep(0.5)
#      else :
#        print("No hay presencia")
#        time.sleep(0.5)

except KeyboardInterrupt:
        print "  Quit"
  # Reset GPIO settings
GPIO.cleanup()
