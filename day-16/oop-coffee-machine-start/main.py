from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_mk = CoffeeMaker()
money_m = MoneyMachine()


def coffee():
    request = input(f"What would you like?{menu.get_items()} :").lower()
    match request:
        case 'report':
            coffee_mk.report()
            money_m.report()
            return True
        case 'off':
            print("Turning off")
            return False
        case _:
            if menu.find_drink(request):
                if coffee_mk.is_resource_sufficient(menu.find_drink(request)) and money_m.make_payment(menu.find_drink(request).cost):
                    coffee_mk.make_coffee(menu.find_drink(request))
                    return True
                else:
                    return True
            else:
                print("Opção inválida.")
                return True


turnoff = coffee()
while turnoff:
    turnoff = coffee()
