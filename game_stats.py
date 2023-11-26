import pygame

class GameStats:
    """Track statistics for Cat Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        
        self.lives_left = self.settings.lives_limit
        self.score = 0
        self.level = 1
        