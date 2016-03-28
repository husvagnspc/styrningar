#Denna sätter korrekt värde på gpio på alla relän som används.
#Placeras i /etc/rc.local som körs en gång vid uppstart
#Korrigera så det stämmer med så många relän du använder.
#Om du inte kör denna vid uppstart så har du svagt sken från reläna samt
#Att dom inte fungerar direkt vid uppstart.
#Konstruerad av Andreas Olsson för husvagns pc projektet
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

GPIO.output(29, GPIO.HIGH)
GPIO.output(31, GPIO.HIGH)
GPIO.output(33, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(32, GPIO.HIGH)
GPIO.output(36, GPIO.HIGH)
