#Denna lampstyrning använder en textfil för att läsa av knappstatus
#Det är inte nödvändigt om man inte vill kunna enkelt visa om lampan är på eller av
#Ändra sökvägen i filerna om du skall använda knappstatus
#Glöm inte att ställa in vilken GPIO som styrningen är inkopplad på.
#Detta är för att aktivera 1 stycke relä
#Konstruerad av Andreas Olsson för Husvagns PC Projekt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.OUT)

state = GPIO.input(29)

if (GPIO.input(29) == 1):
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.LOW)
	with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
		data = file.readlines()
	data[0] = '1\n'
	with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
		file.writelines( data )
	print ("Lampa Aktiverad")
elif (GPIO.input(29) == 0):
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.HIGH)
	with open('/opt/skript/lampstyrning/knappstatus.txt', 'r') as file:
		data = file.readlines()
	data[0] = '0\n'
	with open('/opt/skript/lampstyrning/knappstatus.txt', 'w') as file:
		file.writelines( data )
	print ("Lampa Avaktiverad")
