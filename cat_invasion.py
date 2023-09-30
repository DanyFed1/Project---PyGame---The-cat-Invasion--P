import sys
import pygame
from settings import Settings
from character import Girl

#Making an empty Pygame window by creating a class to represent the game.

class CatInvasion:
    def __init__(self):
        """Overall class to manage game assets and behavior."""
        pygame.init()
        self.clock = pygame.time.Clock() #We measure the time it takes to iterate over the
        self.settings = Settings() #initialize the settings from settings module
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height)) #we take this now from settings module
        pygame.display.set_caption("Cat Invasion")
        
        self.girl = Girl(self)
        
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.girl.update() #update location of a character
            self._update_screen()
            
            #controlling the frame rate based on the clocl measurement. Every time we run faster
            #refresh rate should be stable.
            self.clock.tick(60) #set the frame rate to 60
    
    def _check_events(self):
        #Watch for keyboard and mouse events.
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:   #quits the game
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move girl to the right
                        self.girl.moving_right = True
                    elif event.key ==pygame.K_LEFT:
                        #Move girl left
                        self.girl.moving_left = True
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT: #Stop moving right if key is up
                        self.girl.moving_right = False
                    elif event.key == pygame.K_LEFT: #Stop moving left if key is up
                        self.girl.moving_left = False
                    
                    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.girl.blitme()
        
        #Make the most recently drawn screen visible.
        pygame.display.flip()
                    
if __name__ == "__main__":
    #Make a game instance, and run the game,
    ai = CatInvasion()
    ai.run_game()