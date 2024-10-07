class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget  
        self.__expenses = 0
        
    def get_category_name(self):
        return self.__category_name
    
    def set_name(self, new_category_name):
        self.__category_name = new_category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget 
    
    def set_allocated_budget(self, new_allocated_budget):
        if new_allocated_budget > 0:
            self.__allocated_budget = new_allocated_budget  
        else:
            print("Allocated budget must be a positive number.")
            
    def add_expense(self, amount):
        if amount > 0:
            if self.__allocated_budget >= amount:
                self.__expenses += amount 
                print(f"Expense added: ${amount}")
            else:
                print("Expense exceeds allocated budget.")
        else:
            print("Expense amount must be a positive number.")
        
    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Total Expenses: ${self.__expenses:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")
        
        
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()