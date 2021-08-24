MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resources_sufficient(order):
    for items in order:
        if order[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
        return True


def coin_check():
    print("Please Insert Coins")
    total = int(input("How many quarters?  ")) * 0.25
    total += int(input("How many dimes?  ")) * 0.1
    total += int(input("How many nickel?  ")) * 0.05
    total += int(input("How many pennies?  ")) * 0.01
    return round(total, 2)


def sufficient_coin(amount_inserted, cost_order):
    if amount_inserted >= cost_order:
        change = amount_inserted - cost_order
        print(f"Here is ${change} in change")
        global profit
        profit += cost_order
        return True
    elif cost_order > amount_inserted:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for key in order_ingredients:
       resources[key] -= order_ingredients[key]
    print(f"Here is your {drink_name}☕. Enjoy!")


#TODO:2 Turn off the coffee Machine by entering "Off to the Prompt"
switch = True
while switch is not False:
#TODO:1 Print Prompt the user
    choice = input("What would you like? (espreso/latte/cappuccino): ").lower()
    if choice == "off":
        switch = False
        print("Machine Turned off")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = coin_check()
            if sufficient_coin(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








