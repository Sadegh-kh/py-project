import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent of single alien in fleet"""

    def __init__(self, ai_game) -> None:
        """Initalize the alien and set its position."""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(
            self.image,
            (40, 40),
        )
        self.rect = self.image.get_rect()

        # start each alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # postion of each alien
        self.x = float(self.rect.x)
