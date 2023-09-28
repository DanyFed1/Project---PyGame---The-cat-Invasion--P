import sys
import pygame

#Making an empty Pygame window by creating a class to represent the game.

class CatInvasion:
    def __init__(self):
        """Overall class to manage game assets and behavior."""
        pygame.init()
        
        self.clock = pygame.time.Clock() #We measure the time it takes to iterate over the
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Cat Invasion")
        
        # Set the background color
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            
            #Make the most recently drawn screen visible.
            pygame.display.flip()
            
            #controlling the frame rate based on the clocl measurement. Every time we run faster
            #refresh rate should be stable.
            self.clock.tick(60) #set the frame rate to 60
            
if __name__ == "__main__":
    #Make a game instance, and run the game,
    ai = CatInvasion()
    ai.run_game()