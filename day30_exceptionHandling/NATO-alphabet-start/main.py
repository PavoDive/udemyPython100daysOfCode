# This is code originally from day 26. The goal today is to catch
# flawed user inputs and deal with those exceptions
import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_dictionary = {letter:code for (letter, code) in nato_alphabet.itertuples(index = False, name = None)}

# alternative way Angela followed:
# nato_dictionary = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# This was the original code
# user_word = input("Please input a word: ").upper()

# code_list = [nato_dictionary[letter] for letter in user_word]
# print(code_list)

# ------------ This is the new added / modified part ---###
keep_trying = True
while keep_trying:
    user_word = input("Please input a word: ").upper()
    try:
        code_list = [nato_dictionary[letter] for letter in user_word]
        keep_trying = False
    except KeyError:
        print("Sorry letters only, please")

print(code_list)
