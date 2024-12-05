logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
print("Welcome to number guessing game.")
print("Im thinking of a number between 1 and 100")
import random
number=random.randint(1,100)
difficulty=input("Choose a difficulty. Type easy or hard: ").lower()
if difficulty=="easy":
    attempts=10
    print("You have 10 attempts remaining.")
else:
    attempts=5
    print("You have 5 attempts remaining")
while attempts>0:
    guess=int(input("Make a guess:\n"))
    if guess<number:
        print("Too low.")
    elif guess==number:
        print(f"You got it! The answer was {guess}")
        break
    else:
        print("Too high")
    attempts-=1
    print(f"You have {attempts} remaining.")
    if attempts==0:
        print("You have run out of attempts.")
        print(f"Number was {number}.")