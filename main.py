from tkinter import *
from tkinter import ttk
import random
import os

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

#Create an instance of Tkinter frame
root = Tk()
root_width = 600 # Width 
root_height = 300 # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (root_width/2)
y = (screen_height/2) - (root_height/2)
 
root.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))
rootLabel = Label(root, text= "Portuguese Training App", font=('Helvetica 15 bold'))
rootLabel.pack()
rootLabel2 = Label(root, text= "What would you like to practice?", font=('Helvetica 10'))
rootLabel2.pack(pady=20)
button = ttk.Button(root, text="Numbers")
button.pack(pady=20)

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
