#!bin/bash
# Programa com intuíto de tocar um alarme conforme horário definido 
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>

import datetime
import pygame

horas = int(input("Que horas tocar o alarme?\n"))
minuto = int(input("Que minuto tocar o alarme?\n"))
periodo = input("Digite am ou pm?\n")

if(periodo == "pm"):
    horas = horas + 12

print("Aguardando")

while True:
    if(horas == datetime.datetime.now().hour and minuto == datetime.datetime.now().minute):
        pygame.init()
        pygame.mixer.music.load('sinal.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        pygame.stop()
        break
