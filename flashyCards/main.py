BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/wrds_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")

dict = data.to_dict(orient="records")

def cards():
    global wrd, timer
    window.after_cancel(timer)
    wrd = random.choice(dict)
    canvas.itemconfig(cardtitle,text="French",fill="black")
    canvas.itemconfig(cardwrd, text=wrd["French"],fill="black")
    canvas.itemconfig(canvas_image, image=cardimgfrnt)
    timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(cardtitle, text="English",fill="white")
    canvas.itemconfig(cardwrd, text=wrd["English"],fill="white")
    canvas.itemconfig(canvas_image,image=cardimgback)

def known_card():
    dict.remove(wrd)
    data = pandas.DataFrame(dict)
    data.to_csv("data/wrds_to_learn.csv",index=False)
    cards()



window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50,pady=50)




canvas = Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
cardimgfrnt = PhotoImage(file="./images/card_front.png")
cardimgback = PhotoImage(file="./images/card_back.png")
canvas_image =canvas.create_image(400,263,image=cardimgfrnt)
canvas.grid(row=0,column=0,columnspan=2)
cardtitle = canvas.create_text(400,150,text="lang",font=("Ariel",40,"italic"))
cardwrd =canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))



rghimg = PhotoImage(file="./images/right.png")
right = Button(image=rghimg, highlightthickness=0,bg=BACKGROUND_COLOR,command=known_card)
right.grid(row=1,column=1)

wrnimg = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrnimg, highlightthickness=0,bg=BACKGROUND_COLOR,command=cards)
wrong.grid(row=1,column=0)
timer = window.after(3000, func=flip_card)
cards()


window.mainloop()

