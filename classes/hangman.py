import random


class Hangman:
    def __init__(self):
        self.DEAD = "HANGMAN"

        words = ["cheese", "eggs", "shoes", "film", "computer", "yellow", "happy", "elephant", "stadium", "basketball",
                 "art", "pillow"]
        self.incorrect_guesses = 0
        self.choice = random.choice(words)
        self.x = "-" * len(self.choice)
        self.running = True

    def has_won(self):
        if self.x == self.choice:
            self.running = False

    def main(self, guess):
        out = ""
        if guess in self.choice:
            positions = [x for x in range(len(self.choice)) if self.choice[x] == guess]
            for idx in positions:
                self.x = self.x[:idx] + guess + self.x[idx+1:]
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses == 7:
                self.running = False
            else:
                out = "Guess was incorrect"
        self.has_won()
        return out
