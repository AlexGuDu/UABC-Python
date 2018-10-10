class Account:
    __acct_holder = ''
    __acct_balance = 0
    __acct_type = ''

    def __init__(self, acct_holder, acct_balance, acct_type):
        self.__acct_holder = acct_holder
        self.__acct_balance = acct_balance
        self.__acct_type = acct_type

    def get_holder(self):
        return self.__acct_holder


    def get_balance(self):
        return self.__acct_balance


    def get_type(self):
        return self.__acct_type


    def deposit(self, deposit):
        self.__acct_balance += deposit


    def withdraw(self, withdrawal):
        self.__acct_balance -= withdrawal


guy = Account('Mike', 3000, 'A')

print("Account holder information:")
print("Account holder: ", guy.get_holder())
print("Balance: ", guy.get_balance())
print("Account Type: ",guy.get_type())
print("---------------")

print("You're about to make a deposit and your current balance is: ", guy.get_balance())
guy.deposit(3000)
print("After your new deposit your current balance sits at: ", guy.get_balance())

print("---------------")

print("You're about to make a withdrawal and your current balance is: ", guy.get_balance())
guy.withdraw(4000)
print("After your withdrawal your current balance sits at: ", guy.get_balance())
