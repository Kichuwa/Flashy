from tkinter import *

LIGHT_GREEN = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=LIGHT_GREEN)
canvas = Canvas(width=800, height=526, bg=LIGHT_GREEN, highlightthickness=0)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

btn_right = Button(image=right_image, highlightthickness=0)
btn_wrong = Button(image=wrong_image, highlightthickness=0)

canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

btn_right.grid(row=1, column=0)
btn_wrong.grid(row=1, column=1)



window.mainloop()