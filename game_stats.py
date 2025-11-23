class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self.get_high_score()

    def get_high_score(self):
        """Get the high score from the file if it exists."""
        try:
            with open('high_score.txt') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1