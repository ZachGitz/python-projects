from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
mnu =  Menu()
is_off = False

while not is_off:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if(choice.lower() =="off"):
        is_off= True
    elif(choice.lower()=="report"):
        coffeemaker.report()
        moneymachine.report()
    else:
        order = mnu.find_drink(choice)
        if(order==None):continue
        if (coffeemaker.is_resource_sufficient(order)):
            if(moneymachine.make_payment(order.cost)):
                coffeemaker.make_coffee(order)



