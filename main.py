from tkinter import *
import pandas
import random

LIGHT_GREEN = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


# ------------------ Button Functions ----------------------#

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


def flip_card():
    pass


# -------------------GUI SETUP -----------------------------#




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=LIGHT_GREEN)
canvas = Canvas(width=800, height=526, bg=LIGHT_GREEN, highlightthickness=0)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

btn_right = Button(image=right_image, highlightthickness=0, command=next_card)
btn_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)

canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

btn_right.grid(row=1, column=0)
btn_wrong.grid(row=1, column=1)


next_card()

window.mainloop()