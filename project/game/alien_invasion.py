import sys

import pygame
from bullet import Bullet
from pygame.event import Event
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assert and behavior."""

    def __init__(self) -> None:
        """initialize the game"""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start main loop for running game"""
        while True:
            self._check_events()

            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # frame rate
            self.clock.tick(120)

    def _update_screen(self):
        """Update images on the screen , and filp to the new screen"""
        # background color
        self.screen.fill(self.setting.bg_color)

        # blit ship with mouse position
        # mx, my = pygame.mouse.get_pos()

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make the most recently drawn screen visible
        pygame.display.flip()

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event: Event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """Create new bullet and add to bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_event(self, event: Event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
