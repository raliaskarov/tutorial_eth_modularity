"""
Level 1 MODULAR: Add Player Names (Facade Pattern)
===================================================

Modular version with player names using the Facade pattern.
- Player class includes name and score
- ScoreDisplay manages game state and display
- TennisFacade provides simple interface
"""


class Player:
    """Represents a player with name and score."""

    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_point(self):
        """Increment score by 1."""
        self.score += 1

    def get_score(self):
        """Return current score."""
        return self.score

    def get_name(self):
        """Return player name."""
        return self.name

    def reset_score(self):
        """Reset score to 0."""
        self.score = 0


class ScoreDisplay:
    """Handles score display and game state management."""

    def __init__(self):
        self.winner = None

    def display(self, player1, player2):
        """Display the current score and determine game over state."""
        # Check if game is over and store winner
        if player1.get_score() >= 4 or player2.get_score() >= 4:
            if self.winner is None:
                self.winner = player1.get_name() if player1.get_score() > player2.get_score() else player2.get_name()

        # Display score
        print(f"{player1.get_name()}: {player1.get_score()}, {player2.get_name()}: {player2.get_score()}")
        if self.winner is not None:
            print(f"Game Over! Winner: {self.winner}")

    def is_game_over(self, player1, player2):
        """Check if game is over based on current scores."""
        return player1.get_score() >= 4 or player2.get_score() >= 4

    def reset(self):
        """Reset game state."""
        self.winner = None


class TennisFacade:
    """
    Facade that provides a simple interface to the tennis game.
    Hides the complexity of Player and ScoreDisplay.
    """

    def __init__(self, name1, name2):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.display = ScoreDisplay()

    def score_point(self, name):
        """Score a point for the named player."""
        if self.display.is_game_over(self.player1, self.player2):
            return

        if name == self.player1.get_name():
            self.player1.score_point()
        elif name == self.player2.get_name():
            self.player2.score_point()
        else:
            raise ValueError(f"Unknown player: {name}")

    def print_score(self):
        """Display the current score."""
        self.display.display(self.player1, self.player2)

    def reset_game(self):
        """Reset the game to initial state."""
        self.player1.reset_score()
        self.player2.reset_score()
        self.display.reset()


if __name__ == "__main__":
    game = TennisFacade("Alice", "Bob")
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
