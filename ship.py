import pygame

class Ship():
    def __init__(self, screen):
        """init statku i połozenie początkowe"""
        self.screen = screen

        #wczytanie obrazu statku i pobranie prostokąta
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #każdy nowy ship pojawia się na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #wyświeltenie statku w aktualnym położeniu
        self.screen.blit(self.image, self.rect)
