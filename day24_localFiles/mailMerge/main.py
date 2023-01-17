#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file1:
    letter_text = file1.read()

with open("Input/Names/invited_names.txt") as file2:
    invited_names = file2.read()

# this could have been done with invited_names = file2.readlines()
# but string.strip() would have been needed to remove \n
invited_names = invited_names.split("\n")

for name in invited_names:
    actual_text = letter_text.replace("[name]", name)
    with open("Output/ReadyToSend/letter_to_"+name+".txt", mode = "w") as file3:
        file3.write(actual_text)
    
