import pygame

class Girl:
    """A class to maange player controlled character - girl"""
    
    def __init__(self, ai_game):
        """Initialize the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the girl image and get its rect
        self.image = pygame.image.load('/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/rcIaniCpy5NCWgUYcK2r-1-sb7rx-_1_.bmp')
        # Resize the image
        self.image = pygame.transform.scale(self.image, (100, 100))  # Set new dimensions (width, height)
        self.rect = self.image.get_rect() #pygame treats objects as rectangles which 
        #simplifies the collision registration
        
        #Start each new girl at the bottom center of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the girl at its current location."""
        self.screen.blit(self.image, self.rect)