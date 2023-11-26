class Settings:
    """A class to store all settings for the game"""
    
    def __init__(self):
        """Initialize the settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30,0,30) #background color
        
        #Girl settings
        self.lives_limit = 3
        
        #Bullet settings:  #To be later replaced with a fish onject.
        self.bullet_width = 30
        self.bullet_height = 40
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 #sets the limit of allowed bullets
        
        #Cats' settings: 
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.2
        
        # How quickly the cats point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Settings will change throughout the game."""
        self.girl_speed = 1.5 #Controlling characters speed
        self.bullet_speed = 2.5
        self.cat_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1    
        
        # Scoring settings
        self.cat_points = 50
        
    def increase_speed(self):
        """Increase speed settings and point values."""
        self.girl_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.cat_speed *= self.speedup_scale