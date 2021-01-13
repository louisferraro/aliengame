# louis ferraro

import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initialize a ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start every ship from the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ships movement based on the flag boolean (for continuos movement)"""
        # using ifs instead of elifs makes for more fluid movement/accounts for pressing both keys
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
