import tkinter as tk
from tkinter import ttk
import random

class NumbersWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.width = 600 
        self.height = 300
        self.data = self.get_data()
        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2) 
        
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.label1 = tk.Label(self, text= "Numbers", font=('Helvetica 15 bold'))
        self.label1.pack()

        self.min_label = tk.Label(self, text= "min", font=('Helvetica 10'))
        self.min_label.pack()

        self.input_min = tk.Entry(self, width= 5)
        self.input_min.insert(0,"-1")
        self.input_min.pack()

        self.max_label = tk.Label(self, text= "max", font=('Helvetica 10'))
        self.max_label.pack()

        self.input_max = tk.Entry(self, width= 5)
        self.input_max.insert(0,"10000")
        self.input_max.pack(pady=5)

        self.min = self.get_min(self.input_min.get())
        self.max = self.get_max(self.input_max.get())

        self.number = random.randint(self.min, self.max)
        self.answer = self.data[self.number]

        self.label_question = tk.Label(self, text="What is " + str(self.number) + " in Portuguese?", font=('Helvetica 10'))
        self.label_question.pack()

        self.input_text = tk.Entry(self, width=50)
        self.input_text.pack(pady=5)

        self.num_back_button = ttk.Button(self, text="back", command=lambda: self.back(parent))
        self.num_back_button.pack(pady=10)

        self.bind('<Return>', self.keypress_return)

        self.quit_num_button = ttk.Button(self, text="quit", command=parent.destroy)
        self.quit_num_button.pack()
    
    def get_min(self, min):
        if not min.isnumeric() or int(min) < -1 or int(min) > 10000:
            return -1
        return int(min)
    
    def get_max (self, max):
        if not max.isnumeric() or int(max) < -1 or int(max) > 10000:
            return 10000
        return int(max)

    def update_number(self):
        self.number =  random.randint(self.get_min(self.input_min.get()), self.get_max(self.input_max.get()))
        self.answer = self.data[self.number]
        self.label_question.config(text="What is " + str(self.number) + " in Portuguese?", fg="black", font=('Helvetica 10'))
        self.input_text.delete(0,'end')

    def back (self, parent):
        self.withdraw()
        parent.deiconify()

    def keypress_return(self, event):
        if self.input_text.get().strip() == self.answer:
            self.label_question.config(text="Correct", fg="green")
            self.after(1000, self.update_number)
        else:
            self.label_question.config(text=self.answer, font=('Helvetica 10'), fg="red")
            self.label_question.after(4000, self.update_number)

    def get_data(self):
        fname = "data/numbers.csv"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        return data.split(",")