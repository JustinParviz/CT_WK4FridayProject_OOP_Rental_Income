
# Calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property. And now that we know a thing or two about making our programs run more efficiently, try utilizing some of the strategies we talked about this week for optimization!

# Your Program should have the following (this is not an exhaustive list but just base functionality):

# -  There should be some sort of Driver code for users to choose what to do next 

# -  There should be a way to store multiple users and for users to be able to have multiple different properties (This might be done by creating a User Class & a Property class similarly to how we did it with the Codeflix program)

# -  Properties should be able to store multiple different types of expenses (i.e. taxes, mortgage, insurance, etc) and multiple different types of incomes (i.e. rent, laundry, parking, etc)

# -  The ROI needs to be calculated & displayed to the user and should also be stored for that specific property.

# This project will be completed individually, though you can feel free to share ideas with your fellow students.

# Once completed, commit the project to github and submit the link to this assignment.


# <--------------------------------------------------------------------------------------------------------->

# Theater was comparable to Driver Class. Driver Class and Code should go at the bottom!

class User: # Comparable to User
    def __init__(self, name):
        self.title = None
        self.name = name
        self.property_list = []

        

class Property: # Comparable to Series Class
    def __init__(self, name, address):
        self.title = None
        self.name = name
        self.address = address
        self.total_expenses = 0    # Expenses
        self.taxes = 0
        self.mortgage = 0
        self.insurance = 0
        self.utilities = 0
        self.total_income = 0      # Incomes
        self.rent = 0
        self.laundry = 0
        self.parking = 0
        self.total_roi = 0




    def property_incomes(self): # Have to figure out Total Incomes
        print("Hello, and Welcome to the Ultimate Rental Property Calculator where together, we will decide if a certain property is the right investment for you!")
        print("To begin, lets focus on how much INCOME you expect this property to generate.")
        self.rent = int(input("How much do you think you'll be able to charge monthly for the rent? "))
        self.laundry = int(input("Around how much do you think you'll be able to make off of the laundry room? "))
        self.parking = int(input("How much revenue do you think you'll bring in off of charging for monthly parking? "))
        self.total_income = self.rent + self.laundry + self.parking
        print(f"Ok Great. Now based on you being able to charge {self.rent} per month for the rent, around {self.laundry} a month off of the laundry room, combined with the {self.parking} 
        in monthly revenue off of the parking, you're projected total income is {self.total_income} for this property.")


    def property_expenses(self): # Have to figure out Total Expenses
        print("Now, let's focus on the EXPENSES associated with the property by breaking down all of it's costs.")
        self.taxes = int(input("How much are the monthly taxes associated with this property? "))
        self.mortgage = int(input("How much will your mortgage be every month? "))
        self.insurance = int(input("How much will you be paying monthly for the insurance? "))
        self.utilities = int(input("And how much do you think your monthly utilities (electricity, water, gas, etc) will cost? "))
        self.total_expenses = self.taxes + self.mortgage + self.insurance + self.utilities
        print(f"Ok so based on your monthly taxes costing around {self.taxes}, your mortgage of {self.mortgage} per month, {self.insurance} monthly for the insurance, and about 
        {self.utilities} a month for all of the utilities, your total monthly expenses are expected to be about {self.total_expenses} for this property.")


    
    def property_roi(self): #ROI = Total Monthly Income - Total Monthly Expenses
        self.total_roi = self.total_income - self.total_expenses
        
        if self.total_roi > 0:
            print(f"Based on all the information you provided, this property is cash flow positive and has a monthly ROI of {self.total_roi}. Congratulations!")
        elif self.total_roi <= 0:
            print(f"Sorry but based on all the information you provided, this property is cash flow negative since your Total Monthly Expenses of {self.total_expenses} outweighs 
            your Total Monthly Income of {self.total_income}. Maybe you'd be better off looking at other properties.")
        


