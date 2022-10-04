import tkinter as tk
from tkinter import ttk
from num_win import NumbersWindow
from pre_window import PresenteWindow
from preimp_window import PreteritoImperfeitoWindow
from futuro_win import FuturoWindow
from pretperf_win import PreteritoPerfeitoWindow
from futpret_win import FuturoDoPreteritoWindow

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('app')

        self.width = 600 
        self.height = 400
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
        num_button.pack(pady=10)

        presente_button = ttk.Button(self, text="Presente", command=self.open_presente)
        presente_button.pack(pady=10)

        preimp_button = ttk.Button(self, text="Préterito Imperfeito", command=self.open_preimp)
        preimp_button.pack(pady=10)

        futuro_button = ttk.Button(self, text="Préterito Perfeito", command=self.open_pretperf)
        futuro_button.pack(pady=10)

        futuro_button = ttk.Button(self, text="Subjuntivo Futuro", command=self.open_futuro)
        futuro_button.pack(pady=10)

        futpret_button = ttk.Button(self, text="Futuro do Pretérito", command=self.open_futpret)
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

    def open_presente(self):
        self.presente = PresenteWindow(self)
        self.withdraw()
    
    def open_pretperf(self):
        self.presente = PreteritoPerfeitoWindow(self)
        self.withdraw()

    def open_preimp(self):
        self.presente = PreteritoImperfeitoWindow(self)
        self.withdraw()
    
    def open_futuro(self):
        self.presente = FuturoWindow(self)
        self.withdraw()

    def open_futpret(self):
        self.presente = FuturoDoPreteritoWindow(self)
        self.withdraw()

if __name__ == "__main__":
    app = App()
    app.mainloop()