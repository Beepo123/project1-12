from random import randint

class GuessNumberGame:
    """A game where player guess the number chosen by computer"""
    def __init__(self):
        self.number = randint(0,10)
        self.guess = None
        
    def play_game(self):
        while not self.guess == self.number:
            self.guess = int(input("enter number: "))

        print("you won")

game = GuessNumberGame()
game.play_game()