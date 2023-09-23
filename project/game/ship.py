import pygame


class Ship:
    """A class for manage the ship"""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting

        # Load the ship image and its rectangel
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.move_right = False
        self.move_left = False
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag"""
        if (self.move_right) and (self.rect.right < self.screen_rect.right):
            self.x += self.setting.ship_speed
        elif (self.move_left) and (self.rect.left > 0):
            self.x -= self.setting.ship_speed
        self.rect.x = self.x

    def blitme(self, position=None):
        """Draw the ship at its current location"""
        # position for if we have been mouce movement
        if position == None:
            position = self.rect
        else:
            self.rect.center = position
        self.screen.blit(self.image, self.rect)
