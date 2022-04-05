''' Week 9 TimesTable Task '''

from tkinter import *
import random

class Window:
    def __init__(self, root):
        self.root = root

        self.main_frame = Frame(root)
        self.main_frame.grid()

        self.equation = Equation()

        self.question_label = Label(self.main_frame, text = self.equation.question())
        self.question_label.grid()

        self.entry = Entry(root)
        self.entry.grid()

        btn1 = Button(self.main_frame, text = "Check Answer", command = self.check_answer)
        btn1.grid()

        btn2 = Button(self.main_frame, text = "Next", command = self.next_equation)
        btn2.grid()

        self.answer_label = Label(self.main_frame, text = "")
        self.answer_label.grid()

    def check_answer(self):
        self.answer_label["text"] = "Correct" if self.equation.check_answer(int(self.entry.get())) else "Incorrect"

    def next_equation(self):
        self.answer_label["text"] = ""
        self.equation = Equation()
        self.question_label["text"] = self.equation.question()


class Equation():
    def __init__(self):
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def check_answer(self, answer):
        return answer == self.x * self.y
    
    def question(self):
        return f"{self.x} * {self.y}"

if __name__ == '__main__':
    root = Tk()
    root.title("Quiz Task")
    Window(root)
    root.update()
    root.mainloop()