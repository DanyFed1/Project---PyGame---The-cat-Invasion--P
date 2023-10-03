import pygame
from pygame.sprite import Sprite
from random import randint

class Alien_Cat(Sprite):
    """A class to represent a single alien cat in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen=ai_game.screen
        self.settings = ai_game.settings
        
        #Load the cat image and set its rect attribute.
        self.image_1 = pygame.image.load("/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/DALL·E-2023-09-30-18.46 (1).bmp")
        self.image_1 = pygame.transform.scale(self.image_1, (60, 60))
        self.image_2 = pygame.image.load("/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/DALL·E-2023-09-30-19.02.bmp")
        self.image_2 = pygame.transform.scale(self.image_2, (60, 60))
        self.image_3 = pygame.image.load("/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/DALL·E-2023-09-30-19.00.bmp")
        self.image_3 = pygame.transform.scale(self.image_3, (60, 60))
        
        self.random_number = randint(0,2)
        if self.random_number == 0:
            self.image = self.image_1
            self.rect = self.image_1.get_rect()
        elif self.random_number == 1:
            self.image = self.image_2
            self.rect = self.image_2.get_rect()
        elif self.random_number == 2:
            self.image = self.image_3
            self.rect = self.image_3.get_rect()
        # Place each new cat near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the cat's exact horizontal position.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move cat tot the right"""
        self.x += self.settings.cat_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
