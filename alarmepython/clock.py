import datetime
from pygame import mixer

horas = int(input("Que horas tocar o alarme?\n"))
minuto = int(input("Que minuto tocar o alarme?\n"))
periodo = str(input("Digite am ou pm?\n"))

if(periodo == "pm"):
    horas = horas + 12

print("Aguardando")

while True:
    if(horas == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute):
       mixer.init()
       mixer.music.load('/home/matheusleao/arquivos_importantes/alarme_escolar/alarmepython/sinal.mp3')
       mixer.music.play()
       break