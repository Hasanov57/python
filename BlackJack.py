playing=input("do you want to play black jack game?y/n\n")
import sys
import random
if playing=="n":
    sys.exit()
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards=[]
comp_cards=[]
def add_card_player():
    player_cards.append(random.choice(cards))
    if player_cards[len(player_cards)-1]==11 and sum(player_cards)>21:
        player_cards[len(player_cards)-1]=1
def add_card_comp():
    comp_cards.append(random.choice(cards))
def comp():
    while sum(comp_cards)<17:
        add_card_comp()
    if sum(comp_cards)>21:
        print(f"Your cards: {player_cards}, Your Score: {sum(player_cards)},computer's cards: {comp_cards}, computer score: {sum(comp_cards)}")
        print("You win")
    else: 
        print(f"Your cards: {player_cards}, Your Score: {sum(player_cards)},computer's cards: {comp_cards}, computer score: {sum(comp_cards)}")
        if sum(player_cards)>sum(comp_cards):
            print("You win")
        elif sum(player_cards)<sum(comp_cards):
            print("You lose")
        else:
            print("Draw")
    sys.exit()        
def answer():
    answer=input("Do you want to add cards or let the computer play? y/n\n")
    if answer=="y":
        add_card_player()
        print(f"Your cards: {player_cards}, Your score:{sum(player_cards)}, computer's first card:{comp_cards}")
        if sum(player_cards)>21:
            print("You Lose")
            sys.exit()
    else:
        comp()
player_cards.append(random.choice(cards))
add_card_player()
add_card_comp()
print(f"Your cards: {player_cards}, Your score: {sum(player_cards)}, computer's first card: {comp_cards}")
if sum(player_cards)==21:
    print("You won with BlackJack!")
    sys.exit()
else:
    answer()
    while sum(player_cards)<21:
        answer()