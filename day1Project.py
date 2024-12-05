rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user==0:
    print(rock)
elif user==1:
    print(paper)
else:
    print(scissors)
import random
comp_choice=random.randint(0,2)
print("Computer chose:")
if comp_choice==0:
    print(rock)
elif comp_choice==1:
    print(paper)
else:
    print(scissors)
if user==0 and comp_choice==1:
    print("You lose")
    if user==0 and comp_choice==2:
        print("You win")
elif user==1 and comp_choice==0:
    print("You win")
    if user==1 and comp_choice==2:
        print("You lose")
elif user==2 and comp_choice==0:
    print("You lose")
    if user==2 and comp_choice==1:
        print("You win")
else:
    print("Nobody wins")