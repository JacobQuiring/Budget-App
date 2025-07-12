class Category:

    def __init__(self, category):

        self.ledger = []
        self.balance = 0
        self.category = category


    def __str__(self):

        display = f'{self.category:*^30}\n'
        for item in self.ledger:
            item_amount = f"{item['amount']:.2f}"
            display += f"{item['description'][:23].ljust(30 - len(item_amount))}{item_amount[:7]}\n"
        display += f'Total: {self.balance:.2f}'
        return str(display)

    
    def deposit(self, amount, description=''):

        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount


    def withdraw(self, amount, description=''):

        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else: 
            return False


    def transfer(self, amount, transfer_account):

        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {transfer_account.category}'})
            self.balance -= amount
            transfer_account.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
            transfer_account.balance += amount
            return True
        else: 
            return False


    def get_balance(self):
        return self.balance
    

    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False


def create_spend_chart (categories):

    total_expense = 0
    category_expenses = []
    count = 0
    
    

    for category in categories:

        category_expenses.append(0)

        for expense in category.ledger:
            if expense['amount'] < 0:
                total_expense += expense['amount']
                category_expenses[count] += expense['amount']
        
        
            
                

        count += 1



    title = 'Percentage spent by category\n'
    percentages = []
    line = f'    {"-"*len(categories*3)}-\n'
    names = ''
    max_name_length = max(len(category.category) for category in categories)
    adjusted_categories = ([name.category.ljust(max_name_length) for name in categories])
    print(adjusted_categories)

    for i in range(11):
        percentages.append(f'{str(i*10):>3}| ')
        
        for expense in category_expenses:
            
            if (expense/total_expense)*10 >= i:
                percentages[i] += 'o  '
            else:
                percentages[i] += '   '
        percentages[i] += '\n'
    percentages.reverse()

    for i in range(max_name_length):
        names += '     '
        for name in adjusted_categories:
            names += f'{name[i]}  '
        names += '\n'

    return title + ''.join(percentages) + line + names.rstrip('\n')


test = Category('Test')
test.deposit(100.01, 'deposit test')
test.withdraw(5, 'withdraw test')
test.withdraw(5, 'withdraw testing the range')
test2 = Category('Test2')
test.transfer(20, test2)
test2.deposit(500, 'test2 deposit')
test2.withdraw(100, 'test2 withdraw')
print(create_spend_chart([test, test2]))
