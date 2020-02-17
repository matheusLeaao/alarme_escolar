#!bin/bash
# Teste tocar música python 
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>


import pygame



pygame.init()
pygame.mixer.music.load('sinal.mp3')
pygame.mixer.music.play()
pygame.event.wait()
