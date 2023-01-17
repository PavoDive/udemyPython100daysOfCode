# The file exampleFile.txt was created with the following
# text inside:
#    hello, this is inside the file.
#    and also this.

# there is a "canonical" way to open it:

file1 = open("exampleFile.txt")

file_contents = file1.read()
print(file_contents)


file1.close() # this is needed always!

# But there is another way to avoid *forgetting* the close:

with open("exampleFile.txt") as file2:
    contents = file2.read()
    print(contents)

# writing and append:

with open("exampleFile.txt", mode = "w") as file2:
    file2.write("New text")

with open("exampleFile.txt", mode = "a") as file2:
    file2.write("\nNew Text.")

    
