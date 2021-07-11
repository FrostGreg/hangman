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

        self.root.mainloop()

    def update(self):
        self.target_word.configure(text=self.game.x)
        if self.game.x == self.game.choice:
            self.result_lbl.configure(text="Congrats you guessed correctly :)")

    def get_input(self):
        guess = self.user_guess.get()
        self.game.main(guess)
        self.update()


