class Settings:
    """A class to store all settings of Alien Invasion"""

    def __init__(self) -> None:
        """initialize the game's settings"""

        # screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.ship_speed = 4.5

        # bullet setting
        self.bullet_speed = 6.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
