import datetime
from pygame import mixer

horas = int(input("Que horas tocar o alarme?\n"))
minuto = int(input("Que minuto tocar o alarme?\n"))
periodo = input("Digite am ou pm?\n")

if(periodo == "pm"):
    horas = horas + 12

print("Aguardando")

while True:
    if(horas == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute):
       pygame.mixer.music.queue('sinal.mp3')