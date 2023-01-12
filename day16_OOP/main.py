from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create menu. It self-populates
coffe_menu = Menu()
money_handler = MoneyMachine()
coffe_machine = CoffeeMaker()

run_machine = True

while run_machine:
    choice = input(f"What drink do you want? Please type any of the following choices {coffe_menu.get_items()}: ")
    menu_item = coffe_menu.find_drink(choice)
    if choice == "off":
        break
    elif choice == "report":
        coffe_machine.report()
        money_handler.report()
    else:
        if coffe_machine.is_resource_sufficient(menu_item):
            if money_handler.make_payment(menu_item.cost):
                coffe_machine.make_coffee(menu_item)

