import pygame

pygame.init()
pygame.mixer.music.load('sinal.mp3')
pygame.mixer.music.play()
pygame.event.wait()