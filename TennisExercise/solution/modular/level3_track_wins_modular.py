"""
Level 3 MODULAR: Track Total Games Won (Facade Pattern)
========================================================

Modular version with win tracking using Facade pattern.
- Player tracks games won
- ScoreDisplay manages game state and shows games won in parentheses
- TennisFacade provides simple interface
"""


class Player:
    """Represents a player with name, score, and games won."""

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_won = 0

    def score_point(self):
        self.score += 1

    def win_game(self):
        """Increment games won counter."""
        self.games_won += 1

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_games_won(self):
        """Get total games won."""
        return self.games_won

    def reset_score(self):
        self.score = 0


class ScoreFormatter:
    """Formats scores using tennis terminology."""

    SCORE_NAMES = ["love", "fifteen", "thirty", "forty"]

    def format_score(self, score):
        if score < 4:
            return self.SCORE_NAMES[score]
        return str(score)


class ScoreDisplay:
    """Handles score display with games won tracking and game state."""

    def __init__(self):
        self.formatter = ScoreFormatter()
        self.winner = None

    def display(self, player1, player2):
        """Display the current score with games won in parentheses."""
        # Check if game is over and update winner
        if player1.get_score() >= 4 or player2.get_score() >= 4:
            if self.winner is None:
                if player1.get_score() > player2.get_score():
                    self.winner = player1
                    player1.win_game()
                else:
                    self.winner = player2
                    player2.win_game()

        # Display score
        if self.winner is not None:
            print(f"Game: {self.winner.get_name()} ({player1.get_games_won()}-{player2.get_games_won()})")
        elif player1.get_score() == player2.get_score() and player1.get_score() < 4:
            score_display = self.formatter.format_score(player1.get_score())
            print(f"{score_display} all ({player1.get_games_won()}-{player2.get_games_won()})")
        else:
            p1_display = self.formatter.format_score(player1.get_score())
            p2_display = self.formatter.format_score(player2.get_score())
            print(f"{player1.get_name()} ({player1.get_games_won()}): {p1_display}, {player2.get_name()} ({player2.get_games_won()}): {p2_display}")

    def is_game_over(self, player1, player2):
        """Check if game is over based on current scores."""
        return player1.get_score() >= 4 or player2.get_score() >= 4

    def reset(self):
        """Reset game state."""
        self.winner = None


class TennisFacade:
    """
    Facade that provides a simple interface to the tennis game with win tracking.
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
        """Reset the current game (but keep games won counter)."""
        self.player1.reset_score()
        self.player2.reset_score()
        self.display.reset()


if __name__ == "__main__":
    game = TennisFacade("Alice", "Bob")

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
