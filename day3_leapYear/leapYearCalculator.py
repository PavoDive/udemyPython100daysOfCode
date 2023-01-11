# Don't change the code below 
year = int(input("Which year do you want to check? "))
# Don't change the code above 

# Write your code below this line
ly = "Leap year."
nly = "Not leap year."

if year % 4 == 0:
    if year % 100 == 0: 
        if year % 400 == 0:
            print(ly)
        else:
            print(nly)
    else:
        print(ly)
else:
    print(nly)
