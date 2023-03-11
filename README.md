# 🍕PizzaOrderSystem🍕

## Project Overview💼 

Would you like to open a pizza shop? Then this project could be your dream project. The project aims to have users design their own pizzas and add the user to the database after paying. So what kind of tasks do we have in this project?

The Pizza Order system starts with the users choosing the pizza on the menu and the sauces they want.  They have to pay with their choice of sauce and pizza.  Users are required to pay by credit card.  Each pizza has a description and price.  Note that these values ​​must be set as a constant value within the classes.

## Creating a Google Colaboratory File🗃️

Make sure your project has .ipynb extension.
Make sure that there are comment lines explaining the details in your project.
When submitting the project, submit the cells of this .ipynb file so that the cells are run and the results are visible.

## Importing Required Libraries :octocat:
Import csv and datetime libraries

## Create “Menu.txt”🗞️
Create a file named Menu.txt and write the following text in it.

#### Please Choose a Pizza Base: 
- 1: Classic
- 2: Margherita 
- 3: TurkPizza 
- 4: PlainPizza 
#### And sauce of your choice: 
- 11: Olives 
- 12: Mushrooms 
- 13: GoatCheese 
- 14: Meat 
- 15: Onions 
- 16: Corn 
##### ´Enjoy your pizza!´

## Create superclass “pizza”🧀
Define the get_description() and get_cost() methods for encapsulation that creates the pizza class and inside this class.
This description should be a short description of the prepared pizza!

## Create subclass “pizza”🥩
Classic, Margherita, Turk Pizza, Dominos Pizza. Create pizza classes. Since each of these pizza types is a type of pizza, these classes will be defined as subclasses.
Don't forget that each pizza must have its own price and description of the pizzas as variables.

## Create superclass “Decorator”🍄
Create a decorator class. Decorator is called super class of all sauce classes here.
The decorator class will use the get_description() and get_cost() methods using the properties of the pizza class. Complete the decorator class using the following methods.

   def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)


   def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)

Determine Olives, Mushrooms, Goat Cheese, Meat, Onions, and Corn as sauces, and define each of the sauces you have determined as a class.
Don't forget that each sauce must have its own price and description of the pizzas as variables.
Create a main function. This function will print the menu on the screen first. Then let the user choose a pizza and sauce from the menu. After calculating the total price of the selected products, it should ask the user for a name, ID number, credit card number and credit card password. with all required information
Calculate the payments of the people who choose their pizza and keep the user's name, user id, credit card information, description of order, time order and credit card password in the "Orders_Database.csv" file, which we call the database.
