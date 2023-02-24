import tkinter as tk
from tkinter import ttk
import random

class InfinitiveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.width = 600 
        self.height = 300

        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2) 

        self.correct = 0
        self.incorrect = 0
        
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.label1 = tk.Label(self, text= "Infinitive", font=('Helvetica 15 bold'))
        self.label1.pack()

        self.label_question = tk.Label(self, font=('Helvetica 12'))
        self.label_question.pack()

        self.input_text = tk.Entry(self, width=50)
        self.input_text.pack(pady=5)

        self.correct_label = tk.Label(self, text=f'Correct: {self.correct}', font=('Helvetica 10'), fg="green")
        self.correct_label.pack()

        self.incorrect_label = tk.Label(self, text=f'Incorrect: {self.incorrect}', font=('Helvetica 10'), fg="red")
        self.incorrect_label.pack()

        self.num_back_button = ttk.Button(self, text="back", command=lambda: self.back(parent))
        self.num_back_button.pack(pady=10)

        self.quit_num_button = ttk.Button(self, text="quit", command=parent.destroy)
        self.quit_num_button.pack()

        self.verbs = self.get_verbs()
        self.redo_list = []
        self.min = 0
        self.max = len(self.verbs) - 1

        self.verb_index = random.randint(self.min, self.max)
        self.verb = self.verbs[self.verb_index].split('=')

        self.answer = self.verb[0]
        
        self.update_form_label()
        self.bind('<Return>', self.keypress_return)

    def back (self, parent):
        self.destroy()
        parent.deiconify()
    
    def update_form_label(self):
        self.label_question.config(text=self.verb[1], fg="black", font=('Helvetica 12'))

    def keypress_return(self, event):
        if self.input_text.get().strip() == self.answer.strip():
            self.correct += 1
            self.label_question.config(text="Correct", font=('Helvetica 12') ,fg="green")
            self.correct_label.config(text=f'Correct: {self.correct}')
            self.after(1000, self.update_answer, True)
        else:
            self.incorrect += 1
            self.incorrect_label.config(text=f'Incorrect: {self.incorrect}')
            self.label_question.config(text=self.answer, font=('Helvetica 12'), fg="red")
            self.label_question.after(1500, self.update_answer, False)

    def update_answer(self, is_correct):
        if not is_correct: self.redo_list.append(self.verb)
        if self.verbs: del self.verbs[self.verb_index]
        if not self.verbs:
            if self.redo_list:
                self.verb_index = random.randint(self.min, len(self.redo_list) - 1)
                self.verb = self.redo_list[self.verb_index]
                self.answer = self.verb[0]
                self.redo_list.remove(self.verb)

                self.update_form_label()
                self.input_text.delete(0,'end')
            else:
                self.verbs = self.get_verbs()
                self.verb_index = random.randint(self.min, len(self.verbs) - 1)
                self.verb = self.verbs[self.verb_index].split('=')
                self.answer = self.verb[0]

                self.update_form_label()
                self.input_text.delete(0,'end')

        else:
            self.verb_index = random.randint(self.min, len(self.verbs) - 1)
            self.verb = self.verbs[self.verb_index].split('=')
            self.answer = self.verb[0]

            self.update_form_label()
            self.input_text.delete(0,'end')


    def get_verbs(self):
        fname = "data/infinitive.txt"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.splitlines()