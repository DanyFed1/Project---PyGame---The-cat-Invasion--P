import pygame
from pygame.sprite import Sprite
import os

class Bullet(Sprite):
    """A class to manage bullets fired from the girl."""
    
    def __init__(self, ai_game):
        """Create a bullet object at the girl's current position."""
        super().__init__()  # To properly inherit
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the fish image and get its rect.
        image_path = os.path.join(self.base_dir, 'assets/Game images/DALL·E-2023-09-28-21.48.bmp')
        self.image = pygame.image.load(image_path)
        # Resize the image if necessary
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.girl.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
        
    def resize(self, width, height):
        """Resize the image. for the screen dimensions"""
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom