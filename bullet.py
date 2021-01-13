# louis ferraro

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class that will manage bullets fired from spaceship"""
    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at ship's current position"""
        # allows us to inherit properties from Sprite
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at origin (0, 0) then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        # update the decimal position of the bullet
        self.y -= self.speed_factor
        # update rect
        self.rect.y = self.y

    def draw_bullet(self):
        """draws bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
