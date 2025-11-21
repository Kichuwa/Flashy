from tkinter import *
import pandas
import random

LIGHT_GREEN = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# ------------------ Button Functions ----------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)



# -------------------GUI SETUP -----------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=LIGHT_GREEN)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=LIGHT_GREEN, highlightthickness=0)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

btn_right = Button(image=right_image, highlightthickness=0, command=next_card)
btn_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)

card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

btn_right.grid(row=1, column=0)
btn_wrong.grid(row=1, column=1)


next_card()

window.mainloop()