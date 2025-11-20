"""
Level 3 MONOLITHIC: Track Total Games Won
==========================================

Monolithic version that tracks total games won by each player.
- Players have win counters
- Games won displayed in parentheses
- Still monolithic
"""


class Tennis:
    """Monolithic tennis game with win tracking."""

    SCORE_NAMES = ["love", "fifteen", "thirty", "forty"]

    def __init__(self, name1, name2):
        self.player1_name = name1
        self.player2_name = name2
        self.player1_score = 0
        self.player2_score = 0
        self.player1_games_won = 0
        self.player2_games_won = 0
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
            if self.player1_score > self.player2_score:
                self.winner = self.player1_name
                self.player1_games_won += 1
            else:
                self.winner = self.player2_name
                self.player2_games_won += 1

    def print_score(self):
        """Display the current score with games won in parentheses."""
        if self.game_over:
            print(f"Game: {self.winner} ({self.player1_games_won}-{self.player2_games_won})")
        elif self.player1_score == self.player2_score and self.player1_score < 4:
            print(f"{self.SCORE_NAMES[self.player1_score]} all ({self.player1_games_won}-{self.player2_games_won})")
        else:
            p1_display = self.SCORE_NAMES[self.player1_score] if self.player1_score < 4 else str(self.player1_score)
            p2_display = self.SCORE_NAMES[self.player2_score] if self.player2_score < 4 else str(self.player2_score)
            print(f"{self.player1_name} ({self.player1_games_won}): {p1_display}, {self.player2_name} ({self.player2_games_won}): {p2_display}")

    def reset_game(self):
        """Reset the current game (but keep games won counter)."""
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.winner = None


if __name__ == "__main__":
    game = Tennis("Alice", "Bob")

    # Play first game
    print("=== Game 1 ===")
    game.score_point("Alice")
    game.score_point("Alice")
    game.score_point("Alice")
    game.score_point("Alice")
    game.print_score()

    # Play second game
    print("\n=== Game 2 ===")
    game.reset_game()
    game.score_point("Bob")
    game.score_point("Bob")
    game.score_point("Bob")
    game.score_point("Bob")
    game.print_score()
