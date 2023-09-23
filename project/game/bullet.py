import pygame
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings


class Bullet(Sprite):
    """A class to magnage bullet fired from the ship"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen: Surface = ai_game.screen
        self.setting: Settings = ai_game.setting
        self.color = self.setting.bullet_color

        # Create a bullet rect at (0,0) and then set correc position .
        self.rect = pygame.Rect(
            0, 0, self.setting.bullet_width, self.setting.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's position as float
        self.y = float(self.rect.y)

    def update(self):
        """Update position's of bullet"""
        # Move bullet to top
        self.y -= self.setting.bullet_speed

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
