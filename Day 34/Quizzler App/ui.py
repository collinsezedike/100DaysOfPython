from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=25, pady=25, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12))

        self.score_label.grid(row=0, column=1, padx=(90, 0))

        self.canvas = Canvas(width=300, height=300, bg='white')
        self.text = self.canvas.create_text(
            150,
            150,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(10, 50))

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answered_true)
        self.true_button.grid(row=2, column=0, padx=25)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answered_false)
        self.false_button.grid(row=2, column=1, padx=25)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.change_canvas_color("white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)

        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz"
                                                   f"\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answered_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answered_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def change_canvas_color(self, color):
        self.canvas.config(bg=color)

    def give_feedback(self, is_correct):
        if is_correct:
            self.change_canvas_color("green")
        else:
            self.change_canvas_color("red")
        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")

