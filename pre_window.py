import tkinter as tk
from tkinter import ttk
import random

class VerbWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.width = 600 
        self.height = 300

        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2) 
        
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.label1 = tk.Label(self, text= "Verbs", font=('Helvetica 15 bold'))
        self.label1.pack()

        # self.number = random.randint(self.min, self.max)

        self.label_question = tk.Label(self, text="What is "  + " in Portuguese?", font=('Helvetica 10'))
        self.label_question.pack()

        self.input_text = tk.Entry(self, width=50)
        self.input_text.pack(pady=5)

        self.num_back_button = ttk.Button(self, text="back", command=lambda: self.back(parent))
        self.num_back_button.pack(pady=10)

        self.quit_num_button = ttk.Button(self, text="quit", command=parent.destroy)
        self.quit_num_button.pack()

        self.verbs = self.get_verbs()
        self.min = 0
        self.max = len(self.verbs)

        self.verb_index = random.randint(self.min, self.max)
        self.verb = self.verbs[self.verb_index].split(',')

        self.form_index = 0
        self.answer = self.verb[self.form_index]

    def back (self, parent):
        self.destroy()
        parent.deiconify()

    def keypress_return(self, event):
        if self.input_text.get().strip() == self.answer:
            self.label_question.config(text="Correct", fg="green")
            #self.after(1000, self.update_number)
        else:
            self.label_question.config(text=self.answer, font=('Helvetica 10'), fg="red")
            #self.label_question.after(4000, self.update_number)

    def get_verbs(self):
        fname = "scripts/test.txt"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.splitlines()