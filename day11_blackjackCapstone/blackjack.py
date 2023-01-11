import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_inital_two():
    return random.choices(cards, k = 2)

def draw_additional():
    return random.choice(cards)

def replace_ace(hand, score):
    ### could have used hand.remove(11)
    ### could have used hand.append(1)
    if score > 21:
        position_ace = 0
        for card in hand:
            if card == 11:
                hand[position_ace] = 1
                return hand
        position_ace = position_ace + 1
    else:
        ""
    return hand


def calculate_score(hand):
    ### could have used sum(hand)
    score = 0
    for card in hand:
        score = score + card
    return score

def print_status_user(hand, type_print):
    score = calculate_score(hand)
    print(f"    Your {type_print} cards: {hand}, {type_print} score: {score}")

def establish_winner(u_score, c_score):
    if u_score > 21:
        print("You went over. You lose :(")
    elif c_score > 21:
        print("Computer went over. You win :")
    elif u_score > c_score:
        print("You win!")
    elif u_score == c_score:
        print("There's a draw.")
    else:
        print("You lose")

def want_to_exit_game():
    want_to_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == "n":
        return True
    else:
        return False


def play_game():
    user_hand = draw_inital_two()
    user_score = calculate_score(user_hand)
    user_hand = replace_ace(user_hand, user_score)
    print_status_user(user_hand, "current")
    computer_hand = [draw_additional()]
    print(f"    Computer's first card: {computer_hand}")
    want_to_add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while want_to_add_card == "y":
        user_hand.append(draw_additional())
        user_score = calculate_score(user_hand)
        user_hand = replace_ace(user_hand, user_score)
        print_status_user(user_hand, "current")
        want_to_add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if want_to_add_card == "n":
            print_status_user(user_hand, "final")

    computer_hand.append(draw_additional())
    computer_score = calculate_score(computer_hand)
    
    while computer_score < user_score or computer_score < 17:
        computer_hand.append(draw_additional())
        computer_score = calculate_score(computer_hand)
        print(f"Debug1 {computer_hand}")
        computer_hand = replace_ace(computer_hand, computer_score)
    print(f"    Computer's final cards: {computer_hand}, final score: {computer_score}")

    establish_winner(user_score, computer_score)


### initial logo and question

want_to_quit = want_to_exit_game()
if not want_to_quit:              
    print(logo)

while not want_to_quit:
    play_game()
    want_to_quit = want_to_exit_game()


### dealer has to deal if
### 1. has less than 17
### 2. has less than user
