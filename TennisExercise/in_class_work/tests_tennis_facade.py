# tests_tennis_facade.py
import unittest
from .tennis_facade import Tennis

class TestTennis(unittest.TestCase):

    def test_invalid_player_id_after_game_over(self):
        game = Tennis("Marcel", "Carlos")

        # end the game
        for _ in range(4):
            game.point_to(1)

        self.assertTrue(game.board.game_over)

        with self.assertRaises(ValueError):
            game.point_to(3)


if __name__ == "__main__":
    unittest.main()
