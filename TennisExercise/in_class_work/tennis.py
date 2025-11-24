# tennis_monolithic.py
class Tennis:
    
    def __init__(self, name1, name2, language="EN"):
        self.name1 = name1
        self.name2 = name2
        self.score1 = 0
        self.score2 = 0
        self.games_won1 = 0
        self.games_won2 = 0
        self.game_over = False
        self.score_codes = {
            "EN": ["love", "fifteen", "thirty", "forty", "game"],
            "DE": ["Liebe", "fünfzehn", "dreissig", "vierzig", "Spiel"]
            }
        self.vocabulary = {
            "EN": {
                "score_codes":["love", "fifteen", "thirty", "forty", "game"],
                "equal_code": "all",
                "game": "Game",
                "games_score": "Games Score",
                "winner": "Winner"
                },
            "DE": {
                "score_codes": ["Liebe", "fünfzehn", "dreissig", "vierzig", "Spiel"],
                "equal_code": "beide",
                "game": "Spiel",
                "games_score": "Spielstand",
                "winner": "Gewinner"
                }
            }
        self.winner = None
        self.language = language

    def display(self):
        voc = self.vocabulary[self.language]
        if self.game_over:
            print(f"{voc["game"]}. {voc["winner"]}: {self.winner}"
                "\n"
                f"{voc["games_score"]}: {self.name1}: {self.games_won1} / {self.name2}: {self.games_won2}"
                )
        else:
            code1 = voc["score_codes"][self.score1]
            code2 = voc["score_codes"][self.score2]
            if code1 == code2:
                print(f"{code1} {voc["equal_code"]}")
            else:
                print(f"{self.name1} : {code1} -  {self.name2} : {code2}")
        

    def score_point(self, name):

        if self.game_over:
            print("Error recording points. Game over. No new points not recorded")
            return

        if self.name1 == name:
            self.score1 += 1
        elif self.name2 == name:
            self.score2 += 1
        else:
            raise ValueError("Name not found")

        # check if someone won
        if self.score1 >= 4:
            self.game_over = True
            self.games_won1 += 1
            self.winner = self.name1
        if self.score2 >= 4:
            self.game_over = True
            self.games_won2 += 1      
            self.winner = self.name2   

    def reset(self):
        self.score1 = 0
        self.score2 = 0
        self.game_over = False
        self.winner = None

if __name__ == "__main__":
    # initialize the game
    game = Tennis("Marcel", "Carlos", "DE")

    print("=============== Game 1 ================")
    game.display()
    game.score_point("Marcel")
    game.display()
    game.score_point("Carlos")
    game.display()
    game.score_point("Marcel")
    game.display()
    game.score_point("Marcel")
    game.display()
    game.score_point("Marcel")
    game.display()

    print("=============== Game 2 ================")
    game.reset()
    game.display()
    game.score_point("Carlos")
    game.display()
    game.score_point("Carlos")
    game.display()
    game.score_point("Marcel")
    game.display()
    game.score_point("Carlos")
    game.display()
    game.score_point("Carlos")
    game.display() 


# TODO: how many games played so far
# TODO: multi-language (DE and EN)