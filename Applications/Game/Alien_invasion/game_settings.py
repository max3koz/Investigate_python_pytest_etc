class GameSettings:
    """
    Class to save all game settings.
    """
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (120, 210, 230)

        # Ship setting
        self.ship_speed = 5

        # Bullet setting
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = (60, 60 ,60)