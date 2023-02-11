import random
from replit import clear
from art import logo

def draw_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

    
def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)
     
def check_score(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose. You went Over"
    elif user_score == 0:
        return "You Win. BlackJack"
    elif computer_score == 0:
        return "You Lose. BlackJack for Computer"
    elif user_score > 21:
        return "You Lose. You went Over"
    elif computer_score > 21:
        return "You Win. Computer Went Over"
    elif user_score > computer_score:
        return "You Win. U Scored near to 21"
    else:
        return "You Lose. Computer Scored near to 21"
def play():
    print(logo)
    is_end_game = False
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(draw_card())
        computer_card.append(draw_card())
    while not is_end_game:
        if calculate_score(user_card) == 0 or calculate_score(computer_card) == 0 or calculate_score(user_card) > 21:
            is_end_game = True
        else:
            print(f"Your card is {user_card} and score is {calculate_score(user_card)}")
            print(f"First card of computer is {computer_card[0]}")
            ch = input("Do u want to draw another card from the deck: ")
            if ch == "y":
                user_card.append(draw_card())
            elif ch == "n":
                is_end_game = True               
    while calculate_score(computer_card) != 0 and calculate_score(computer_card) < 17:
        computer_card.append(draw_card())
        result = check_score(calculate_score(user_card),calculate_score(computer_card))
        print(f"Your card is {user_card} and score is {calculate_score(user_card)}")
        print(f"Computer card is {computer_card} and score is {calculate_score(computer_card)}")
        print(result)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play()
        
    
