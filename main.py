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

#we use lists for these so we don't have to mess with global variables
profit = [0]
change = [0]

def print_report(): #prints a report of the levels of inventory of each resource, as well as accumulated profits
  for resource in resources:
    print(f"{resource}: {resources[resource]}")
  print(f"money: ${profit[0]}")

def check_resources(drink): #compares our ingredents on hand to the ingredients for the recipe and says not enough or it returns a True value
  ingredients = MENU[drink]["ingredients"]
  x = False  #by default the function returns False
  for resource in resources:
    if resource not in ingredients: #handles case where not all resources are used as ingredients
      pass
    elif ingredients[resource] > resources[resource]:
      print(f"Sorry, there is not enough {resource}.")
    else:
      x=True  #if input passes all checks, returns True
  return x

def process_coins(drink): #if user pays enough money, returns True
  x=False
  price = MENU[drink]["cost"]

  #input should look like "1 1 1 1" to represent 1 quarter, 1 dime, 1 nickel, 1 penny
  coins = input("Enter numbers of quarters, dimes, nickels, pennies, separated by space: ").split()

  quarter = int(coins[0])
  dime = int(coins[1])
  nickel = int(coins[2])
  penny = int(coins[3])
  
  payment = sum([quarter*0.25, dime*0.1, nickel*0.05, penny*0.01])
  
  if price > payment: #returns False if insufficient payment
    return x
  elif price == payment: #returns True if payment is exact change
    x=True
    return x
  elif price < payment: #returns True and also gives user back their change if they pay more than the price of the drink
    x=True
    change[0] = round(payment - price, 2)
    return x
  else:
    return x

def tx_success(drink): #Checks if user inserst enough money to purchase the drink they select
  if process_coins(drink) == False:
    print("Sorry that's not enough money. Returning your refund.")
    return False
  else:
    if change[0]>0: #Returns precise amount of change and returns True if they overpay
      print(f"Here is {change[0]} in change.")
      change[0]=0
      return True
    else:  #Just return True for exact payment
      return True

def make_coffee(drink):
  if tx_success(drink)==True and check_resources(drink)==True: #This function will only run if payment succeeds and there are enough resources
    for resource in resources:
      if resource not in MENU[drink]["ingredients"]: #Handles case where drink uses fewer resources than whats on hand
        pass
      else: #Subtracts each resource from resources on hand
        resources[resource] -= MENU[drink]["ingredients"][resource]
    profit[0]+=MENU[drink]["cost"]  #Adds cost of drink to profit registers
    return f"Here is your {drink}, enjoy!"

def main(): #Putting it all together
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
