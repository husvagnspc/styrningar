#Detta är system skriptet som körs i bakgrunden så länge datorn är på.
#Den loopas och har en paus på 20 sekunder.
#Värderna sparas i en textfil som sedan kan hämtas till hemsida eller ex kodi.
#Du måste själv ändra adresserna till tempgivarna samt alla anslutningar till olika funktioner
#Utvecklat av Andreas Olsson för husvagns pc projektet
import time
import RPi.GPIO as GPIO
import os
while 1:
  #Öppnar inställningar
  filename = "/opt/skript/system/settings.txt"
	file = open(filename, "r")
	lines = file.read().splitlines()
	file.close()
	#Öppnar knappstatus filen
	filename1 = "/opt/skript/lampstyrning/knappstatus.txt"
	file1 = open(filename1, "r")
	lines1 = file1.read().splitlines()
	file1.close()
	#Tempgivare 1/4 Ändra: 28-011464cdc0ff denna används för tempen inne
	tempfile = open("/sys/bus/w1/devices/28-011464cdc0ff/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000
	temperature = round(temperature, 1)
	
	#Tempgivare 2/4 Ändra: 28-021463284fff denna används för tempen ute
	tempfile1 = open("/sys/bus/w1/devices/28-021463284fff/w1_slave")
	thetext1 = tempfile1.read()
	tempfile1.close()
	tempdata1 = thetext1.split("\n")[1].split(" ")[9]
	temperature1 = float(tempdata1[2:])
	temperature1 = temperature1 / 1000
	temperature1 = round(temperature1, 1)
	
	#Tempgivare 3/4 Ändra: 28-0314621b8cff denna används för inne i kylskåpet
	tempfile2 = open("/sys/bus/w1/devices/28-0314621b8cff/w1_slave")
	thetext2 = tempfile2.read()
	tempfile2.close()
	tempdata2 = thetext2.split("\n")[1].split(" ")[9]
	temperature2 = float(tempdata2[2:])
	temperature2 = temperature2 / 1000
	temperature2 = round(temperature2, 1)

	
	#Tempgivare 4/4 Ändra: 28-02146335ccff denna används för kylskåps larmet
	tempfile3 = open("/sys/bus/w1/devices/28-02146335ccff/w1_slave")
	thetext3 = tempfile3.read()
	tempfile3.close()
	tempdata3 = thetext3.split("\n")[1].split(" ")[9]
	temperature3 = float(tempdata3[2:])
	temperature3 = temperature3 / 1000
	temperature3 = round(temperature3, 1)

	print "Inne: " ,temperature, "grader"
	print "Ute: " ,temperature1, "grader"
	print "Kyl: " ,temperature2, "grader"
	print "Larm: ", temperature3, "grader"

	#Nu avläser vi vatten nivån
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	#TRIG är på den GPIO anslutning som ljud mätaren triggar
	TRIG = 37
	#ECHO är på den GPIO anslutning som ljud mätaren ekar tillbaka
	ECHO = 35
	#Läs av i inställnings filen hur djup vattentanken är, behövs för att räkna ut mängden
	TANK = float(lines[0])
	#Läs av i inställnings filen när kylskåps larmet skall aktiveras
	KYLTEMP = float(lines[1])
	#Kolla om fläkten är aktiverad
	FLAKTPA = float(lines1[6])

	print "Cabby Vatten Kontroll Startad"

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	print "Kallibrerar vatten sensor"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
        	pulse_start = time.time()

	while GPIO.input(ECHO)==1:
        	pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	procent1 = TANK - distance
	procent = procent1 / TANK * 100

	procent = int(procent)

	if procent >= 100:
        	procent = int(100)
	elif procent <= 0:
        	procent = int(0)

	print "Vatten:", distance, "cm"
	print "Procent:",procent, "% av 100"

	GPIO.cleanup()

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(36, GPIO.OUT)

	#Om fläkten inte är startad manuellt så aktivera den, glöm ej att ändra relä anslutningen
	if FLAKTPA == 0:
		if temperature3 >=KYLTEMP:
			GPIO.setup(36, GPIO.OUT)
			GPIO.output(36, GPIO.LOW)
			with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
				data = file.readlines()
			data[5] = '1\n'
			data[7] = '1\n'
			with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
				file.writelines( data )
			print ("Kyl Aktiverad")
		elif temperature3 <=KYLTEMP:
			GPIO.setup(36, GPIO.OUT)
			GPIO.output(36, GPIO.HIGH)
			with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
				data = file.readlines()
			data[5] = '0\n'
			data[7] = '0\n'
			with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
				file.writelines( data )
			print ("Kyl Avaktiverad")
	
	#Vi tar bort gamla filen för att göra en ny av säkerhetsskäl innan värdena skrivs
	if os.path.exists("/opt/skript/system/texten.txt"):
		os.remove("/opt/skript/system/texten.txt")
	else:
		print("Sorry, I can not remove %s file." % filename)
	tempen1 = str(temperature)
	tempen2 = str(temperature1)
	tempen3 = str(temperature2)
	tempen4 = str(temperature3)
	procenten = str(procent)
	file = open("/opt/skript/system/texten.txt", "w")
	#Skriv alla värden på separata rader 12.3 är för volten, då avläsning för det ej är inbyggt här
	lines_of_text = [tempen1,"\n",tempen2,"\n",tempen3,"\n",procenten,"\n","12.3\n",tempen4]
	file.writelines(lines_of_text)
	file.close()

	time.sleep(20)
