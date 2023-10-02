import pygame
from pygame.sprite import Sprite

class Alien_Cat(Sprite):
    """A class to represent a single alien cat in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen=ai_game.screen
        
        #Load the cat image and set its rect attribute.
        self.image = pygame.image.load("/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/DALL·E-2023-09-30-18.46 (1).bmp")
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        self.rect = self.image.get_rect()
        # Place each new cat near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the cat's exact horizontal position.
        self.x = float(self.rect.x)