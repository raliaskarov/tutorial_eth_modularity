"""
Level 2 MODULAR: Official Tennis Score Display (Facade Pattern)
================================================================

Modular version with official tennis terminology using Facade pattern.
- ScoreFormatter handles tennis terminology
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


class ScoreFormatter:
    """Formats scores using tennis terminology."""

    SCORE_NAMES = ["love", "fifteen", "thirty", "forty"]

    @staticmethod
    def format_score(score):
        """Format a single score value."""
        if score < 4:
            return ScoreFormatter.SCORE_NAMES[score]
        return str(score)


class ScoreDisplay:
    """Handles score display with tennis terminology and game state."""

    def __init__(self):
        self.formatter = ScoreFormatter()
        self.winner = None

    def display(self, player1, player2):
        """Display the current score and determine game over state."""
        # Check if game is over and store winner
        if player1.get_score() >= 4 or player2.get_score() >= 4:
            if self.winner is None:
                self.winner = player1.get_name() if player1.get_score() > player2.get_score() else player2.get_name()

        # Display score
        if self.winner is not None:
            print(f"Game: {self.winner}")
        elif player1.get_score() == player2.get_score() and player1.get_score() < 4:
            print(f"{self.formatter.format_score(player1.get_score())} all")
        else:
            p1_display = self.formatter.format_score(player1.get_score())
            p2_display = self.formatter.format_score(player2.get_score())
            print(f"{player1.get_name()}: {p1_display}, {player2.get_name()}: {p2_display}")

    def is_game_over(self, player1, player2):
        """Check if game is over based on current scores."""
        return player1.get_score() >= 4 or player2.get_score() >= 4

    def reset(self):
        """Reset game state."""
        self.winner = None


class TennisFacade:
    """
    Facade that provides a simple interface to the tennis game.
    Hides the complexity of Player, ScoreFormatter, and ScoreDisplay.
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
