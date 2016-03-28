#Detta skript används för att avläsa hur varm datorn är.
#Om temperaturen överstiger en inställning så aktiveras ett relä
#Relät startar en fläkt för att kyla ner inne till datorn.
#I settings.txt filen sparas önskad gräns för temp på tredje raden.
#Ändra gpio för där relät är inkopplat.
#Utvecklat av Andreas Olsson för husvagns pc projektet
import subprocess
import os
import RPi.GPIO as GPIO
import time

while 1:
	filename = "/opt/skript/system/settings.txt"
	file = open(filename, "r")
	lines = file.read().splitlines()
	file.close()
	def get_temperature():
		try:
        		s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
			return float(s.split('=')[1][:-3])
		except:
			return 0
	temperatur = get_temperature()
	tempen= str(get_temperature())


	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(12, GPIO.OUT)
	TEMPEN = float(lines[2])

	if temperatur > TEMPEN:
		GPIO.output(12, GPIO.HIGH)
		print ("Processor Varm")
		print "Processor:" + tempen
	elif temperatur <= TEMPEN:
		GPIO.output(12, GPIO.LOW)
		print ("Processor Kall")
		print "Processor:" + tempen

	time.sleep(30)
