import sys

import pygame

def check_events():
    """ Reakcja na zdarzenie klawiatury lub muszy """
    for event in pygame.event.get()
    if event.type == pygame.QUIT:
        sys.exit()
        
