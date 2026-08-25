'''
CERTIFICATION PROJECT 2 : BUDGET APP
'''


class Category:
    def __init__(self , name):
        self.name = name
        self.ledger = []
    
    def deposit(self , amount , description = ""):
        self.ledger.append({"amount": amount , "description":description})
        return self.ledger
    
    def withdraw(self , amount , description = ""):
        sucess = False
        transaction = {}
        if self.check_funds(amount) and not amount<=0:
            transaction["amount"] = -amount
            transaction["description"] = description
            self.ledger.append(transaction)
            sucess = True
        return sucess 
    def get_balance(self):
        balance = 0 
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
    def transfer(self , amount , other):
        transaction_here = {}
        transaction_destination = {}
        sucess = False
        if self.check_funds(amount) and not amount <=0:
            transaction_here["amount"] = -amount
            transaction_here["description"] = f"Transfer to {other.name}"
            self.ledger.append(transaction_here)
            transaction_destination["amount"] = amount
            transaction_destination["description"] = f"Transfer from {self.name}"
            other.ledger.append(transaction_destination)
            sucess = True
        return sucess
    def check_funds(self , amount):
        current_amount = self.get_balance()
        if amount>current_amount:
            return False
        else:
            return True
    def __str__(self):
        output = self.name.center(30 , "*")+"\n"
        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = f"{transaction['amount']:.2f}"
            output += f"{description: <23}{amount:>7}"+"\n"
        current = self.get_balance()
        output += f"Total: {current}"
        return output
        


def create_spend_chart(categories):
    percent = {}
    total = 0
    for category in categories:
        bills = category.ledger
        spending = 0
        for transaction in bills:
            if transaction['amount'] < 0:
                total += abs(transaction['amount'])
                spending += abs(transaction['amount'])
        percent[category.name] = spending
    for category in percent:
        percent[category] = round(percent[category]/total*100, 6)//10*10

    line = "Percentage spent by category\n"
    for y in range(100, -1, -10):
        line += f"{y:3}| "
        for category in categories:
            if percent[category.name] >= y:
                line += "o  "      
            else:
                line += "   "      
        line += "\n"

    spacing = len(categories)*3 + 1
    line += ("    " + "-"*spacing) + "\n"
    max_len = max(len(category.name) for category in categories)
    name = [c.name.ljust(max_len) for c in categories]
    for row in zip(*name):
        line += "     " + "".join(letter + "  " for letter in row) + "\n"
    return line.rstrip("\n")


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food , clothing]))





