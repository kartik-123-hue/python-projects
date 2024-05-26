class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=list()
    def __str__(self):
        title=f"{self.name:*^30}\n"
        items=""
        total=0
        for item in self.ledger:
            try:
                left=item['description'][0:23]
            except TypeError:
                left=''
            right=str("{:.2f}".format(item['amount']))
            items+=f"{left:<23}{right:>7}\n"
        output=title+items+"Total: "+str(self.get_balance())
        '''
        print("Ledger:")
        for item in self.ledger:
            print(f"Description: {item['description']}, Amount: {item['amount']}")
        '''
        return output
        
        
    def deposit(self,amount,description=""):
        #Add the amount and with that the description
        self.ledger.append({"amount": amount,"description":description})
        
        
    def withdraw(self,amount,description=""):
        #withdrawal amount is showcased 
        #shows if the amount is present or not by returning T oFalse
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -(amount),"description":description})
            return True
        return False
        
        
    def get_balance(self):
        #this returns the total balance that the person has used after
        #after making all the deposits and withdrawal
        total_cash=0
        for item in self.ledger:
            total_cash+=item["amount"]
        return total_cash
        
        
    def transfer(self,amount,category):
        #the transfering of an amount for a certain categories
        """
            the category.deposit will make another category
            so intial we have Ground Deposit lets take 100
            not from the 100 we need to transfer it to the 
            clothing category that is lets take 20
            when we do that then Ground Deposit in the 
            category==clothing will have 20 and it will deducted
            initial 100 that is 100-20 that is 80(balance)
        """
        if (self.check_funds(amount)):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")  
            return True
       
        return False
        
        
    def check_funds(self,amount):
        if(self.get_balance()>=amount):
            return True
        return False
        
        
    def get_withdrawals(self):
        total=0
        for item in self.ledger:
            if item["amount"]<0:
                total+=item["amount"]
        return total
        
def truncate(n):
    multiplier=10
    return int(n*multiplier)/multiplier
        
        
def getTotals(categories):
    total=0
    breakdown=[]
    for category in categories:
        total+=category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded=list(map(lambda x:truncate(x/total),breakdown))
    return rounded
        
def create_spend_chart(categories):
    
    to_print = "Percentage spent by category\n"
    i = 100
    percentages = getTotals(categories)
    while i >= 0:
        to_print += str(i).rjust(3) + '| '
        for percentage in percentages:
            if percentage * 100 >= i:
                to_print += 'o  '
            else:
                to_print += '   '
        to_print += '\n'
        i -= 10
    bar = '    ' + '-' * (3 * len(categories) + 1) + '\n'
    to_print += bar
    max_length = max(len(category.name) for category in categories)
    names = [category.name for category in categories]
    for i in range(max_length):
        name_str = '     '
        for name in names:
            if i < len(name):
                name_str += name[i] + '  '
            else:
                name_str += '   '
        if i < max_length - 1:
            name_str += '\n'
        to_print += name_str
    return to_print
