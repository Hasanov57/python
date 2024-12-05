import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

coins={"quarters":0.25,
       "dimes":0.10,
       "nickless":0.05,
       "pennies":0.01}
total=0
money=0
def report():
    resources["money"]=money
    for key,value in resources.items():
        print(f"{key}: {value}")
def off():
    sys.exit()
while True:
    coffe=input("What would you like?(espresso,latte,cappuccino): ")
    if coffe=="report":
        report()
        coffe = input("What whould you like?(espresso,latte,cappuccino): ")
        if coffe=="off":
            off()
    elif coffe=="off":
        off()
    print("insert coins.")
    for item in coins:
        cash=int(input(f"How much {item}? "))*coins[item]
        total=total+cash
    if coffe=="espresso":
        if MENU["espresso"]["cost"]>total:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change=total-MENU["espresso"]["cost"]
            print(f"Here is your in change: {round(change,2)}")
            total=MENU["espresso"]["cost"]
            money=money+total
            for item in resources:
                resources[item]=resources[item]-MENU["espresso"]["ingredients"][item]
            for items in resources:
                if resources[items]<=0:
                    print(f"Sorry , there is no enough {items}")
                    continue
            print(f"Here is your {coffe}. Enjoy!")
    elif coffe=="latte":
        if MENU["latte"]["cost"] > total:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = total - MENU["latte"]["cost"]
            print(f"Here is your in change: {round(change,2)}")
            total = MENU["latte"]["cost"]
            money = money + total
            for item in resources:
                resources[item] = resources[item] - MENU["latte"]["ingredients"][item]
            for items in resources:
                if resources[items] <= 0:
                    print(f"Sorry , there is no enough {items}")
                    continue
            print(f"Here is your {coffe}. Enjoy!")
    else:
        if MENU["cappuccino"]["cost"] > total:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = total - MENU["cappuccino"]["cost"]
            print(f"Here is your in change: {round(change,2)}")
            total = MENU["cappuccino"]["cost"]
            money = money + total
            for item in resources:
                resources[item] = resources[item] - MENU["cappuccino"]["ingredients"][item]
            for items in resources:
                if resources[items] <= 0:
                    print(f"Sorry , there is no enough {items}")
                    continue
                    print(f"Here is your {coffe}. enjoy!")