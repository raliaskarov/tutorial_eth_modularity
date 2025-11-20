"""
Level 4 MONOLITHIC: Multi-Language Support + Win Tracking
==========================================================

Monolithic version with language switching and win tracking (English/German).
- Can change language during the game
- Supports English and German
- Tracks total games won by each player
- All logic still in one class
"""


class Tennis:
    """Monolithic tennis game with multi-language support and win tracking."""

    def __init__(self, name1, name2, language="English"):
        self.player1_name = name1
        self.player2_name = name2
        self.player1_score = 0
        self.player2_score = 0
        self.player1_games_won = 0
        self.player2_games_won = 0
        self.game_over = False
        self.winner = None
        self.language = language

        # Score names in different languages
        self.score_names_en = ["love", "fifteen", "thirty", "forty"]
        self.score_names_de = ["null", "fünfzehn", "dreißig", "vierzig"]

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

    def set_language(self, language):
        """Change the display language."""
        if language not in ["English", "German"]:
            raise ValueError("Language must be 'English' or 'German'")
        self.language = language

    def _get_score_names(self):
        """Get the score names for the current language."""
        if self.language == "English":
            return self.score_names_en
        else:
            return self.score_names_de

    def _get_game_text(self):
        """Get 'Game' text in current language."""
        return "Game" if self.language == "English" else "Spiel"

    def _get_all_text(self):
        """Get 'all' text in current language."""
        return "all" if self.language == "English" else "beide"

    def print_score(self):
        """Display the current score in the selected language."""
        score_names = self._get_score_names()

        if self.game_over:
            game_text = self._get_game_text()
            print(f"{game_text}: {self.winner} ({self.player1_games_won}-{self.player2_games_won})")
        elif self.player1_score == self.player2_score and self.player1_score < 4:
            all_text = self._get_all_text()
            print(f"{score_names[self.player1_score]} {all_text} ({self.player1_games_won}-{self.player2_games_won})")
        else:
            p1_display = score_names[self.player1_score] if self.player1_score < 4 else str(self.player1_score)
            p2_display = score_names[self.player2_score] if self.player2_score < 4 else str(self.player2_score)
            print(f"{self.player1_name} ({self.player1_games_won}): {p1_display}, {self.player2_name} ({self.player2_games_won}): {p2_display}")

    def reset_game(self):
        """Reset the current game (but keep games won counter)."""
        self.player1_score = 0
        self.player2_score = 0
        self.game_over = False
        self.winner = None


if __name__ == "__main__":
    game = Tennis("Alice", "Bob", "English")

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

    # Switch to German and show score
    print("\n--- Switching to German ---")
    game.set_language("German")
    game.print_score()
