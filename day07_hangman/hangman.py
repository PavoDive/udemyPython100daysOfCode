import random
#Step 1 

word_list = ["ardvark", "baboon", "camel"]
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


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
selected_word = random.choice(word_list)
print(selected_word)

# print as many blanks as letters:
representation = ["_"] * len(selected_word)
#print(representation) #used for debugging

end_of_game = False

while not end_of_game:
  #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess_letter = input("Please guess a letter\n").lower()
  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  
  hits = []
  selected_word_list = list(selected_word)
  
  for i in range(0, len(selected_word)):
    if guess_letter == selected_word_list[i]:
      hits.append(i)
  
  # print(hits) # used for debugging
  
  # replace guessed items in representation
  if len(hits) == 0:
    actual_stage = stages.pop(-1)
    print(actual_stage)
    if len(stages) == 0:
      end_of_game = True
      print("You lose")
  else:
    for i in hits:
      representation[i] = guess_letter
  
  print(representation)
  if not "_" in representation:
    end_of_game = True
    print("You won!")
