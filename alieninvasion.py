# louis ferraro
# practice using pygame

# to disable pygame's welcome message when runnning program
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create the screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # make a ship. group of bullets, and group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)

    # starts the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
