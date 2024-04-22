from tkinter import *
def button_is_pressed():
    val=text_box.get()
    result.config(text=round(int(val)*1.6,2))

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300,height=100)
window.maxsize(width=300,height=100)
window.config(padx=60,pady=10)

text_box = Entry(width=7)
text_box.grid(row=0,column=1)
nw1= Label(text="Miles")
nw1.grid(row=0,column=2)
nw2= Label(text="is equal to")
nw2.grid(row=1,column=0)
result = Label(text="0",font="bold")
result.grid(row=1,column=1)
nw3= Label(text="Km")
nw3.grid(row=1,column=2)
calc = Button(text="Calculate", command=button_is_pressed)
calc.grid(row=2,column=1)











window.mainloop()