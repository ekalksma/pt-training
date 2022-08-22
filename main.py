from tkinter import *
from tkinter import ttk
import random
import os
import time
from turtle import left

fname = "data/numbers.csv"
data = ""
user_mode = "0"
min = -1
max = 1000

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

root_label = Label(root, text= "Portuguese Training App", font=('Helvetica 15 bold')).pack()
root_label2 = Label(root, text= "What would you like to practice?", font=('Helvetica 10')).pack(pady=20)

num_button = ttk.Button(root, text="Numbers", command=lambda: create_num_win()).pack(pady=20)

# Numbers Window 
num_win = Toplevel(root)
num_win.withdraw()

number = random.randint(min, max)
answer = data[number]

num_win_width = 600 
num_win_height = 300 
 
num_win.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

num_winlabel1 = Label(num_win, text= "Numbers", font=('Helvetica 15 bold'))
num_winlabel1.pack()

input_min = Entry(num_win, width= 5).pack()
input_max = Entry(num_win, width= 5).pack()

label_question = Label(num_win, text="What is " + str(number) + " in Portuguese?", font=('Helvetica 10')).pack()
input_text = Entry(num_win).pack(pady=5)

num_back_button = ttk.Button(num_win, text="back", command=lambda: close_num_win())
num_back_button.pack()

def create_num_win():
    root.withdraw()
    num_win.deiconify()

def close_num_win():
   num_win.withdraw()
   root.deiconify()

def update_number():
    global number 
    global answer
    number =  random.randint(min, max)  
    answer = data[number]
    label_question.config(text="What is " + str(number) + " in Portuguese?", fg="black", font=('Helvetica 10'))

def hit_return(event):
    if input_text.get().strip() == answer:
        label_question.config(text="Correct", fg="green")
        num_win.after(1000, update_number)
    else:
        print(answer)
        label_question.config(text=answer, font=('Helvetica 10'), fg="red")
        label_question.after(5000, update_number)

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
