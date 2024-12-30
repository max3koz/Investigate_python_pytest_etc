import pygame

# from constants import file_path
from pygame.sprite import Sprite

class Bullet(Sprite):
    """The class use to manage of bullets are started from my_ship."""
    def __init__(self, ai_game):
        """Create bullet in the current ship position."""
        super().__init__()
        self.screen = ai_game.game_screen
        self.setting = ai_game.game_setting
        self.color = self.setting.bullet_color

        """Create bullet rect at (0, 0) and set right position"""
        # self.ship_image = pygame.image.load(f"{file_path}/Images/bullet.bmp")
        self.rect =pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        """Save the decimal value for the bullet position"""
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet to top of the screen"""
        # Update decimal bullet position
        self.y -= self.setting.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
