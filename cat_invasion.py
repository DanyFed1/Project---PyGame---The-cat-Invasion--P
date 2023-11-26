import sys
import pygame
from settings import Settings
from character import Girl
from bullet import Bullet
from allien_cat import Alien_Cat
from time import sleep
from game_stats import GameStats
from start_button import GameButton
from scoreboard import Scoreboard

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
        
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.girl = Girl(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_cat_fleet()
        
        self.bg_image = self._load_bg_image('/Users/daniilfjodorov/Desktop/CodingProjects/Alien Invaders/Project-PyGame-Cat-Invasion/assets/Game images/G6R5FIHLLMLpkVSBxNwb-1-22vuz.bmp')
        
        # Start Cat Invasion in an active state.
        self.game_active = False
        
        # Make the Play button.
        self.play_button = GameButton(self, "New Game")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_active:
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    
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
        
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        #Check if bullet hits a cat
        #if yes, removes both objects
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.cat_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Draw the background image.
        self.screen.blit(self.bg_image, (0, 0))
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.girl.blitme()
        self.aliens.draw(self.screen)
        
        # Draw the score information.
        self.sb.show_score()
        
        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        
        if not self.aliens:
            # Destroy existing bullets and create new cat fleet.
            self.bullets.empty()
            self._create_cat_fleet()
            self.settings.increase_speed()
            
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
        
    def _toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        self.fullscreen = not self.fullscreen  # Toggle the fullscreen flag
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            # self.girl.resize(self)
            # self.bullets.resize(self)
            # self.aliens.resize(self)
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
        
        # Look for alien-character collisions.
        if pygame.sprite.spritecollideany(self.girl, self.aliens):
            self._character_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_cat_bottom()
            
    def _character_hit(self):
        """Respond to the cat hitting a character."""
        if self.stats.lives_left > 0:
            # Decrement character_left.
            self.stats.lives_left -= 1
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the character.
            self._create_cat_fleet()
            self.girl.center_character()
            
            #pause
            sleep(0.5)
            
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_cat_bottom(self):
        """Check if any of the cats have reached the bottom of the screen."""
        for cat in self.aliens.sprites():
            if cat.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._character_hit()
                break
        
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks New Game."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings. 
            self.settings.initialize_dynamic_settings()
            
            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.game_active = True
            
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            
            # Create a new fleet and center the ship.
            self._create_cat_fleet()
            self.girl.center_character()
            
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
    
if __name__ == "__main__":
    #Make a game instance, and run the game,
    ai = CatInvasion()
    ai.run_game()