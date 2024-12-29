import pygame

from constants import file_path

class Ship:
    """
    Class to control the ship
    """
    def __init__(self, ai_game):
        """Initial the ship and its starting position."""
        self.screen = ai_game.game_screen
        self.ship_speed_settings = ai_game.game_setting
        self.screen_rect = ai_game.game_screen.get_rect()

        """Download the my_ship image and get it rect"""
        self.ship_image = pygame.image.load(f"{file_path}/Images/my_ship.bmp")
        self.rect = self.ship_image.get_rect()

        """Create each new ship down the screen in the middle."""
        self.rect.midbottom = self.screen_rect.midbottom

        """Save the decimal value for the ship position horizontally"""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        """Moving inicator"""
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update_position(self):
        """Update current ship position based on the moving indicator."""
        if self.moving_right:
            self.rect.x += self.ship_speed_settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.ship_speed_settings.ship_speed
        if self.moving_bottom:
            self.rect.y += self.ship_speed_settings.ship_speed
        if self.moving_top:
            self.rect.y -= self.ship_speed_settings.ship_speed

    def start_position(self):
        """Paint ship in the current location"""
        self.screen.blit(self.ship_image, self.rect)
