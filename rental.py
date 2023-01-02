class roi_rental():
    def __init__(self, name):
        self.name = name
        self.invest_costs = {}
        self.income = {}
        self.expenses = {}
        
        
    def addinvestment(self):
        name = input('What is the name of the investment cost?')
        price = int(input('How much is the investment cost'))
        self.invest_costs[name] = price
        print(f'The {name} is {price} in price!')
        
    def deleteinvestment(self):
        name = input('What investment would you like to remove? ')
        print(f'{self.invest_costs[name]} has been removed from the roster!')
        del self.invest_costs[name]
        
    def addincome(self):
        print('Remember that this is a monthly number')
        name = input('What is the name of the investment cost?')
        price = int(input('How much is the investment cost'))
        self.income[name] = price
        print(f'The {name} is {price} in price!')
        
    def deleteincome(self):
        name = input('What investment would you like to remove? ')
        print(f'{self.income[name]} has been removed from the roster!')
        del self.income[name]
        
    def addexpense(self):
        print('Remember that this is monthly number')
        name = input('What is the name of the investment cost?')
        price = int(input('How much is the investment cost'))
        self.expenses[name] = price
        print(f'The {name} is {price} in price!')
        
    def delete_expense(self):
        name = input('What investment would you like to remove? ')
        print(f'{self.expenses[name]} has been removed.')
        del self.expenses[name]
        
    def calculate(self):
        inc = 0
        exp = 0
        inv = 0
        for k,v in self.income.items():
            inc += v
        for k,v in self.expenses.items():
            exp += v
        for k,v in self.invest_costs.items():
            inv += v
            
        cash_flow = (12 * inc) + (12 * exp)
        
        roi = cash_flow / inv
        
        print(f'Your will return on your in vestment in {roi} years.')
        
    def view(self):
        print(f'---------- Expenses ----------')
        for k,v in self.expenses.items():
            print(k,v)
        print(f'---------- Income ----------')
        for k,v in self.income.items():
            print(k,v)
            
        print(f'---------- Investments ----------')
        for k,v in self.invest_costs.items():
            print(k,v)
        
    def littleblackbook(self):
        while True:
            action = input("What would you like to do? (Add, Delete, Calculate, View)")
            if action.lower() == 'add':
                where = input('Where would you like to add to? (Expenses, Income, Investment)')
                if where.lower() == 'expenses':
                    self.addexpense()
                elif where.lower() == 'income':
                    self.addincome()
                elif where.lower() == 'investment':
                    self.addinvestment()
                else:
                    print('I am sorry that was not an option')
                
            elif action.lower() == 'delete':
                where = input('Where would you like to add to? (Expenses, Income, Investment)')
                if where.lower() == 'expenses':
                    self.delete_expense()
                elif where.lower() == 'income':
                    self.deleteincome()
                elif where.lower() == 'investment':
                    self.deleteinvestment()
                else:
                    print('I am sorry that was not an option')
                    
            elif action.lower() == 'calculate':
                self.calculate()
                
            elif action.lower() == 'view':
                self.view()
            else:
                print('I am sorry that was not an option')
unit_1 = roi_rental('Boca')