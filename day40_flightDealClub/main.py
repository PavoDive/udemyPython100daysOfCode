from kiwi import Kiwi
from sheety import Sheety
# from telegram import Telegram # disabled as gmail is used, following the project instructions
from gmail import Gmail
import datetime
from unidecode import unidecode

k = Kiwi()
wb = Sheety()
# t = Telegram() # disabled as gmail is used, following the project instructions
g = Gmail()

# ---------------- get new user ----------------
new_user = input("Are you a new user? (yes / no): ").lower()
if new_user == "yes":
    wb.get_user_data()
    print("Now, please provide us with your dream destinations:\n")
    wb.get_user_destination()
elif new_user == "no":
    new_destinations = input("Do you want to add to your dream destinations? (yes / no): ").lower()
    if new_destinations == "yes":
        wb.get_user_destination()
    else:
        print("We'll send you good deals once we find some!")


# ---------------- read destinations ----------------
print("Reading from user destinations...\n")
destinations = wb.read_destinations()

# I initially did this with listh comprehension (and it worked)
# but after reading the comments to unutbu's answer here
# https://stackoverflow.com/questions/18193205/list-comprehension-returning-values-plus-none-none-none-why, it is clear that even
# if possible, it's better to use for loops sometimes
#
# [destination.update(destination_id=k.get_destination_id(destination["destination"])) for destination in destinations]

for _ in destinations:
    _.update(destination_id = k.get_destination_id(_["destination"]))

    
# define approximate dates. Min departure date will be +10d
# max departure date will be +40d. Min stay = 7d, max stay = 20d
today = datetime.datetime.now()
d_from = (today + datetime.timedelta(days = 10)).strftime("%d/%m/%Y")
d_to = (today + datetime.timedelta(days = 40)).strftime("%d/%m/%Y")
n_in_dst_from = 7
n_in_dst_to = 20

# this results in a list with either false or the flight data
print("Getting flights for those destinations...\n")
result_list = [k.get_flights(fly_to = destination["destination_id"], date_from = d_from, date_to = d_to, price_to = destination["cutoffPrice"], nights_in_dst_from = n_in_dst_from, nights_in_dst_to = n_in_dst_to) for destination in destinations]

if any(result_list):
    result_list = [result for result in result_list if result != False]
    print("Sending email to users")
    for email in [user["email"] for user in wb.read_user_data()]:
        for result in result_list:
            # unidecode needed to remove utf-8 encoding that makes
            # smtplib fail: https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
            body = unidecode("".join([f"{key}: {value}\n" for (key, value) in result.items()]))
            g.send_email(email, body)


# ----------------- This is to send it to telegram, rather than email ---------------

# this sends the sendable items of result_list to telegram BOT, which I like more for personal use

# if any(result_list):
#     print("Sending messages to Telegram Bot")
#     [t.send_message("".join([f"{key}: {value}\n" for (key, value) in result.items()])) for result in result_list if result != False]
# else:
#     print("Sorry, no flights matched your requirements at this time.")
