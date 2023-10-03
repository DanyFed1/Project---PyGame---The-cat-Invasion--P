class Settings:
    """A class to store all settings for the game"""
    
    def __init__(self):
        """Initialize the settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30,0,30) #background color
        
        #Girl settings
        self.girl_speed = 1.5 #Controlling characters speed
        
        #Bullet settings:  #To be later replaced with a fish onject.
        self.bullet_speed = 2.0
        self.bullet_width = 30
        self.bullet_height = 40
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 #sets the limit of allowed bullets
        
        #Cats' settings: 
        self.cat_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        