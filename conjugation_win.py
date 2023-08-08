import tkinter as tk
from tkinter import ttk
import random

class ConjugationWindow(tk.Toplevel):
    def __init__(self, parent, filename, title):
        super().__init__(parent)

        self.width = 800
        self.height = 400
        
        self.filename = filename

        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, sticky="NWE")
        self.listbox_frame = tk.Frame(self.frame, pady=10)
        self.listbox_frame.grid(row=6, column=0)
        self.button_frame = tk.Frame(self.listbox_frame)
        self.button_frame.grid(row=0, column=1, padx=10)

        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2) 

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.correct = 0
        self.incorrect = 0
        
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.label1 = tk.Label(self.frame, text= title, font=('Helvetica 15 bold'))
        # self.label1.pack(fill="x")
        self.label1.grid(row=0,column=0, sticky="EW")

        self.verb_label = tk.Label(self.frame, font=('Helvetica 12 bold'))
        # self.verb_label.pack()
        self.verb_label.grid(row=1, column=0, sticky="EW")

        self.label_question = tk.Label(self.frame, font=('Helvetica 10'))
        # self.label_question.pack()
        self.label_question.grid(row=2, column=0, sticky="EW")

        self.input_text = tk.Entry(self.frame, width=50)
        # self.input_text.pack(pady=5)
        self.input_text.grid(row=3, column=0)

        self.correct_label = tk.Label(self.frame, text=f'Correct: {self.correct}', font=('Helvetica 10'), fg="green")
        # self.correct_label.pack()
        self.correct_label.grid(row=4, column=0)

        self.incorrect_label = tk.Label(self.frame, text=f'Incorrect: {self.incorrect}', font=('Helvetica 10'), fg="red")
        # self.incorrect_label.pack()
        self.incorrect_label.grid(row=5, column=0)

        self.listbox = tk.Listbox(self.listbox_frame, selectmode="extended")
        # self.listbox.pack(side="left", padx=5)
        self.listbox.grid(row=0, column=0)

        self.add_button = ttk.Button(self.button_frame, text="Add", command=lambda: self.add_verb())
        self.add_button.grid(row=0, column=0)
        # self.add_button.pack(side="left", padx=5)

        self.reload_button = ttk.Button(self.button_frame, text="Reload", command=lambda: self.reload_verbs())
        # self.reload_button.pack(side="left", padx=5)
        self.reload_button.grid(row=2,column=0)

        self.remove_button = ttk.Button(self.button_frame, text="Remove", command=lambda: self.remove_verb())
        # self.remove_button.pack(side="left", padx=5)
        self.remove_button.grid(row=1,column=0, pady=10)

        self.listbox2 = tk.Listbox(self.listbox_frame, selectmode="extended")
        # self.listbox2.pack(side="left", padx=5)
        self.listbox2.grid(row=0,column=2)

        self.num_back_button = ttk.Button(self.frame, text="back", command=lambda: self.back(parent))
        # self.num_back_button.pack(pady=10)
        self.num_back_button.grid(row=7, column=0,pady= 10)

        self.quit_num_button = ttk.Button(self.frame, text="quit", command=parent.destroy)
        self.quit_num_button.grid(row=8, column=0)
        # self.quit_num_button.pack()

        self.verbs = self.get_verbs()
        self.redo_list = []

        for verb in self.verbs:
            self.listbox.insert("end", verb)
        
        self.set_random_verb()
        self.bind('<Return>', self.keypress_return)

    def back (self, parent):
        self.destroy()
        parent.deiconify()
    
    def update_form_label(self):
        match self.form_index:
            case 0:
                self.label_question.config(text=f"eu:", fg="black")
            case 1:
                self.label_question.config(text=f"ele/ela:", fg="black")
            case 2:
                self.label_question.config(text=f"nós:", fg="black")
            case 3:
                self.label_question.config(text=f"eles/elas:", fg="black")

    def keypress_return(self, event):
        if self.input_text.get().strip() == self.answer:
            self.correct += 1
            self.label_question.config(text="Correct", fg="green")
            self.correct_label.config(text=f'Correct: {self.correct}')
            self.after(1000, self.update_answer, True)
        else:
            self.incorrect += 1
            self.incorrect_label.config(text=f'Incorrect: {self.incorrect}')
            self.label_question.config(text=self.answer, font=('Helvetica 10'), fg="red")
            self.label_question.after(1500, self.update_answer, False)

    def update_answer(self, is_correct):
        if not is_correct: self.redo_list.append([self.form_index, self.verbs[self.verb]])
        print(self.redo_list)
        self.form_index +=1
        if self.form_index > 3:
            del self.verbs[self.verb]
            if not self.verbs:
                self.verbs = self.get_verbs()

            self.set_random_verb()

        else:
            self.answer = self.verbs[self.verb][self.form_index]
            self.update_form_label()

        self.input_text.delete(0,'end')

    def set_random_verb(self):
        self.verb = random.choice(list(self.verbs.keys()))
        self.form_index = 0
        self.answer = self.verbs[self.verb][self.form_index]
        self.verb_label.config(text=f"Verb: {self.verb}")
        self.update_form_label()

    def add_verb(self):
        index = 0
        if self.listbox.curselection(): # if something is selected
            for selected_item in self.listbox.curselection():
                self.listbox2.insert("end", self.listbox.get(self.listbox.curselection()[index]))
                index +=1

    def remove_verb(self):
        offset = 0
        if self.listbox2.curselection(): # if something is selected
            for selected_item in self.listbox2.curselection():
                self.listbox2.delete(selected_item - offset)
                offset +=1

    def reload_verbs(self):
        self.verbs = self.get_verbs()
        new_verbs = {}
        selected_verbs = self.listbox2.get(0, "end")

        for verb in selected_verbs:
            new_verbs[verb] = self.verbs[verb]

        self.verbs = new_verbs
        self.set_random_verb()

    def get_verbs(self):
        fname = f"data/{self.filename}"
        data = ""

        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Unable to read file {fname}") from e
        
        data = data.splitlines()
        data = sorted(data)

        dict = {}

        for line in data:
            line = line.split(",")
            dict[line[0]] = line [1:]

        return dict