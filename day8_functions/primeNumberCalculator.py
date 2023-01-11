#Write your code below this line 👇
def prime_checker(number):
    if number == 1 or number == 2:
        print("It's a prime number.")
    elif number % 2 == 0:
        print("It's not a prime number.")
    else:
        i = 3
        while i <= number:
            if number % i == 0 and i < number:
                print("It's not a prime number.")
                break
            elif i == number:
                print("It's a prime number.")
            i = i + 1
            

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
