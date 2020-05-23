import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make ship
    ship = Ship(ai_settings, screen)

    # make group to store bullets
    bullets = Group()

    # make an alien
    alien = Alien(ai_settings, screen)

    # start the main loop for the game
    while True:

        # check events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # redraw background color
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()