from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self,n:int):
        try:
            if self._transactions:
                return self._transactions[n]

        except IndexError:
            return 'nothing found at that index position.'

    def __iterate__(self):
        for item in self._transactions:
            print(item)
    
    def __lt__(self, other):
        return self.balance() < other.balance()
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'


checking = Account('checking')
savings = Account('savings', 5)

