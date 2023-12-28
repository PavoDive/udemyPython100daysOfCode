import numpy as np

def print_board(bd):
    line_0 = f"1  {bd[0,0]:^5s}|{bd[0,1]:^5s}|{bd[0,2]:^5s}"
    line_1 = f"2  {bd[1,0]:^5s}|{bd[1,1]:^5s}|{bd[1,2]:^5s}"
    line_2 = f"3  {bd[2,0]:^5s}|{bd[2,1]:^5s}|{bd[2,2]:^5s}"

    space_line = "        |     |     "
    sep_line =   "   -----+-----+-----"
    columns_line = f"   {'A':^5s}|{'B':^5s}|{'C':^5s}\n                    "

    print(f"{columns_line}\n{space_line}\n{line_0}\n{space_line}\n{sep_line}\n{space_line}\n{line_1}\n{space_line}\n{sep_line}\n{space_line}\n{line_2}\n{space_line}")

def process_input(user, input_symbol, board_array):
    mapping = {"a": 0, "b": 1, "c": 2}

    invalid_input = True
    while invalid_input:
        user_input = input(f"This is {user} turn.\nPlease input the cell you want to put your '{input_symbol}' as columnRow: for example 'a1' or 'b3':\n").lower()
        if len(user_input) != 2:
            print("Too long an input! please enter only two characters, the first a letter for the column, and the second a number for the row.")
            continue
        else:
            column,row = user_input
            if row in ["1", "2", "3"] and column in ["a", "b", "c"]:
                row = int(row) - 1
                column = mapping.get(column)
                if not board_array[row, column] == " ":
                    print("That cell is already filled. Pick a different one\n")
                    continue
                else:
                    invalid_input = False
            else:
                print("Your input doesn't look right. Please enter only two characters, the first a letter for the column (among a, b or c), and the second a number for the row (among 1, 2, or 3).")
                continue

        board_array[row, column] = input_symbol
        return board_array

def check_winner(board_array):
    winner = None
    for symbol in ["X", "O"]:
        for column in range(3):
            if all(board_array[:,column] == symbol):
                winner = symbol
                return winner
        for row in range(3):
            if all(board_array[row,:] == symbol):
                winner = symbol
                return winner
        if np.trace(board_array == symbol) == 3:
            winner = symbol
            return winner
        if (board_array[0, 2] == symbol and board_array[1,1] == symbol and board_array[2, 0] == symbol):
            winner = symbol
            return winner

def check_finished(board_array):
    if (board_array == " ").sum() == 0:
        return True
    else:
        return False

def switch_user(user, users):
    if user == users[0]:
        return users[1]
    else:
        return users[0]

def play_game():
    board = np.full(shape = (3,3), fill_value = " ", dtype = "str")

    game_finished = (check_finished(board) or (check_winner(board) in ["X", "O"]))
    user_1_name = input("Please input the name of User that will play 'X':\n")
    user_2_name = input("Please input the name of User that will play 'O':\n")
    users = {user_1_name: "X", user_2_name: "O"}
    current_user = user_1_name

    while not game_finished:
        print_board(board)
        board = process_input(current_user, users[current_user], board)
        winner = check_winner(board)
        if winner == "X":
            print(f"{'='*40}\n{'The winner is '+[key for key, value in users.items() if value == 'X'][0]+'!':^40s}\n{'='*40}")
            print_board(board)
        elif winner == "O":
            print(f"{'='*40}\n{'The winner is '+[key for key, value in users.items() if value == 'O'][0]+'!':^40s}\n{'='*40}")
            print_board(board)
        if check_finished(board) == True:
            print("No player wins, game over!")
            print_board(board)
        current_user = switch_user(current_user, list(users.keys()))
        game_finished = (check_finished(board) or (check_winner(board) in ["X", "O"]))

want_to_play = True
while want_to_play:
    play_game()
    want_to_play = bool(input("If you DON'T want to play some more, please press the ENTER key. Else, press any other key: "))
