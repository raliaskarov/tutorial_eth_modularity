"""
Level 2 MONOLITHIC: Add Player Names
=====================================

Monolithic version with player names added.
- Players now have names
- Still no official tennis terminology
"""


class Tennis:
    """Monolithic tennis game with player names."""

    def __init__(self, name1, name2):
        self.player1_name = name1
        self.player2_name = name2
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.winner = None

    def score_point(self, name):
        """Score a point for the named player."""
        if self.game_over:
            return

        if name == self.player1_name:
            self.player1_score += 1
        elif name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError(f"Unknown player: {name}")

        # Check if game is won
        if self.player1_score >= 4 or self.player2_score >= 4:
            self.game_over = True
            self.winner = self.player1_name if self.player1_score > self.player2_score else self.player2_name

    def print_score(self):
        """Display the current score."""
        print(f"{self.player1_name}: {self.player1_score}, {self.player2_name}: {self.player2_score}")
        if self.game_over:
            print(f"Game Over! Winner: {self.winner}")

    def reset_game(self):
        """Reset the game to initial state."""
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.winner = None


if __name__ == "__main__":
    game = Tennis("Alice", "Bob")
    game.score_point("Alice")
    game.print_score()
    game.score_point("Bob")
    game.print_score()
    game.score_point("Alice")
    game.print_score()
    game.score_point("Alice")
    game.print_score()
    game.score_point("Alice")
    game.print_score()
