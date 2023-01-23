import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_dictionary = {letter:code for (letter, code) in nato_alphabet.itertuples(index = False, name = None)}

# alternative way Angela followed:
# nato_dictionary = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Please input a word: ").upper()

code_list = [nato_dictionary[letter] for letter in user_word]
print(code_list)
