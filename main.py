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

profit = [0]
change = [0]

def print_report():
  for resource in resources:
    print(f"{resource}: {resources[resource]}")
  print(f"money: ${profit[0]}")

def check_resources(drink):
  ingredients = MENU[drink]["ingredients"]
  x = False
  for resource in resources:
    if resource not in ingredients:
      pass
    elif ingredients[resource] > resources[resource]:
      print(f"Sorry, there is not enough {resource}.")
      
    else:
      x=True
  return x

def process_coins(drink):
  x=False
  price = MENU[drink]["cost"]

  coins = input("Enter numbers of quarters, dimes, nickels, pennies, separated by space: ").split()

  quarter = int(coins[0])
  dime = int(coins[1])
  nickel = int(coins[2])
  penny = int(coins[3])
  
  payment = sum([quarter*0.25, dime*0.1, nickel*0.05, penny*0.01])
  
  if price > payment:
    return x
  elif price == payment:
    x=True
    return x
  elif price < payment:
    x=True
    change[0] = round(payment - price, 2)
    return x
  else:
    return x

def tx_success(drink):
  if process_coins(drink) == False:
    print("Sorry that's not enough money. Returning your refund.")
    return False
  else:
    if change[0]>0:
      print(f"Here is {change[0]} in change.")
      change[0]=0
      return True
    else:
      return True

def make_coffee(drink):
  if tx_success(drink)==True and check_resources(drink)==True:
    for resource in resources:
      if resource not in MENU[drink]["ingredients"]:
        pass
      else:
        resources[resource] -= MENU[drink]["ingredients"][resource]
    profit[0]+=MENU[drink]["cost"]
    return f"Here is your {drink}, enjoy!"

def main():
  y=True
  while y==True:  
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink == "off":
      print("The machine is turning off.")
      break
    elif drink == "report":
      print_report()
    elif drink in ["cappuccino", "latte", "espresso"]:
      make_coffee(drink)
    else:
      print("Invalid input try again.")
      drink
