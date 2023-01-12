from game_data import data
import random
import art
#from replit import clear
import os


############# FUNCTIONS ###############
### clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
### select one element
def select_one(length_of_data):
    range_of_data = range(length_of_data)
    return random.choice(range_of_data)

### select another element. It can't be the same as previous
def select_new(first_selected, length_of_data):
    new_select = select_one(length_of_data)
    while new_select == first_selected:
        new_select = select_one(length_of_data)
    
    return new_select
    
### display the data of each element

def display_data(data, first_selected, second_selected):
#    clear()
    clear_screen()
    print(f"Compare A: {data[first_selected]['name']}, a {data[first_selected]['description']}, from {data[first_selected]['country']}.")
    print(art.vs)
    print(f"Against B: {data[second_selected]['name']}, a {data[second_selected]['description']}, from {data[second_selected]['country']}.")

### get users answer and compare against reality

def get_and_evaluate_answer(data, first_selected, second_selected, user_score):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    A_followers = data[first_selected]["follower_count"]
    B_followers = data[second_selected]["follower_count"]
    if A_followers > B_followers:
        actual_answer = "A"
    else:
        actual_answer = "B"
    if actual_answer == user_choice:
        user_score = user_score + 1
        print(art.logo)
        print(f"You're right! Current score: {user_score}")
        game_over = False
    else:
        print(f"Sorry, you're wrong. Final score: {user_score}")
        game_over = True
    return {"score": user_score, "game_over": game_over}

    

############## ACTUAL GAME ###############
    
game_over = False
choice1 = select_one(len(data))
choice2 = select_new(choice1, len(data))
user_score = 0

while game_over == False:
    display_data(data, choice1, choice2)
    user_results = get_and_evaluate_answer(data, choice1, choice2, user_score)
    game_over = user_results["game_over"]
    if game_over == True:
        break
    user_score = user_results["score"]
    choice1 = choice2
    choice2 = select_new(choice1, len(data))
