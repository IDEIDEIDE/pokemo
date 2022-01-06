#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:14:33 2022

@author: clockshield
"""


from tkinter import *
import random
from PIL import ImageTk, Image
root=Tk()
root.title("lol")
root.geometry("600x400")
root.config(bg="orange")

label_player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
label_player1.place(relx = 0.2, rely = 0.3, anchor=CENTER)

label_player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
label_player2.place(relx = 0.8, rely = 0.3, anchor=CENTER)

label_score1 = Label(root, bg = "royal blue", fg = "white")
label_score1.place(relx = 0.2, rely = 0.4, anchor=CENTER)

label_score2 = Label(root, bg = "royal blue", fg = "white")
label_score2.place(relx = 0.8, rely = 0.4, anchor=CENTER)

label_randomdice = Label(root, bg = "white", fg = "blue")
label_randomdice.place(relx = 0.5, rely = 0.3, anchor=CENTER)






root.mainloop()