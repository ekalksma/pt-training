import tkinter as tk
from tkinter import ttk
from num_win import NumbersWindow
from conjugation_win import ConjugationWindow
from infinitive_win import InfinitiveWindow

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('app')

        self.width = 600 
        self.height = 600
        self.screen_width = self.winfo_screenwidth()  # Width of the screen
        self.screen_height = self.winfo_screenheight() # Height of the screen
        
        # Calculate Starting X and Y coordinates for Window
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2)
        
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.label = tk.Label(self, text= "Portuguese Training App", font=('Helvetica 15 bold'))
        self.label.pack()
        self.label2 = tk.Label(self, text= "What would you like to practice?", font=('Helvetica 10'))
        self.label2.pack(pady=20)

        num_button = ttk.Button(self, text="Numbers", command=self.open_numbers)
        num_button.pack(pady=5)

        self.indi_label = tk.Label(self, text= "Indicativo", font=('Helvetica 15'))
        self.indi_label.pack(pady=5)


        presente_button = ttk.Button(self, text="Presente", command=lambda: self.open_conjugation_win("indi_presente.txt", "Presente"))
        presente_button.pack(pady=10)

        preimp_button = ttk.Button(self, text="Préterito Imperfeito", command=lambda: self.open_conjugation_win("indi_preimp.txt", "Préterito Imperfeito"))
        preimp_button.pack(pady=10)

        futuro_button = ttk.Button(self, text="Préterito Perfeito", command=lambda: self.open_conjugation_win("indi_preperf.txt", "Préterito Perfeito"))
        futuro_button.pack(pady=10)

        futpret_button = ttk.Button(self, text="Futuro do Pretérito", command=lambda: self.open_conjugation_win("indi_futpret.txt", "Futuro do Pretérito"))
        futpret_button.pack(pady=10)

        self.sub_label = tk.Label(self, text= "Subjuntivo", font=('Helvetica 15'))
        self.sub_label.pack(pady=5)

        sub_preimp_button = ttk.Button(self, text="Subjuntivo Préterito Imperfeito", command=lambda: self.open_conjugation_win("sub_preimp.txt", "Subjuntivo Préterito Imperfeito"))
        sub_preimp_button.pack(pady=10)

        sub_futuro_button = ttk.Button(self, text="Subjuntivo Futuro", command=lambda: self.open_conjugation_win("sub_futuro.txt", "Futuro do Pretérito"))
        sub_futuro_button.pack(pady=10)

        futpret_button = ttk.Button(self, text="Vocabulary", command=self.open_infinitive)
        futpret_button.pack(pady=10)

        self.quit_button = ttk.Button(self, text="quit", command=self.quit)
        self.quit_button.pack(pady=10)

        self.num_win = NumbersWindow(self)
        self.num_win.withdraw()


    def quit(self):
        self.destroy()
    
    def open_numbers(self):
        self.num_win.deiconify()
        self.withdraw()

    def open_conjugation_win(self, filename, titel):
        self.presente = ConjugationWindow(self,filename, titel)
        self.withdraw()
    
    def open_infinitive(self):
        self.presente = InfinitiveWindow(self)
        self.withdraw()

if __name__ == "__main__":
    app = App()
    app.mainloop()