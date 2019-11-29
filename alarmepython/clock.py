import datetime
#import playsound
from pygame import mixer

horas = int(input("Que horas tocar o alarme?\n"))
minuto = int(input("Que minuto tocar o alarme?\n"))
periodo = str(input("Digite am ou pm?\n"))

if(periodo == "pm"):
    horas = horas + 12

print("Aguardando")

while True:
    if(horas == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute):
       print("Tocando agora as " + str(datetime.datetime.now()))
       #playsound.playsound('/path/to/filename.mp3', True)
       break