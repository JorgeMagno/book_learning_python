class AmountError(Exception):
    def __init__(self, number, holder, balance, overdraft_limit):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.overdraft_limit = overdraft_limit
    def __str__(self):
        return 'AmountError (Cannot deposit negative amounts) on Account Number:'+ self.number + ' - ' + self.holder +', ' +' account = ' + str(self.balance) + '-overdraft limit:' + str(self.overdraft_limit)

class BalanceError(Exception):
    def __init__(self, number, holder, balance, overdraft_limit):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.overdraft_limit = overdraft_limit
    def __str__(self):
        return 'Withdrawal would exceed your overdraft limit on Account Number:'+ self.number + ' - ' + self.holder +', ' +' account = ' + str(self.balance) + '-overdraft limit:' + str(self.overdraft_limit)
class Account:
    instance_count = 0
    @staticmethod
    def static_function():
        print('Conta Criada')
        
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        
    def __init__(self, number,holder, balance):
        Account.increment_instance_count()
        self.number = number
        self.holder = holder
        self.balance = balance
        Account.static_function()
        
    def __str__(self):
        return 'Account Number:'+ self.number + ' - ' + self.holder +', ' +' account = ' + str(self.balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise AmountError(self.number, self.holder, self.balance, self.overdraft_limit)
            
    def get_balance(self):
        return self.balance
    #balance = property(get_balance, doc="A balance property")
class DepositAccount(Account):
    def __init__(self, number, holder, balance, interest_rate):
        super().__init__(number, holder, balance)
        self.interest_rate = interest_rate
    def __str__(self):
        return super().__str__() + '-intereste rate:' + str(self.interest_rate)
        
    
class CurrentAccount(Account):
    def __init__(self, number, holder, balance, overdraft_limit):
        super().__init__(number, holder, balance)
        self.overdraft_limit = overdraft_limit
    def __str__(self):
        return super().__str__() + '-overdraft limit:' + str(self.overdraft_limit)
    def withdraw(self, amount):    
        if amount > 0:
            if amount <= self.overdraft_limit:
                self.balance -= amount
                return self.balance
            else:
                raise BalanceError(self.number, self.holder, self.balance, self.overdraft_limit)
        else:
            raise AmountError(self.number, self.holder, self.balance, self.overdraft_limit)
            
    
class InvestmentAccount(Account):
    def __init__(self, number, holder, balance, investment_type):
        super().__init__(number, holder, balance)
        self.investment_type = investment_type
    def __str__(self):
        return super().__str__() + '-investment type:' + str(self.investment_type)