from coffee_data import MENU, resources


######### FUNCTIONS ############
# Turn off the machine if user input is "off" (end code execution)
def turn_off(user_input):
    if input == "off":
        return False
    else:
        return True
    
# print report if user input is "report". It should show current resource values (water, milk, coffe, Money)
def report_inventory(resources, money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${format('%.2f' % money)}")

# Check if resources are sufficient
def test_resources(MENU, choice, resources):

    keys_of_choice = MENU[choice]["ingredients"].keys()
    for i in keys_of_choice:
        required = MENU[choice]["ingredients"][i]
        available = resources[i]
        left = available - required
        if left < 0:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

# Process coins
def get_input_value():
    value_each_coin = {"quarters":.25, "dimes": .1, "nickles":.05, "pennies": .01}
    value = 0
    for coin in ["quarters", "dimes", "nickles", "pennies"]:
        number_of_coins = int(input(f"How many {coin}?: "))
        value = value + value_each_coin[coin] * number_of_coins
    return value

def test_value(MENU, choice, value):
    if value >= MENU[choice]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
# Check transaction was successful. 
def commit_resources(MENU, choice, resources):
    for resource in MENU[choice]["ingredients"].keys():
        resources[resource] = resources[resource] - MENU[choice]["ingredients"][resource]
    return resources


def calculate_change(value, MENU, choice):
    change = value - MENU[choice]["cost"]
    if change > 0:
        print(f"Here is ${format('%.2f' % change)} in change.")
    else:
        return

# ask user for input
machine_on = True
money = 0

while machine_on:   
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        break
    elif user_choice == "report":
        report_inventory(resources, money)
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if test_resources(MENU, user_choice, resources):
            user_value = get_input_value()
            if test_value(MENU, user_choice, user_value):
                change = calculate_change(user_value, MENU, user_choice)
                print(f"Here is your {user_choice}. Enjoy!")
                resources = commit_resources(MENU, user_choice, resources)
                money = money + MENU[user_choice]["cost"]
        
