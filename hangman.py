stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=len(stages)-1
word_list = ["apple", "cucumber", "tomato"]
import random
chosen_word = random.choice(word_list)
test_list=list(chosen_word)
for i in range(len(test_list)):
  test_list[i]="_"
print(stages[6])
while "".join(test_list)!=chosen_word:
  guess = input("Guess a letter: ").lower()
  for j in range(len(chosen_word)):
    if chosen_word[j]==guess:
      test_list[j]=guess
  if guess in test_list:
    print(test_list)
  else:
    print(test_list)
    lives-=1
  print(stages[lives])
  if lives==0:
    print("You lose")
  elif "".join(test_list)==chosen_word:
    print("You win")