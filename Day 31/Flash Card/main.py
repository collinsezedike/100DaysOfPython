from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# TODO 4: Remove known words from te words database
def remove_word():
    global words
    words.remove(current_word)
    pick_word()


# TODO 2: Generate and assign a random word to title
current_word = {}


def pick_word():
    global current_word, change_card
    window.after_cancel(change_card)
    canvas.itemconfig(image, image=FRONT_IMAGE)
    canvas.itemconfig(title, text="French", fill="black")
    current_word = random.choice(words)
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    change_card = window.after(3000, flip_card, current_word)


# TODO 3: Flip card
def flip_card(current_card):
    canvas.itemconfig(image, image=BACK_IMAGE)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# TODO 1:  Create the interface
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
FRONT_IMAGE = PhotoImage(file="images/card_front.png")
BACK_IMAGE = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 265, image=FRONT_IMAGE)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 300, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=pick_word)
no_button.grid(row=1, column=0)

yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=remove_word)
yes_button.grid(row=1, column=1)


# TODO 5: Save unknown words to words_to_learn.csv and read from it if it exists
# Read the csv file
data_df = pandas.read_csv("data/french_words.csv")
words = data_df.to_dict(orient="records")
# words is a LIST of DICTIONARIES
# the language is the key and the word is the value

try:
    data_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_df = pandas.read_csv("data/french_words.csv")
finally:
    words = data_df.to_dict(orient="records")

change_card = window.after(3000, flip_card, current_word)
pick_word()
window.mainloop()

# save the unknown words to words_to_learn.csv
new_data = pandas.DataFrame(words)
new_data.to_csv("data/words_to_learn.csv", index=False)
