import sys
import pygame
from settings import Settings
from character import Girl
from bullet import Bullet

#Making an empty Pygame window by creating a class to represent the game.

class CatInvasion:
    def __init__(self):
        """Overall class to manage game assets and behavior."""
        pygame.init()
        self.clock = pygame.time.Clock() #We measure the time it takes to iterate over the
        self.settings = Settings() #initialize the settings from settings module
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height)) #we take this now from settings module
        self.fullscreen = False  # Flag to keep track of fullscreen mode
        pygame.display.set_caption("Cat Invasion")
        
        self.girl = Girl(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.girl.update() #update location of a character
            self._update_bullets()
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
                    self._check_keydown_events(event)        #refactoring   
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_RIGHT:
            #Move girl to the right
            self.girl.moving_right = True
        elif event.key ==pygame.K_LEFT:
            #Move girl left
            self.girl.moving_left = True
        elif event.key == pygame.K_q: #Quit the game 
            sys.exit()
        elif event.key == pygame.K_f:  # Toggle fullscreen with 'F' key
            self._toggle_fullscreen()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
   
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.girl.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.girl.moving_left = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)
                       
                    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.girl.blitme()
        
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        
    def _toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        self.fullscreen = not self.fullscreen  # Toggle the fullscreen flag
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.girl.screen = self.screen  # Update the screen reference in the girl object
    
                    
if __name__ == "__main__":
    #Make a game instance, and run the game,
    ai = CatInvasion()
    ai.run_game()