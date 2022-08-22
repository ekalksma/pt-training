from tkinter import *
from tkinter import ttk
import random
import os
import time
from turtle import left

fname = "data/numbers.csv"
data = ""
user_mode = "0"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

try:
    with open(fname, "r", encoding="utf-8") as f:
        data = f.read()
except Exception as e:
    raise ValueError(f"Unable to read file {fname}") from e

data = data.split(",")

# Main Window
root = Tk()

root_width = 600 
root_height = 300 
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (root_width/2)
y = (screen_height/2) - (root_height/2)
 
root.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

root_label = Label(root, text= "Portuguese Training App", font=('Helvetica 15 bold'))
root_label.pack()
root_label2 = Label(root, text= "What would you like to practice?", font=('Helvetica 10'))
root_label2.pack(pady=20)

num_button = ttk.Button(root, text="Numbers", command=lambda: create_num_win())
num_button.pack(pady=20)

quit_root_button = ttk.Button(root, text="quit", command=lambda: quit())
quit_root_button.pack()

# Numbers Window 
num_win = Toplevel(root)
num_win.withdraw()

num_win_width = 600 
num_win_height = 300 
 
num_win.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

num_winlabel1 = Label(num_win, text= "Numbers", font=('Helvetica 15 bold'))
num_winlabel1.pack()

min_label = Label(num_win, text= "min", font=('Helvetica 10'))
min_label.pack()
input_min = Entry(num_win, width= 5)
input_min.insert(0,"-1")
input_min.pack()

max_label = Label(num_win, text= "max", font=('Helvetica 10'))
max_label.pack()
input_max = Entry(num_win, width= 5)
input_max.insert(0,"10000")
input_max.pack(pady=5)

min = int(input_min.get())
max = int(input_max.get())
number = random.randint(min, max)
answer = data[number]

label_question = Label(num_win, text="What is " + str(number) + " in Portuguese?", font=('Helvetica 10'))
label_question.pack()
input_text = Entry(num_win, width=50)
input_text.pack(pady=5)

num_back_button = ttk.Button(num_win, text="back", command=lambda: close_num_win())
num_back_button.pack(pady=10)

quit_num_button = ttk.Button(num_win, text="quit", command=lambda: quit())
quit_num_button.pack()

def quit():
    root.destroy()

def create_num_win():
    root.withdraw()
    num_win.deiconify()

def close_num_win():
   num_win.withdraw()
   root.deiconify()

def update_number():
    global number 
    global answer

    min = input_min.get()
    max = input_max.get()

    if min.isnumeric() and max.isnumeric():
        min = int(min)
        if min < -1 or min > 10000:
            min = -1
        max = int(max)
        if max > 10000 or max < -1:
            max = 10000
    else:
        min = -1
        max = 10000

    number =  random.randint(min, max)
    answer = data[number]
    label_question.config(text="What is " + str(number) + " in Portuguese?", fg="black", font=('Helvetica 10'))
    input_text.delete(0,'end')

def hit_return(event):
    if input_text.get().strip() == answer:
        label_question.config(text="Correct", fg="green")
        num_win.after(1000, update_number)
    else:
        print(answer)
        label_question.config(text=answer, font=('Helvetica 10'), fg="red")
        label_question.after(4000, update_number)

num_win.bind('<Return>', hit_return)
    
root.mainloop()

# while user_mode != "1" or user_mode != "2" or user_mode != "3":
#     cls()
#     user_mode = input("Type 1 for: Numbers -> PT. Type 2 for: PT -> Numbers.\n")
#     while (min < 0 or min > 9999) or (max < 0 or max > 10000):
#         print("We are now going to select what numbers you want to practice.")
#         min = int(input("Please fill in the lowest number (Has to be >= 0):\n"))
#         max = int(input("Now fill in the highest number you want to practice (>=10000):\n"))

#         cls()

#     while user_mode == "1":
#         number = random.randint(min, max)
#         answer = data[number]
#         user_input = input("What is " + str(number) + " in Portuguese?\n").strip()

#         if user_input == answer:
#             print("\033[1;32mThat's Correct!\033[0;0m")
#             input("Type 'q' and press enter to return to the main menu.\n")

#             cls()
#         else:
#             print("\033[1;31mNice try! The correct answer is: \033[0;0m" + answer)
#             input("Type 'q' and press enter to return to the main menu.\n")

#             cls()

#         if user_input == "q":
#             break

#     while user_mode == "2":
#         number = random.randint(min, max)
#         answer = data[number]
#         user_input = input("What is '" + answer + "' in Portuguese?\n").strip()

#         if not user_input.isnumeric():
#             input("\033[1;31mOnly numbers are allowed\n\033[0;0m")
#             continue
#         else:
#             user_input = int(user_input)

#         if user_input == number:
#             print("\033[1;32mThat's Correct!\033[0;0m")
#             input("Type 'q' and press enter to return to the main menu.\n")

#             cls()
#         else:
#             print("\033[1;31mNice try! The correct answer is: \033[0;0m" + str(number))
#             input("Type 'q' and press enter to return to the main menu.\n")

#             cls()

#         if user_input == "q":
#             break
