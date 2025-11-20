"""
Level 2 MONOLITHIC: Official Tennis Score Display
==================================================

TODO: Add official tennis terminology to score display.

Your tasks:
1. Add score_names list to __init__: ["love", "fifteen", "thirty", "forty"]
2. Modify print_score() to use tennis terminology instead of numbers
3. Handle tied scores (e.g., "love all", "fifteen all")
4. Use numeric display for scores >= 4

Expected output:
    Alice: fifteen, Bob: love
    Alice: thirty, Bob: love
    Game: Alice
"""


class Tennis:
    """Monolithic tennis game with official score display."""

    def __init__(self, name1, name2):
        self.player1_name = name1
        self.player2_name = name2
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.winner = None
        # TODO: Add score_names = ["love", "fifteen", "thirty", "forty"]

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
        """Display the current score with tennis terminology."""
        # TODO: Implement tennis terminology display
        # Hint 1: Check if game_over first
        # Hint 2: Check for tied scores (both players have same score < 4)
        # Hint 3: For scores < 4, use score_names[score]
        # Hint 4: For scores >= 4, use str(score)
        pass

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
