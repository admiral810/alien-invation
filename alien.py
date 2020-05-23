import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_settings, screen):
        """initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
