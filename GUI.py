import tkinter as tk
import hangman


def update():
    targetword.configure(text=newgame.x)
    if newgame.x == newgame.choice:
        resultlbl.configure(text="Congrats you guessed correctly :)")


def getinput():
    guess = userguess.get()
    newgame.maincode(guess)
    update()


newgame = hangman.game()
root = tk.Tk()
root.geometry("400x300")

title = tk.Label(root, text="HANGMAN")
title.grid(row=1, column=2, ipadx=75)

resultlbl = tk.Label(root, text="")
resultlbl.grid(row=2, column=2)

targetword = tk.Label(root, text=newgame.x)
targetword.grid(row=3, column=2)

userguess = tk.Entry(root)
userguess.grid(row=4, column=2)

submitbtn = tk.Button(root, text="Submit", command=getinput)
submitbtn.grid(row=4, column=3)

root.mainloop()
