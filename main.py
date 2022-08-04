import random

fname = "data/numbers.csv"
data = ""
user_mode = "0"
min = 0
max = 10000

try:
    with open(fname, "r") as f:
        data = f.read()
except Exception as e:
    raise ValueError(f"Unable to read file {fname}") from e

data = data.split(",")
print(data[10000])
while user_mode != "1" or user_mode != "2" or user_mode != "3":
    user_mode = input("Type 1 for: Numbers -> PT. Type 2 for: PT -> Numbers. Type 3 for: Mixed:\n")
    
    while user_mode == "1":
        number = random.randint(min, max)
        answer = data[number]
        user_input = input("What is " + str(number) + " in Portuguese?\n").strip()

        if user_input == answer:
            print("That's Correct!\n")
        else:
            print("Nice try! The correct answer is: " + answer + "\n")

