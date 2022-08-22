from tkinter import *
from tkinter import ttk
import random
import os
from turtle import left

fname = "data/numbers.csv"
data = ""
user_mode = "0"
min = -1
max = 10001

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

try:
    with open(fname, "r") as f:
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

# Numbers Window 
num_win = Toplevel(root)
num_win.withdraw()

num_win_width = 600 
num_win_height = 300 
 
num_win.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

num_winlabel1 = Label(num_win, text= "Numbers", font=('Helvetica 15 bold'))
num_winlabel1.pack()

input_min = Entry(num_win, width= 5)
input_max = Entry(num_win, width= 5)
input_min.pack()
input_max.pack()

input = Entry(num_win)
input.pack()

num_back_button = ttk.Button(num_win, text="back", command=lambda: close_num_win())
num_back_button.pack()

def create_num_win():
    root.withdraw()
    num_win.deiconify()

def close_num_win():
   num_win.withdraw()
   root.deiconify()

num_win.mainloop()

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
