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
    "money": 0
}


def processcoin(price):
    global resources
    while True:
        quarter = int(input("How much Quarters?"))
        dimes = int(input("How much Dimes?"))
        nickels = int(input("How much Nickels?"))
        pennies = int(input("How much Pennies?"))
        money = quarter*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.05
        if money - price < 0:
            print("That's not enough.")
            stop = input("Try again(t) / Cancel(c): ").lower()
            if stop == 'c':
                return False
        else:
            print(f"Here is ${round((money - price),2)} dollars in change")
            resources["money"] += price
            return True


def coffee():
    request = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    match request:
        case 'espresso':
            if resources["water"] < 50:
                print("Sorry there is not enough water.")
                return True
            elif resources["coffee"] < 18:
                print("Sorry there is not enough coffee.")
                return True
            elif processcoin(1.5):
                resources["water"] -= 50
                resources["coffee"] -= 18
                return True
            else:
                return True
        case 'latte':
            if resources["water"] < 200:
                print("Sorry there is not enough water.")
                return True
            elif resources["coffee"] < 24:
                print("Sorry there is not enough coffee.")
                return True
            elif resources["milk"] < 150:
                print("Sorry there is not enough milk.")
                return True
            elif processcoin(2.5):
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
                return True
            else:
                return True
        case 'cappuccino':
            if resources["water"] < 250:
                print("Sorry there is not enough water.")
                return True
            elif resources["coffee"] < 24:
                print("Sorry there is not enough coffee.")
                return True
            elif resources["milk"] < 100:
                print("Sorry there is not enough milk.")
                return True
            elif processcoin(3.0):
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
                return True
            else:
                return True

        case 'report':
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: ${resources["money"]}")
            return True
        case 'off':
            print("Turning off")
            return False
        case _:
            print("Opção inválida.")
            return True


turnoff = coffee()
while turnoff:
    turnoff = coffee()





