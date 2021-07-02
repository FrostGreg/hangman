import random

class game:
    def __init__(self):
        words = ["cheese", "eggs", "shoes", "film", "computer", "yellow", "happy", "elephant", "stadium", "basketball",
                 "art", "pillow"]
        self.y = 0
        self.dead = "HANGMAN"
        self.choice = random.choice(words)
        self.x = self.createWordline()
        self.running = True


    def createWordline(self):
        x = ""
        for letter in self.choice:
            x += "_"
        return x

    def checkWin(self):
        if self.x == self.choice:
            self.running = False
            return True
        else:
            return False


    def maincode(self, guess):
        i = 0
        if guess in self.choice:
            for letter in self.choice:
                if letter == guess:
                    foo = self.choice.find(letter, i)
                    self.x = self.x[:foo] + letter + self.x[foo + 1:]
                    i += 1
                else:
                    i += 1
        else:
            self.y += 1
            if self.y == 7:
                self.running = False
                print("\n######\nHANGMAN\n######\n You have lost the word was: " + self.choice)
            else:
                print("guess was incorrect")
                print("HANGMAN progression: " + self.dead[:self.y])
        self.checkWin()


