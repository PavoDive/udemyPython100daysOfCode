from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

def get_bid(bidder, bid_amount):
    bids[bidder] = bid_amount

def calculate_winner(bid_dictionary):
  max_bid = 0
  for i in bid_dictionary:
    if bid_dictionary[i] > max_bid:
      winner = i
      max_bid = bid_dictionary[i]

  print(f"\nThe winning bid is from {winner} for ${max_bid}")
  
print("\nWelcome to the secret auction program.\n")

last_user = False
bids = {}

while not last_user:
  name = input("What is your name?: ")
  bid_value = float(input("\nWhat's your bid?: $"))
  get_bid(bidder = name, bid_amount = bid_value)
  more_bidders = input("\nAre there any other bidders? Type 'yes' or 'no' \n").lower()
  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    clear()
    calculate_winner(bids)
    last_user = True
  else:
    clear()
    print("I couldn't understand your input. Calculating the bid's winner...")
    calculate_winner(bids)
    last_user = True

