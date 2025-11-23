import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game, alien=None):
        """Create a bullet object at the ship's or alien's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        if alien:
            self.is_alien_bullet = True
            self.color = self.settings.alien_bullet_color
            self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width,
                self.settings.alien_bullet_height)
            self.rect.midbottom = alien.rect.midbottom
        else:
            self.is_alien_bullet = False
            self.color = self.settings.bullet_color
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                self.settings.bullet_height)
            self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up or down the screen."""
        # Update the exact position of the bullet.
        if self.is_alien_bullet:
            self.y += self.settings.alien_bullet_speed
        else:
            self.y -= self.settings.bullet_speed
        
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)