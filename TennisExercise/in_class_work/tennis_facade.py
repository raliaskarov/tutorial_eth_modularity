# tennis_facade.py
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_point(self):
        self.score += 1

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def reset(self):
        self.score = 0

class GameBoard:

    def __init__(self, player1: Player, player2: Player):
        self.winner = None
        self.game_over = False
        self.player1=player1
        self.player2=player2

    def point_to(self, player_id: int):
        
        # define player
        if player_id == 1:
            player = self.player1
        elif player_id == 2:
            player = self.player2
        else:
            raise ValueError("Invalid player ID. Must be 1 or 2")

        if self.game_over:
            return

        # score point
        player.score_point()

        # check for winner
        if player.get_score() >= 4:
            self.game_over = True
            self.winner = player.get_name()

class Tennis:

    def __init__(self, name1, name2):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.board = GameBoard(self.player1, self.player2)

    def point_to(self, player_id):
        self.board.point_to(player_id)

    def display(self):
        if self.board.game_over:
            print(f"Game over. Winner: {self.board.winner}")
        else:
            print(f"{self.player1.get_name()} : {self.player1.get_score()} | {self.player2.get_name()} : {self.player2.get_score()}")

if __name__ == "__main__":
    score = Tennis("Marcel", "Carlos")
    score.display()
    score.point_to(1)
    score.display()
    score.point_to(2)
    score.display()
    score.point_to(1)
    score.display()
    score.point_to(1)
    score.display()
    score.point_to(1)
    score.display()
