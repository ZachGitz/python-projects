THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.score=0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz!!")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.canvas = Canvas(width=300, height=250,bg="White")
        self.ques_t = self.canvas.create_text(150,125,text="Question Here",font=("Arial", 20, "italic"),width=280)

        self.scoretx = Label(text=f"Score: {self.score}",bg=THEME_COLOR,font=("Arial", 10, "bold"),fg="White")
        self.scoretx.grid(row=0, column=1,pady=20)

        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        right_img = PhotoImage(file="images/true.png")
        self.rightb = Button(image=right_img,highlightthickness=0,command=self.right)
        self.rightb.grid(row=2, column=1,pady=20)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrongb = Button(image=wrong_img,highlightthickness=0,command=self.wrong)
        self.wrongb.grid(row=2, column=0,pady=20)
        self.next_ques()

        self.window.mainloop()

    def next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            ques = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_t,text=ques)
        else:
            self.rightb.config(state="disable")
            self.wrongb.config(state="disable")
            self.canvas.itemconfig(self.ques_t,text=f"You have reached the end of the Quiz.\n Your score is {self.score}/ 10")


    def right(self):
        self.feedback("true")


    def wrong(self):
        self.feedback("false")

    def feedback(self,ans:str):
        if self.quiz.check_answer(ans):
            self.canvas.config(bg="green")
            self.score+=1
            self.scoretx.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,func=self.next_ques)
