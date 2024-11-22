'''
You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, 
utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
- Initialize these attributes in the constructor.

- Expected Outcome: A `BudgetCategory` class capable of storing category details securely.


'''
# Define Budget Category Class with private attributes for category name and allocated budget
# Implement getters and setters. Include validation - budget should be a positive number
# Implement a method to add expenses
# Create a method to display details
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__category_name = new_name
            print(f"Category name updated to: {new_name}")
        else:
            print("Invalid category name!")
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_budget):

        if new_budget > 0:
            self.__allocated_budget = new_budget
            print(f"Allocated budget updated to: ${new_budget:.2f}")
        else:
            print("Budget must be a positive number.")

    def add_expense(self, amount):
        if amount > 0:
            if self.__expenses + amount <= self.__allocated_budget:
                self.__expenses += amount
                print(f"Expense of ${amount:.2f} added for {self.__category_name}.")
            else:
                print("Insufficient budget for this expense.")
        else:
            print("Expense amount must be positive.")

    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print("\n---- Budget Category Summary ----")
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Total Expenses: ${self.__expenses:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

# Code Examples
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

entertainment_category = BudgetCategory("Entertainment", 300)
entertainment_category.add_expense(175)
entertainment_category.display_category_summary()

utilities_category = BudgetCategory("Utilities", 900)
utilities_category.add_expense(450)
utilities_category.add_expense(350)
utilities_category.display_category_summary()


