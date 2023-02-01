from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """
        This is the window class for the quiz app.
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question = self.canvas.create_text(150, 125, text = "", font = ("Arial", 20, "italic"), fill = THEME_COLOR, width = 280)
        self.canvas.grid(row = 1, column = 0, columnspan=2, pady = 50)

        true_image = PhotoImage(file = "images/true.png")
        self.true_button = Button(image = true_image, highlightthickness = 0, command = self.answer_true)
        self.true_button.grid(row = 2, column = 0)

        false_image = PhotoImage(file = "images/false.png")
        self.false_button = Button(image = false_image, highlightthickness = 0, command = self.answer_false)
        self.false_button.grid(row = 2, column = 1)


        self.refresh_question()

        self.window.mainloop()


    def refresh_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.score_label.config(text = f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text = f"{question_text}")
        else:
            self.canvas.itemconfig(self.question, text = "You finished the questionnaire")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")


    def answer_true(self):
        user_answer = "true"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
        


    def answer_false(self):
        user_answer = "false"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
        


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(700, self.refresh_question)
