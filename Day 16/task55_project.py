from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee = CoffeeMaker()
my_money = MoneyMachine()

is_on = True
while is_on:
    option = my_menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ")

    if choice == "off":
        is_on = False
        print("Machine turned off.")
        continue

    elif choice == "report":
        report = my_coffee.report()
        report = my_money.report()
        continue

    else:
        drink = my_menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                my_coffee.make_coffee(drink)