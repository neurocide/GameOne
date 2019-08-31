import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #inicjalizacja gry i uteworznie obiektu na ekranie
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja Obcych")

    #utworznie statku
    ship = Ship(screen)

    #pętla główna
    while True:
        gf.check_events()

        #czekaj na klawisz lub mysz
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #odświeżenie ekranu w trkacie każdej iteracji
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        #wyświetlenie ekranu
        pygame.display.flip()

run_game()
