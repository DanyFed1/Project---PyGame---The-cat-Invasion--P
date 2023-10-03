import sys
import pygame
from settings import Settings
from character import Girl
from bullet import Bullet
from allien_cat import Alien_Cat

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
        self.aliens = pygame.sprite.Group()
        
        self._create_cat_fleet()
        
        self.bg_image = self._load_bg_image('/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/G6R5FIHLLMLpkVSBxNwb-1-22vuz.bmp')
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.girl.update() #update location of a character
            self._update_bullets()
            self._update_aliens()
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
        # Get rid of bullets that have disappeared for memory reasons
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)
        
        #Check if bullet hits a cat
        #if yes, removes both objects
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Draw the background image.
        self.screen.blit(self.bg_image, (0, 0))
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.girl.blitme()
        self.aliens.draw(self.screen)
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
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
        
    def _load_bg_image(self, image_path):
        """Load and scale the background image."""
        bg_image = pygame.image.load(image_path)
        bg_image = pygame.transform.scale(bg_image, (self.settings.screen_width, self.settings.screen_height))
        return bg_image
    
    def _create_alien(self, x_position):
        """Create a cat and place it in a the row""" 
        new_alien = Alien_Cat(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)
    
    def _create_cat_fleet(self):
        """Creat the fleet of cats"""
        # Create an alien and keep adding cats until there's no room left.
        # Spacing between cats is one cat width and one cat height.
        alien_cat = Alien_Cat(self)
        alien_width, alien_height = alien_cat.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
        
            #After row is done; reset horizontal position and increment on vertical position
            current_x = alien_width
            current_y += 2* alien_height
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop all cats and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def _create_alien(self, x_position, y_position):
        """Create a cat and place it in a row""" 
        new_alien = Alien_Cat(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _update_aliens(self):
        """Check if the cats are at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

    
if __name__ == "__main__":
    #Make a game instance, and run the game,
    ai = CatInvasion()
    ai.run_game()