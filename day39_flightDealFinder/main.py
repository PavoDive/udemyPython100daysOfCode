from kiwi import Kiwi
from sheety import Sheety
from telegram import Telegram
import datetime

k = Kiwi()
wb = Sheety()
t = Telegram()

print("Reading from user destinations...\n")
destinations = wb.read_destinations()

# define approximate dates. Min departure date will be +10d
# max departure date will be +25d. Min stay = 7d, max stay = 20d
today = datetime.datetime.now()
d_from = (today + datetime.timedelta(days = 10)).strftime("%d/%m/%Y")
d_to = (today + datetime.timedelta(days = 25)).strftime("%d/%m/%Y")
n_in_dst_from = 7
n_in_dst_to = 20

# this results in a list with either false or the flight data
print("Getting flights for those destinations...\n")
result_list = [k.get_flights(fly_to = destination["destination"], date_from = d_from, date_to = d_to, price_to = destination["cutoffPrice"], nights_in_dst_from = n_in_dst_from, nights_in_dst_to = n_in_dst_to) for destination in destinations]

# this sends the sendable items of result_list to telegram BOT
if any(result_list):
    print("Sending messages to Telegram Bot")
    [t.send_message("".join([f"{key}: {value}\n" for (key, value) in result.items()])) for result in result_list if result != False]
else:
    print("Sorry, no flights matched your requirements at this time.")
