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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO check if the resources are sufficient
def check_resources(coffee_chosen):
    chosen_ing = MENU[coffee_chosen]['ingredients']
    for ing in chosen_ing.keys():
        if chosen_ing[ing] > resources[ing]:
            return False, f"Sorry, There is not Enough {ing}."
    return True, "Please insert coins."


def process_coins():
    quarters = int(input('how many quarters?: ')) * 0.25
    dimes = int(input('how many dimes?: ')) * 0.10
    nickles = int(input('how many nickles?: ')) * 0.05
    pennies = int(input('how many pennies?: ')) * 0.01
    total_entered_money = quarters + dimes + nickles + pennies
    return total_entered_money


def check_cost(entered_money, coffee):
    if entered_money < MENU[coffee]['cost']:
        return "Sorry that is not enough money. Money refunded"
    else:
        change = "{:.2f}".format(entered_money - MENU[coffee]['cost'])
        deduct_resources(coffee)
        return f"Here is ${change} in change.\nHere is your {coffee} .Enjoy!"


def deduct_resources(coffee_chosen):
    chosen_ing = MENU[coffee_chosen]['ingredients']
    for ing in chosen_ing:
        resources[ing] -= chosen_ing[ing]


isOff = True
while isOff:
    # TODO: Prompt the user
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'report':
        # TODO: Print report
        report = "The resources are:\n"
        for key in resources.keys():
            report += f"{key}: {resources[key]}\n"
        print(report)

    elif user_input == "off":
        # TODO: Turn off the machine if user enters off
        isOff = False

    elif user_input in MENU.keys():
        if check_resources(user_input)[0]:
            print(check_resources(user_input)[1])
            total_money = process_coins()
            print(check_cost(entered_money=total_money, coffee=user_input))
        else:
            print(check_resources(user_input)[1])

    else:
        print("Sorry, We do not serve that.")

