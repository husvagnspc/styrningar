#Detta skript avläser en Arduino som läser in analoga volt värden.
#För det kan du se under arduino hur du konstruerar en volt mätare.
#Sen läses allt in via serial in via raspberryns USB port
#Allt lagras i separat text fil för att sen kombineras med dom andras.
#Skapat av Andreas Olsson för Husvagn/Husbils Pc projektet
import serial
import os
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
        text = ser.readline()
        print ser.readline()
        file = open("/opt/skript/volten.txt", "w")
        lines_of_text = [text]
        file.writelines(lines_of_text)
        file.close()
