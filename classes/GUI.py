import tkinter as tk
from classes import hangman


class Interface:
    def __init__(self):
        self.game = hangman.Hangman()
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Hangman")

        self.title = tk.Label(self.root, text="HANGMAN")
        self.title.grid(row=1, column=2, ipadx=75)

        self.result_lbl = tk.Label(self.root, text="")
        self.result_lbl.grid(row=2, column=2)

        self.target_word = tk.Label(self.root, text=self.game.x)
        self.target_word.grid(row=3, column=2)

        self.user_guess = tk.Entry(self.root)
        self.user_guess.grid(row=4, column=2)

        self.submit_btn = tk.Button(self.root, text="Submit", command=self.get_input)
        self.submit_btn.grid(row=4, column=3)

        self.feedback = tk.Label(self.root, text="")
        self.feedback.grid(row=5, column=2)

        self.progress = tk.Label(self.root, text="")
        self.progress.grid(row=6, column=2)

        self.root.mainloop()

    def update(self):
        self.target_word.configure(text=self.game.x)
        self.progress.configure(text=self.game.DEAD[:self.game.incorrect_guesses])
        if self.game.x == self.game.choice:
            self.result_lbl.configure(text="Congrats you guessed correctly :)")
        elif not self.game.running:
            self.result_lbl.configure(text="Unlucky you didn't get it")
            self.target_word.configure(text=self.game.choice)

    def get_input(self):
        guess = self.user_guess.get()
        out = ""
        if any(char.isdigit() for char in guess):
            out += "No numbers\n"
        elif len(guess) == 1:
            out = self.game.main(guess)
        else:
            out += "1 character only"
        self.feedback.configure(text=out)
        self.user_guess.delete(0, tk.END)
        self.update()
