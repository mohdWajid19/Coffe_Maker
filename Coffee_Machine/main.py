from replit import clear
from menu import MENU,resources
money_earned = 0
enough_resources = False
  

def check_resources(dish):
    for resource in resources:
        if (resources[resource] - MENU[dish]['ingredients'][resource]) < 0 :
            return False
    return True

def add_money(money):
    '''function to increase the money earned'''
    global money_earned
    money_earned += money

def ask_money(dish):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = float(input("enter the no of quarters : "))
    dimes = float(input("enter the no of dimes : "))
    nickles = float(input("enter the no of nickles : "))
    pennies = float(input("enter the no of pennies : "))
    return evaluate_money(quarters, dimes, nickles, pennies, dish)

def evaluate_money(quarters, dimes, nickles, pennies, dish):
    total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    money_req = MENU[dish]['cost']
    if (total_money - money_req) < 0:
        print(f"The Amount was in sufficient {round(total_money,2)} refunded")
        return False
    elif total_money == money_req:
        print(f"Your Order for {dish} is Being Processed")
        add_money(money_req)
        return True
    else:
        print(f"Here is ${round(total_money - money_req, 2)} change\n order is confirmed and is being processed") 
        add_money(money_req)
        return True

def send_report():
    # resources
    for resource in resources:
        print(resources[resource])
    print(f"Money_Earned : {money_earned}")


def turn_off():
    exit()

def deduct_resources(dish):
    for resource in resources:
        resources[resource] -= MENU[dish]['ingredients'][resource]
        

def make_dish(dish):
    if check_resources(dish):
        if ask_money(dish) :
            deduct_resources(dish)
            return f"here is your ☕ {dish}"
    else:
        return f"not enough resources for making {dish}"
    

  

while not enough_resources:
    clear()
    user_need = input(f"What Would You Like To Have\n ☕ espresso : ${MENU['espresso']['cost']}\n ☕ latte : ${MENU['latte']['cost']} \n ☕ cappuccino : ${MENU['cappuccino']['cost']} \n make me a :: ")
    if user_need == 'espresso' or user_need == "latte" or user_need == 'cappuccino':
        print(make_dish(user_need))
    elif user_need == 'off':
        print(turn_off())
    elif user_need == 'report':
        send_report()
    else:
        print("We Dont Understand what you need check menu again and input from menu ")
    if input("One more ☕?? (y/n) : ").lower() != 'y':
        break

