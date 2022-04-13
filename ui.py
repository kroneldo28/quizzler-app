from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_canvas = self.canvas.create_text(150, 125, text="Question", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightbackground=THEME_COLOR, command=self.check_true)
        self.button_true.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightbackground=THEME_COLOR, command=self.check_false)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.question_canvas,
                                   text=f"You reached the end of the quiz! You score is {self.quiz.score}")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
