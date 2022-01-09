import json


class GameStats:
    """Tracks statistics for the game Alien Invasion"""

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        self.game_active = False
        self.difficulty_selection_complete = False
        self.score = 0
        self.high_score = 0
        self.loaded_high_score = 0
        self.level = 1
        self.reset_stats()
        self._get_high_score()

    def reset_stats(self):
        """Resets the game statistics"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score(self):
        """Get the high score from a json file"""
        filename = 'saved_high_score.json'
        try:
            with open(filename) as f:
                self.high_score = self.loaded_high_score = json.load(f)
        except FileNotFoundError:
            return None

    def set_new_record(self):
        """Saved the newest record high score"""
        filename = 'saved_high_score.json'
        if self.high_score > self.loaded_high_score:
            with open(filename, 'w') as f:
                json.dump(self.high_score, f)
