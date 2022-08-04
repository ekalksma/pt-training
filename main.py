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

while user_mode != "1" or user_mode != "2" or user_mode != "3":
    cls()
    user_mode = input("Type 1 for: Numbers -> PT. Type 2 for: PT -> Numbers.\n")
    while (min < 0 or min > 9999) or (max < 0 or max > 10000):
        print("We are now going to select what numbers you want to practice.")
        min = int(input("Please fill in the lowest number (Has to be >= 0):\n"))
        max = int(input("Now fill in the highest number you want to practice (>=10000):\n"))

        cls()

    while user_mode == "1":
        number = random.randint(min, max)
        answer = data[number]
        user_input = input("What is " + str(number) + " in Portuguese?\n").strip()

        if user_input == answer:
            print("\033[1;32mThat's Correct!\033[0;0m")
            print("Type 'q' and press enter to return to the main menu.\n")
        else:
            print("\033[1;31mNice try! The correct answer is: \033[0;0m" + answer)
            print("Type 'q' and press enter to return to the main menu.\n")

        if user_input == "q":
            break

    while user_mode == "2":
        number = random.randint(min, max)
        answer = data[number]
        user_input = input("What is '" + answer + "' in Portuguese?\n").strip()

        if not user_input.isnumeric():
            input("\033[1;31mOnly numbers are allowed\n\033[0;0m")
            continue
        else:
            user_input = int(user_input)

        if user_input == number:
            print("\033[1;32mThat's Correct!\033[0;0m")
            print("Type 'q' and press enter to return to the main menu.\n")
        else:
            print("\033[1;31mNice try! The correct answer is: \033[0;0m" + str(number))
            print("Type 'q' and press enter to return to the main menu.\n")

        if user_input == "q":
            break
