from tkinter import *
from tkinter import messagebox
from random import choice
import pandas
import json

BACKGROUND_COLOR = "#B1DDC6"
timer = None
PRESENTED_WORD = ""

try:
    with open("data/words_to_learn.json", "r") as file1:
        data = json.load(file1)
except FileNotFoundError:
    data = pandas.read_csv("data/en_1000_mostFrequentWords.csv")
    data = data.to_dict(orient = "records")

def flip_card():
    canvas.itemconfigure(canvas_image, image = back_card)
    canvas.itemconfigure(language, text = "Español", fill = "white")
    canvas.itemconfigure(word, text = PRESENTED_WORD["Spanish"], fill = "white")

    
def advance_timer():
    global timer
    timer = window.after(3000, flip_card)

    
def refresh_word():
    global PRESENTED_WORD
    global timer
    if timer != None:
        timer = window.after_cancel(timer)
    PRESENTED_WORD = choice(data)
    canvas.itemconfigure(canvas_image, image = front_card)
    canvas.itemconfigure(language, text = "English", fill = "black")
    canvas.itemconfigure(word, text = PRESENTED_WORD["English"], fill = "black")
    advance_timer()


def remove_word():
    global data
    data.remove(PRESENTED_WORD)
    refresh_word()


def on_closing():
    if messagebox.askokcancel("Cerrar", "Quires guardar tu avance?"):
        with open("data/words_to_learn.json", "w") as file1:
            json.dump(data, file1, indent = 4)
        window.destroy()

# ------------------- GUI ------------------------ #
window = Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(height = 526, width = 800, bg = BACKGROUND_COLOR, highlightthickness = 0)
front_card = PhotoImage(file = "images/card_front.png")
back_card = PhotoImage(file = "images/card_back.png")
canvas_image = canvas.create_image(412, 273, image = front_card)
canvas.grid(row = 0, column = 0, columnspan = 2)

language = canvas.create_text(400, 150, text = "Language", font = ("Arial", 36, "italic"))
word = canvas.create_text(400, 263, text = "word", font = ("Arial", 40, "bold"))

correct_image = PhotoImage(file = "images/right.png")
correct_button = Button(image = correct_image, highlightthickness = 0, bg = BACKGROUND_COLOR, command = remove_word)
correct_button.grid(row = 1, column = 1)

wrong_image = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness = 0, bg = BACKGROUND_COLOR, command = refresh_word)
wrong_button.grid(row = 1, column = 0)

refresh_word()


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
