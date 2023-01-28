# Imagine that file1.txt **doesn't exist in folder**. Then
# the following code will trhrow an error (a FileNotFoundError):

# with open("file1.txt") as file1:
#     contents = file1.read()

# Then we can try to catch and handle that error:
# try:
#     file1 = open("file1.txt")
# except:
#     file1 = open("file1.txt", "w") # this creates the file
#     file1.write("something")

# but this sort of "broad except" clauses are discouraged by PEP
# because of the risk or catching other, unexpected exceptions.
# A better version would be:

# try:
#     file1 = open("file1.txt")
#     my_dict = {"A":1, "B":2}
#     print(my_dict["C"]) # throws an index error that goes
#     # uncatched **IF file1 exists**.
# except FileNotFoundError:
#     file1 = open("file1.txt", "w")
#     file1.write("something")

# Python does't attempt all the try block: if it catches an
# exception, it immediately goes to the except block.
# Multiple errors can be catched with different except blocks:

# try:
#     file1 = open("file1.txt")
#     my_dict = {"A":1, "B":2}
#     print(my_dict["C"]) # throws an index error that goes
#     # uncatched **IF file1 exists**.
# except FileNotFoundError:
#     file1 = open("file1.txt", "w")
#     file1.write("something")
# except KeyError:
#     print("Index Out of range")

# It is possible to get hold of the error message:

# try:
#     file1 = open("file1.txt")
#     my_dict = {"A":1, "B":2}
#     print(my_dict["C"]) # throws an index error that goes
#     # uncatched **IF file1 exists**.
# except FileNotFoundError:
#     file1 = open("file1.txt", "w")
#     file1.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")

# The else block runs if everything in the try clause succeded.
# If any of the except block ran, the else block will not be run.
# try:
#     file1 = open("file1.txt")
#     my_dict = {"A":1, "B":2}
#     print(my_dict["B"]) # no error here
#     # uncatched **IF file1 exists**.
# except FileNotFoundError:
#     file1 = open("file1.txt", "w")
#     file1.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     contents = file1.read()
#     print(contents)

# the finally block runs no matter what:
# try:
#     file1 = open("file1.txt")
#     my_dict = {"A":1, "B":2}
#     print(my_dict["B"]) # no error here
#     # uncatched **IF file1 exists**.
# except FileNotFoundError:
#     file1 = open("file1.txt", "w")
#     file1.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     contents = file1.read()
#     print(contents)
# finally:
#     file1.close()
#     print("file was closed")

# It is possible to generate one's own errors with raise sentence:
# Imagine a BMI calculating app. It has to catch unrealistic
# user heights:

# user_height = float(input("Please input your height in m: "))
# user_weight = float(input("Please input your weight in kg: "))

# bmi = user_weight/user_height**2
# print(bmi)

# This will work even for the unrealistic height of 40m. So
# a new kind of error is raised:

user_height = float(input("Please input your height in m: "))
user_weight = float(input("Please input your weight in kg: "))

if user_height > 3:
    raise ValueError("Supplied height is unrealistic")

bmi = user_weight/user_height**2
print(bmi)
