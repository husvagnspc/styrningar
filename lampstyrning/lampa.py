import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.OUT)

state = GPIO.input(29)

if (GPIO.input(29) == 1):
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.LOW)
	with open('/opt/skript/knappstatus.txt', 'r') as file:
		data = file.readlines()
	data[0] = '1\n'
	with open('/opt/skript/knappstatus.txt', 'w') as file:
		file.writelines( data )
	print ("Lampa Aktiverad")
elif (GPIO.input(29) == 0):
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.HIGH)
	with open('/opt/skript/knappstatus.txt', 'r') as file:
		data = file.readlines()
	data[0] = '0\n'
	with open('/opt/skript/knappstatus.txt', 'w') as file:
		file.writelines( data )
	print ("Lampa Avaktiverad")
