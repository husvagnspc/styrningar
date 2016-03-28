#Denna låter dig aktivera timer funktion på relän för belysning
#Skapa ett cron job som körs varje minut
#Tider avläses från timer.txt filen för att veta när dom skall aktiveras.
#Du lär själv lägga till eller ta bort beroende på vad du vill ha på timer
#Byggd av Andreas Olsson för husvagns pc projektet
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

print (time.strftime("%H:%M"))
#Öppna timer filen för att avläsa tider
filename = "/opt/skript/timer/timer.txt"
file = open(filename, "r")
lines = file.read().splitlines()
file.close()

now = datetime.datetime.now().time()

print now
#Ttart av timer utebelysning
startUte=datetime.datetime.strptime(lines[0], '%H:%M').time()

stopUte=datetime.datetime.strptime(lines[1], '%H:%M').time()
aktiveradUte=int(lines[6])

if aktiveradUte == 1:

	if now >= startUte and now <= stopUte:        
		print "Inom tid startar timer"
		GPIO.setup(31, GPIO.OUT)
		GPIO.output(31, GPIO.LOW)
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
			data = file.readlines()
		data[1] = '1\n'
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
			file.writelines( data )
		print ("Lampa Aktiverad")
	else:
		print "Ej i tid"
		print "stoppa timer"
		GPIO.setup(31, GPIO.OUT)
		GPIO.output(31, GPIO.HIGH)
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
			data = file.readlines()
		data[1] = '0\n'
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
			file.writelines( data )
		print ("Lampa Avaktiverad")
else:
	print "Ute belysning ej timer aktiverad"
#stop av timer utebelysning

#start av timer position
startPosition=datetime.datetime.strptime(lines[2], '%H:%M').time()

stopPosition=datetime.datetime.strptime(lines[3], '%H:%M').time()
aktiveradPos=int(lines[7])

if aktiveradPos == 1:

	if now >= startPosition and now <= stopPosition:
		print "Inom tid startar timer"
		GPIO.setup(33, GPIO.OUT)
		GPIO.output(33, GPIO.LOW)
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
			data = file.readlines()
		data[2] = '1\n'
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
			file.writelines( data )
		print ("Lampa Aktiverad")
	else:
		print "Ej i tid"
		print "stoppa timer"
		GPIO.setup(33, GPIO.OUT)
		GPIO.output(33, GPIO.HIGH)
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
			data = file.readlines()
		data[2] = '0\n'
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
			file.writelines( data )
		print ("Lampa Avaktiverad")
else:
	print "Position belysning ej timer aktiverad"
#stop av timer position

#start av timer list
startList=datetime.datetime.strptime(lines[4], '%H:%M').time()

stopList=datetime.datetime.strptime(lines[5], '%H:%M').time()
aktiveradList=int(lines[8])

if aktiveradList == 1:

	if now >= startList and now <= stopList:
		print "Inom tid startar timer"
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, GPIO.LOW)
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
			data = file.readlines()
		data[3] = '1\n'
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
			file.writelines( data )
		print ("Lampa Aktiverad")
	else:
		print "Ej i tid"
		print "stoppa timer"
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, GPIO.HIGH)
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
			data = file.readlines()
		data[3] = '0\n'
		with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
			file.writelines( data )
		print ("Lampa Avaktiverad")
else:
        print "Ljuslist belysning ej timer aktiverad"
#stop av timer ljusbelysning
