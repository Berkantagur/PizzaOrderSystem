#Importing Required Libraries
import csv
import datetime

#Create superclass “pizza”
class pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

#Classic, Margherita, Turk Pizza, Dominos Pizza. Create pizza classes. 
#Since each of these pizza types is a type of pizza, these classes will be defined as subclasses.

class classicPizza(pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.price = 10.99
    
class margheritaPizza(pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.price = 13.49

class turkPizza(pizza):
    def __init__(self):
        self.description = "Turk Pizza"
        self.price = 12.99

class plainPizza(pizza):
    def __init__(self):
        self.description = "Plain Pizza"
        self.price = 8.49

#Create a decorator class. Decorator is called super class of all sauce classes here.

class decorator(pizza):
    def __init__(self, description, cost):
        pizza.__init__(description, cost)

    def get_description(self):
        return pizza.get_description()

    def get_cost(self):
        return pizza.get_cost()

#Determine Olives, Mushrooms, Goat Cheese, Meat, Onions, and Corn 
#as sauces, and define each of the sauces you have determined as a class. 
   
class olives(decorator):
    def __init__(self):
        self.cost = 1.99
        self.description = "Olives"

class mushrooms(decorator):
    def __init__(self):
        self.cost = 2.49
        self.description = "Mushrooms"
        
class goatCheese(decorator):
    def __init__(self):
        self.cost = 3.99
        self.description = "Goat Cheese"

class meat(decorator):
    def __init__(self):
        self.cost = 5.49
        self.description = "Meat"

class onions(decorator):
    def __init__(self):
        self.cost = 0.99
        self.description = "Onions"
             
class corn(decorator):
    def __init__(self):
        self.cost = 0.99
        self.description = "Corn"
        

def main():

    menu = open("menu.txt")
    print(menu.read())

    pizzaChoice = input("Please choose the pizza that you want (1-4): ")
    while pizzaChoice not in ["1", "2", "3", "4"]:
        pizzaChoice = input("Invalid input! Please choose a valid pizza number (from 1 to 4): ")

    if pizzaChoice == "1":
        yourPizza = classicPizza()
    
    elif pizzaChoice == "2":
        yourPizza = margheritaPizza()

    elif pizzaChoice == "3":
        yourPizza = turkPizza()

    else:
        yourPizza = plainPizza()

    
    sauceChoice = input("Please choose the sauce you want to add to your pizza (5-11)")
    while sauceChoice not in ["5", "6", "7", "8", "9", "10", "11"]:
        sauceChoice = input("Invalid input! Please choose a valid pizza number (from 5 to 11)")

    if sauceChoice == "5":
        yourPizzaSauce = olives()
    
    elif sauceChoice == "6":
        yourPizzaSauce = mushrooms()

    elif sauceChoice == "7":
        yourPizzaSauce = goatCheese

    elif sauceChoice == "8":
        yourPizzaSauce = meat()
    
    elif sauceChoice == "9":
        yourPizzaSauce = onions()

    elif sauceChoice == "10":
        yourPizzaSauce = corn()
    
    else:
        print("Not Sauce")
    

    payment = yourPizza.get_cost() + yourPizzaSauce.get_cost()

    name = input("Your Name: ")
    idNumber = input("Your ID Number: ")
    creditCardNumber= input("Your credit card number: ")
    creditCardPassword = input("Your credit card password: ")

    now = datetime.datetime.now()
    ordersTime = datetime.datetime.strftime(now, "%c")

    with open("Orders_Database.csv", mode = "a") as file:
        writer = csv.writer(file)
        writer.writerow([yourPizza.__class__.__name__, name, idNumber, creditCardNumber, creditCardPassword, ordersTime, payment])
    
    