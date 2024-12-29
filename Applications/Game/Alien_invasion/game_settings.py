class GameSettings:
    """
    Class to save all game settings.
    """
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (120, 210, 230)
        self.ship_speed = 5