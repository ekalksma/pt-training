import tkinter as tk
from tkinter import ttk
import random

class FuturoDoPreteritoWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.width = 600 
        self.height = 300

        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2) 
        
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.label1 = tk.Label(self, text= "Futuro do Pretérito (I would)", font=('Helvetica 15 bold'))
        self.label1.pack()

        self.verb_label = tk.Label(self, font=('Helvetica 12 bold'))
        self.verb_label.pack()

        self.label_question = tk.Label(self, font=('Helvetica 10'))
        self.label_question.pack()

        self.input_text = tk.Entry(self, width=50)
        self.input_text.pack(pady=5)

        self.num_back_button = ttk.Button(self, text="back", command=lambda: self.back(parent))
        self.num_back_button.pack(pady=10)

        self.quit_num_button = ttk.Button(self, text="quit", command=parent.destroy)
        self.quit_num_button.pack()

        self.verbs = self.get_verbs()
        self.min = 0
        self.max = len(self.verbs) - 1

        self.verb_index = random.randint(self.min, self.max)
        self.verb = self.verbs[self.verb_index].split(',')

        self.form_index = 1
        self.answer = self.verb[self.form_index]
        
        self.verb_label.config(text=f"Verb: {self.verb[0]}")
        self.update_form_label()
        self.bind('<Return>', self.keypress_return)

    def back (self, parent):
        self.destroy()
        parent.deiconify()
    
    def update_form_label(self):
        match self.form_index:
            case 1:
                self.label_question.config(text=f"eu:", fg="black")
            case 2:
                self.label_question.config(text=f"ele/ela:", fg="black")
            case 3:
                self.label_question.config(text=f"nós:", fg="black")
            case 4:
                self.label_question.config(text=f"eles/elas:", fg="black")

    def keypress_return(self, event):
        if self.input_text.get().strip() == self.answer:
            self.label_question.config(text="Correct", fg="green")
            self.after(1000, self.update_answer)
        else:
            self.label_question.config(text=self.answer, font=('Helvetica 10'), fg="red")
            self.label_question.after(1500, self.update_answer)

    def update_answer(self):
        self.form_index +=1
        if self.form_index > 4:
            del self.verbs[self.verb_index]
            if not self.verbs:
                self.verbs = self.get_verbs()

            self.verb_index = random.randint(self.min, len(self.verbs) - 1)
            self.verb = self.verbs[self.verb_index].split(',')
            self.verb_label.config(text=f"Verb: {self.verb[0]}")
            self.form_index = 1
            self.answer = self.verb[self.form_index]
        else:
            self.answer = self.verb[self.form_index]

        self.update_form_label()
        self.input_text.delete(0,'end')

    def get_verbs(self):
        fname = "data/futpret.txt"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.splitlines()