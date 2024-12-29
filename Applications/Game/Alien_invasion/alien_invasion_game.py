import pygame
import sys

from game_settings import GameSettings
from ship import Ship

class AlienInvasion:
    """
    Main class, manages the resources and behavior of the game.
    """
    def __init__(self):
        """
        Initialize the game, and create game resources.
        """
        pygame.init()
        self.game_setting = GameSettings()
        self.game_screen = pygame.display.set_mode((self.game_setting.screen_width,
                                                    self.game_setting.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        """
        Start the main game cycle.
        """
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_screen()

    def _check_events(self):
        """Reaction on the click buttons or mouse actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _update_screen(self):
        self.game_screen.fill(self.game_setting.background_color)  # Reprint screen at each iteration of cycle.
        self.ship.start_position()

        pygame.display.flip()  # Show the last paint screen.

"""Create an instance of the game and run it."""
instance_game = AlienInvasion()
instance_game.run_game()
