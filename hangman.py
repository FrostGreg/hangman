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

        return not self.running

    def main(self, guess):
        if guess in self.choice:
            idx = self.choice.find(guess)
            self.x = self.x[:idx] + guess + self.x[idx+1:]
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses == 7:
                self.running = False
                print("\n######\nHANGMAN\n######\n You have lost the word was: " + self.choice)
            else:
                print("guess was incorrect\nHANGMAN progression: " + self.DEAD[:self.incorrect_guesses])
        self.has_won()
