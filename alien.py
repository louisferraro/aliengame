import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien (bad guy)"""

    def __init__(self, ai_settings, screen):
        """initialize alien and set start position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load up alien image and set its rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at its current location"""
        self.screen.blit(self.image, self.rect)
