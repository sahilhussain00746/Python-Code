# This is a Coffee Machine
import art, data

print(art.logo)

def insert_money():
    penny = int(input("Total Penny: "))
    nickel = int(input("Total Nickel: "))
    dime = int(input("Total Dime: "))
    quarter = int(input("Total Quarter: "))

    return penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25


def is_resource_sufficient(order):
    drink = data.menu[order]
    report = data.menu["report"]

    if report["water"] < drink["water"]:
        print("Sorry, not enough water.")
        return False
    if report["milk"] < drink["milk"]:
        print("Sorry, not enough milk.")
        return False
    if report["coffee"] < drink["coffee"]:
        print("Sorry, not enough coffee.")
        return False

    return True


def prepare_coffee(order, change):
    drink = data.menu[order]
    report = data.menu["report"]

    report["water"] -= drink["water"]
    report["milk"] -= drink["milk"]
    report["coffee"] -= drink["coffee"]
    report["profit"] += drink["money"]

    print(f"\nYour order is ready ☕\n{art.ready}")
    print(
        f"Bill:\n"
        f"Water: {drink['water']}ml\n"
        f"Milk: {drink['milk']}ml\n"
        f"Coffee: {drink['coffee']}g\n"
        f"Cost: ${drink['money']}\n"
    )

    if change > 0:
        print(f"Take your change: ${round(change, 2)}")


def coffee_machine(order):
    if not is_resource_sufficient(order):
        return

    drink = data.menu[order]
    print(f"{order.capitalize()} cost: ${drink['money']}")

    paid_amount = insert_money()

    if paid_amount < drink["money"]:
        print("Insufficient amount! Money refunded.")
        return

    change = paid_amount - drink["money"]
    prepare_coffee(order, change)



is_on = True
while is_on:
    order = input(
        "\nWhat would you like? (espresso/latte/cappuccino/report/off): "
    ).lower()

    if order == "off":
        is_on = False
        print("Machine turned off.")
        continue

    if order == "report":
        report = data.menu["report"]
        print(
            f"\nResources:\n"
            f"Water: {report['water']}ml\n"
            f"Milk: {report['milk']}ml\n"
            f"Coffee: {report['coffee']}g"
            f"Profit: ${report['profit']}"
        )
        continue

    if order in ["espresso", "latte", "cappuccino"]:
        coffee_machine(order)
    else:
        print("Invalid option! Please try again.")
